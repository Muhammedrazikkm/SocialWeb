from django import forms
from django.contrib.auth.models import User
from api.models import Posts

class Userform(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password","email"]

class Loginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

class Postform(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["title","description"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"})
        }

class PostEditform(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["title","description"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"})
        }