from django.urls import path

from . import views


app_name = 'bot'

urlpatterns = [
    path(
        '',
        views.DispatcherView.as_view(),
        name='main'
    ),
    path(
        'send-message/',
        views.SendMessage.as_view(),
        name='send-message'
    ),
    path(
        'face-detection/',
        views.FaceDetection.as_view(),
        name='face-detection'
    )
]
