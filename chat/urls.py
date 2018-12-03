from django.conf.urls import url, include

from django.contrib.auth.views import PasswordChangeView
from django.views.generic import TemplateView
from chat.views import *
from chat import views
app_name='chat'
urlpatterns=[
    url(r'^in/$',views.host,name='ind'),
    url(r'^ch/',views.sea,name='srh'),
]