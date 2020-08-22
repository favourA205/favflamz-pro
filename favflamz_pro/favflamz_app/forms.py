from django import forms
from .models import RegistrationData,signIn

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationData
        fields = [
            'username',
            'password',
            'Email',
            'Phone_number'
        ]



        widgets = {
            'username':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter username'
            }),

            'password':forms.TextInput(attrs={
                    'class':'form-control',
                    'placeholder':'Enter password'
            }),

            'Email':forms.EmailInput(attrs={
                    'class':'form-control',
                    'placeholder':'Enter Email'
            }),

            'Phone_number':forms.NumberInput(attrs={
                    'class':'form-control',
                    'placeholder':'Enter Phone number'
            }),

        }


class signInform(forms.ModelForm):
    class Meta:
        model = signIn
        fields = [
            'username',
            'password',
        ]



        widgets = {
            'username':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter username'
            }),

            'password':forms.TextInput(attrs={
                    'class':'form-control',
                    'placeholder':'Enter password'
            }),
        }




