from django.conf.urls import url, include
from business import views
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import TemplateView

app_name='bus'
urlpatterns=[
    url(r'^busi/$', views.business,name='index'),
    url(r'^adds/$', views.adds,name='adds'),
    url(r'^dashboard/$', views.login,name='dashboard'),




]