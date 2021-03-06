import os
from io import BytesIO
from urllib.parse import urlencode

import asks
import cv2
from sanic import Sanic, response
from pydub import AudioSegment

from config import (
    BOT_TOKEN,
    HOST,
    PORT,
    DEBUG,
    DIRS
)
from face_detection import FaceDetector


app = Sanic(__name__)
face_detector = FaceDetector()

API_URL = 'https://api.telegram.org/'
BOT_URL = API_URL + 'bot' + BOT_TOKEN + '/'
BOT_FILE_URL = API_URL + 'file/' + 'bot' + BOT_TOKEN


@app.post('/')
async def request_handler(request):
    """
    Route function to handle request data depending on data's keys.
    Return empty request with status code 204.
    """
    message = request.json.get('message')
    if 'photo' in message:
        await photo_handler(message)
    elif 'voice' in message:
        await voice_handler(message)
    return response.empty()


async def voice_handler(message: dict) -> None:
    """Getting voice file, process it and save to local dir."""
    voice = message['voice']
    mime_type = voice['mime_type'].split('/').pop()
    file_path = create_filepath(message, DIRS['voices'], 'audio', 'wav')

    # send request to get filepath of voice file
    voice_info_response = await asks.get(
        create_get_file_info_url(voice['file_id'])
    )
    voice_file_path = voice_info_response.json()['result']['file_path']

    # download voice file from telegram
    file_response = await asks.get(BOT_FILE_URL + '/' + voice_file_path)

    # process and save voice file
    voice_memory_file = BytesIO(file_response.body)
    audio = AudioSegment.from_file(voice_memory_file, format=mime_type)
    audio = audio.set_frame_rate(16000)
    audio.export(file_path, format='wav')


async def photo_handler(message: dict) -> None:
    """
    Getting image file, detecting faces on it and saving it to local dir
    if face/faces exists.
    """
    photo = message['photo'].pop()

    # send request to get filepath of photo file
    photo_info_response = await asks.get(
        create_get_file_info_url(photo['file_id'])
    )
    photo_file_path = photo_info_response.json()['result']['file_path']

    # download photo file from telegram
    file_response = await asks.get(BOT_FILE_URL + '/' + photo_file_path)

    # detect faces on image
    image = face_detector.load_image_from_bytes(file_response.body)
    faces = face_detector.detect_faces(image)

    # save image if face/faces exists on it
    if not isinstance(faces, tuple):
        path = create_filepath(message, DIRS['photos'], 'image', 'png')
        cv2.imwrite(path, image)


def create_get_file_info_url(file_id: str) -> str:
    """Return an url to get a file."""
    return BOT_URL + 'getFile?' + urlencode({'file_id': file_id})


def create_filepath(message: dict, dir: str, file_type: str, mime: str) -> str:
    """
    Construct file path from the arguments passed.
    `file_type` - 'audio' for voices or 'image' for images.
    """
    user_id = str(message['from']['id'])
    user_path = os.path.join(dir, user_id)

    if not os.path.exists(user_path):
        os.mkdir(user_path)

    filename = '{type}_message_{num}.{mime}'.format(
        type=file_type,
        num=len(os.listdir(user_path)),
        mime=mime
    )
    return os.path.join(user_path, filename)


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
