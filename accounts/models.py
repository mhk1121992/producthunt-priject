from django import forms


class SignUp(forms.ModelForm):
    name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class Login(forms.ModelForm):
    email = forms.EmailField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)