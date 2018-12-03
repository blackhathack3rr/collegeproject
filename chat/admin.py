from django.contrib import admin
from chat.models import ChatServer
# Register your models here.

class ChatAdmin(admin.ModelAdmin):
    list_display = ['cuser','message','created']
admin.site.register(ChatServer,ChatAdmin)