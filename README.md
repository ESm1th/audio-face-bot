# audio_face_bot
Telegram bot that save audio messages and photos with faces from chat to database.

### How to start
Create telegram `bot` and obtain `token`. You can check how to do that by this [link](https://core.telegram.org/bots#6-botfather)

Clone repository:
```
$ git clone https://github.com/ESm1th/audio_face_bot.git
```

Change working derictory to project:
```
$ cd audio_face_bot
```

Create virtual environment and activate it:
```
$ mkvirtualenv tbot --python=python3
```

Install dependencies:
```
$ pip install -r requirements.txt
```

Add `.env` file to project's folder with following variables:
```
BOT_TOKEN=some_telegram_bot_token  # token obtained in first step
DEBUG=0  # 0 - no, 1 - yes 
```

Change derictory to `telegram` folder:
```
$ cd telegram
```

From one terminal run `ngrok`:
```
$ ./ngrok http 8000
```

From another terminal from `telegram` folder run python script:
```
$ python bot.py
```

At this moment local server running. The last step - setting `webhook` to our bot.

From the `ngrok` running terminal copy `https` forwarding url.

For example forwarding row in opened terminal with running `ngrok`
```
https://afafe4e.ngrok.io -> http://localhost:8000
```
You should copy this part - `https://afafe4e.ngrok.io`
