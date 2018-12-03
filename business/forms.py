from business.models import Business,Add
from django import forms


class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        fields=['buser','email','phone','pas']

class AddsForm(forms.ModelForm):
    class Meta:
        model=Add
        fields=['name','location','phone','price','offers','hotelfacilities','roomfacilities','inhouseservice','photo','photo1']

class LoginFrom(forms.Form):
    class Meta:
        fields=['username','password']

