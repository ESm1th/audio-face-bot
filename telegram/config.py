import os

from dotenv import load_dotenv


# load environment variables from `.env` file
load_dotenv()

DEBUG = bool(int(os.environ['DEBUG']))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_DIR = os.path.join(BASE_DIR, 'media')
PHOTOS_DIR = os.path.join(MEDIA_DIR, 'photos')
VOICES_DIR = os.path.join(MEDIA_DIR, 'voices')

HOST = 'localhost'
PORT = 8000

BOT_TOKEN = os.environ['BOT_TOKEN']
