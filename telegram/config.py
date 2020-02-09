import os

from dotenv import load_dotenv

# load environment variables from `.env` file
load_dotenv()

DEBUG = bool(int(os.environ['DEBUG']))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

DIRS = {
    'media': MEDIA_DIR,
    'photos': os.path.join(MEDIA_DIR, 'photos'),
    'voices': os.path.join(MEDIA_DIR, 'voices')
}

for dir in DIRS.values():
    if not os.path.exists(dir):
        os.mkdir(dir)

HOST = 'localhost'
PORT = 8000

BOT_TOKEN = os.environ['BOT_TOKEN']
