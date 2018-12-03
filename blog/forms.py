from blog.models import Comments, Post, Contact
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['name','email','comment_body']


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','location','duration','budget','maxattitude','bestseason','experiencerequired','carrying','attraction','hotels','body','publish','photo','photo1','photo2','photo3']

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['email','subject','body']



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email=forms.EmailField(help_text='Enter a valid email')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','email' )






