"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from blog.views import *
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import url, include

from django.contrib import admin
from django.template.context_processors import static
from mydjango import settings
from patterns import patterns
from django.conf.urls.static import static
admin.autodiscover()
from django.conf.urls import include, url
from django.contrib import admin
from crypto.views import get_crypto


admin.site.site_header='Django Blog Admin Panel'
admin.site.site_title='Blog Admin Panel'
admin.site.index_title='Dblog Administration'

urlpatterns = [
    # here we are not using pattern module like in previous django versions
    url(r'^admin/', include(admin.site.urls)),
    url(r'',include("blog.urls")),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'',include("business.urls")),
    url(r'',include("chat.urls")),
    url(r'cryp/',include("crypto.urls")),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
