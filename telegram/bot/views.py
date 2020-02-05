import os
import json

import requests
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import RedirectView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from telegram.settings import BOT_URL


class DispatcherView(RedirectView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request):
        return super().dispatch(request)

    def post(self, request):
        data = json.loads(request.body)
        cb_query = data.get('callback_query')
        if cb_query:
            if cb_query['data'] == 'face':
                return FaceDetection.as_view()(request)
            elif cb_query['data'] == 'audio':
                return JsonResponse({})  # to do 
        elif data.get('message'):
            return SendMessage.as_view()(request)


class SendMessage(RedirectView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request):
        return super().dispatch(request)

    def post(self, request):
        data = json.loads(request.body)
        payload = {
            'chat_id': data['message']['chat']['id'],
            'text': 'data',
            'reply_markup': {
                'inline_keyboard': [[
                    {'text': 'Face', 'callback_data': 'face'},
                    {'text': 'Audio', 'callback_data': 'audio'}
                ]]
            }
        }
        requests.post(BOT_URL + 'sendMessage', json=payload)
        return JsonResponse({})


class FaceDetection(RedirectView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request):
        return super().dispatch(request)

    def post(self, request):
        data = json.loads(request.body)
        cb_query = data.get('callback_query')
        payload = {
            'chat_id': cb_query['message']['chat']['id'],
            'text': 'test'
        }
        requests.post(BOT_URL + 'sendMessage', json=payload)
        return JsonResponse({})