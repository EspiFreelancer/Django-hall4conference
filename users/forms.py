from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

# class CustomUserCreationForm(UserCreationForm):

# 	class Meta(UserCreationForm):
# 		model = CustomUser

# class CustomUserChangeForm(UserChangeForm):

# 	class Meta:
# 		model = CustomUser
# 		fields = ('username', 'email')

# 		fields = ('username', 'email')


class SignUpForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('first_name', 'last_name','email', 'is_tenant','is_owner', 'country', 'state')
