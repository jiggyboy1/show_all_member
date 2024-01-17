from django import forms
from .models import Member


class MemberForms(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name','number','location','age','quote','location']