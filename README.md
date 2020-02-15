# audio_face_bot
Telegram bot that save audio messages and photos with faces from chat to local directories.

### How to start
Create telegram `bot` and obtain `token`. You can check how to do that by this [link](https://core.telegram.org/bots#6-botfather)

Clone repository:
```
$ git clone https://github.com/ESm1th/audio_face_bot.git
```

Change working directory to project:
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

Send request to set `webhook`:
```
$ curl https://api.telegram.org/bot{your_bot_token}/setWebHook?url=https://afafe4e.ngrok.io
```

Response for this request:
```
$ {"ok":true,"result":true,"description":"Webhook was set"}
```
Ok. Bot is running, local web server is running, `ngrok` is running and webhook is set.

### Bot's working logic
Bot must work in `disabled` private mode.
This mode can be set by sending `/setprivacy` command in chat with `BotFather` in telegram. Than select your bot and further select `Disable`. After this manipulation `BotFather` send you message: `Success! The new status is: DISABLED.`

Create group or channel and add created `bot` to it. From this moment every message from every member of this group/channel will send to server and processed.

All voices will convert to `wav` with frame rate `16000` and saved to local folder `telegram/media/voices/`.

All images with face/faces on them will saved to local folder `telegram/media/photos/`. 
