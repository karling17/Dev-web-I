from django import forms

from app1.models import Users

class Userform(forms.ModelForm):
    class meta:
        model: Users
        fields: '__all__'
        