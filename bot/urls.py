from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views.index import *


app_name='bot'
urlpatterns = [
    url(r'^$',index,name='index'),
]