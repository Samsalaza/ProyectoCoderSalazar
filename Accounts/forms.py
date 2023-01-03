from django import forms

class signupForm (forms.Form):
    user_name=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=254, required=True)
    password=forms.CharField(label="Password", widget=forms.PasswordInput, strip=False)
