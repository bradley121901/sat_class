from django import forms

class register_form(forms.Form):
    username = forms.CharField(label="username", max_length=30)
    password = forms.CharField(label="password", max_length=30)
    firstname = forms.CharField(label="firstname", max_length=30)
    lastname = forms.CharField(label="lastname", max_length=30)
    email = forms.CharField(label="email", max_length=30)
