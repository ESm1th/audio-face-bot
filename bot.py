from sanic import Sanic, response 


app = Sanic(__name__)


@app.post('/')
def request_router(request):
    message = request.json.get('message')
    if 'photo' in message:
        return response.redirect('/photo')
    elif 'voice' in message:
        return response.redirect('/voice')
    return response.empty()


@app.post('/photo')
def photo_handler(request):
    message = request.json.get('message')
    for photo in in message['photo']:
        photo.update({})
    return response.empty()    


if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)