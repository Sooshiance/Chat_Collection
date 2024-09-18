from django import forms 

from .models import User


class Register(forms.ModelForm):
    """"""
    class Meta:
        model = User
        fields = ['phone', 'username', 'password']

        labels = {
            'password': 'گذر واژه',
        }
        
        widgets = {
            'phone': forms.NumberInput(attrs={'class':'form-control my-5', 'placeholder':'09123456789'}),
            'username': forms.TextInput(attrs={'class':'form-control my-5', 'placeholder':'Username'}),
            'password': forms.PasswordInput(attrs={'class':'form-control my-5', 'placeholder':'••••••••••••'}),
        }
