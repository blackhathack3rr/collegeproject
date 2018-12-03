from django.db import models


# Create your models here.

class ChatServer(models.Model):
    cuser = models.ForeignKey('auth.user')
    message = models.TextField()
    created = models.TimeField(auto_now_add=True)
    def __str__(self):
        return "{} in ({})".format(self.cuser, self.message, self.created)