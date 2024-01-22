from django import forms
from .models import Member


class MemberForms(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name','number','location','age','quote','location']

        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your name'}),
            'location': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Location'}),
            'number': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Number'}),
            'age': forms.TextInput(attrs={'placeholder':'Enter Your Age','class':'form-control'}),
            'quote': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Your Favourites Quote'}),

        }