

from django.db import models
from django.db.models import CASCADE

from django.utils import timezone

class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager,self).get_queryset() \
            .filter(status='published').order_by('-created')

class Contact(models.Model):
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    body=models.TextField()
    def __str__(self):
        return "{} in ({})".format(self.email, self.subject, self.body)


class Post(models.Model):
    STATUS_CHOICES=(
        ('draft','Draft'),
        ('published','Published')
    )
    title=models.CharField(max_length=150)
    location=models.CharField(max_length=300)
    author=models.ForeignKey('auth.User',related_name='blog_posts')
    duration=models.CharField(max_length=20)
    budget=models.CharField(max_length=100)
    attraction=models.CharField(max_length=1000)
    maxattitude=models.CharField(max_length=50)
    bestseason=models.CharField(max_length=500)
    experiencerequired=models.CharField(max_length=1000)
    carrying=models.CharField(max_length=1000)
    hotels=models.CharField(max_length=2000)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    photo=models.ImageField(blank=True)
    photo1=models.ImageField(blank=True)
    photo2=models.ImageField(blank=True)
    photo3=models.ImageField(blank=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    #managers
    objects=models.Manager()
    published=PublishManager()
    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title


class Comments(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(blank=True,null=True)
    post_id=models.ForeignKey("Post",related_name='post_comments', on_delete=CASCADE)
    comment_body=models.TextField(max_length=200)

    def __str__(self):
        return "{} in ({})".format(self.name,self.post_id.title)



from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email=models.EmailField(null=True,blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

