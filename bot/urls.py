from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views.index import *
from .views.chattbot import *


app_name='bot'
urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^$', ChatterBotAppView.as_view(), name='main'),
    url(r'^api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
]