from django import forms

from .models import Room


class RegisterRoom(forms.ModelForm):
    """"""

    class Meta:
        model = Room
        fields = ['title']
