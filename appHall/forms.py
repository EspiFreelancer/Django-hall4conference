from django import forms

from .models import User, Owner

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'country', 'state',)

class isOwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('is_owner', 'name_company',)
    
