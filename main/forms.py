from typing import Any
from django import forms
from .models import Member
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MemberForms(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name','gender','number','location','age','quote','location',]

        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your name'}),
            'gender': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Gender'}),
            'location': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Location'}),
            'number': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Number'}),
            'age': forms.TextInput(attrs={'placeholder':'Enter Your Age','class':'form-control'}),
            'quote': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Your Favourites Quote'}),
           
        }


class Registerform(UserCreationForm):
    email = forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(Registerform,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'