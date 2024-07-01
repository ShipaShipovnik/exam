from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Application

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    third_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "third_name","username", "email", "phone", "password1", "password2")

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        exclude = ['status','user']
        fiedls = ['car', 'descr']
        widgets = {
            'descr': forms.Textarea(attrs={'rows': 4}),
        }
