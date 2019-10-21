from django import forms
from django.contrib.auth.models import User

def clean_phonenumber(number):
    return number.isdigit()

class formRegister(forms.Form):

    username = forms.CharField(label='username', max_length=20)
    cellphone = forms.CharField(label='cellphone', max_length=20)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password confirmation', widget=forms.PasswordInput)

    def checkUsername(self):
        username = self.cleaned_data.get('username')
        if len(username) < 6:
            raise forms.ValidationError('Your username is too short!')
        elif len(username) > 20:
            raise forms.ValidationError('Your username is too long!')
        else:
            username_filter = User.objects.filter(username__exact=username)
            if len(username_filter) > 0:
                raise forms.ValidationError('Your username is exist.')
        return username

    def checkPassword(self):
        Password = self.cleaned_data.get('password1')
        if len(Password) < 8:
            raise forms.ValidationError('Your password is too short')
        return Password

    def checkPasswod2(self):
        Password1 = self.cleaned_data.get('password1')
        Password2 = self.cleaned_data.get('password2')
        if Password1 != Password2:
            raise forms.ValidationError('Your confirmed password is not same.')
        return Password2

    def checkcellphone(self):
        cellphone = self.cleaned_data.get('cellphone')
        if len(cellphone) != 12 or not cellphone.isdigit():
            raise forms.ValidationError('Please input correct phone number.')
        return cellphone

class formLogin(forms.Form):

    username = forms.CharField(label='username', max_length=20)
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    def checkUsername(self):
        username = self.cleaned_data.get('username')

        if len(username) < 6:
            raise forms.ValidationError('Your username is too short!')
        elif len(username) > 20:
            raise forms.ValidationError('Your username is too long!')
        else:
            username_filter = User.objects.filter(username__exact=username)
            if len(username_filter) != 1:
                raise forms.ValidationError('This username is not exist. Please register first.')

        return username
