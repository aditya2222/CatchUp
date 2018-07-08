from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Post
User = get_user_model()


class SignUpForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['username','email','password1','password2']


class CreatePostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = '__all__'

