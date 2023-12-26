from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from home.models import Comment

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields =('first_name','last_name','username','email','password')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #! Remove password fields from form
        # self.fields.pop('password1')
        self.fields.pop('password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class SearchForm(forms.Form):
    query = forms.CharField(max_length=30)