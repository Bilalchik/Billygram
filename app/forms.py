from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class PostCreateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['image', 'description']



class SerchForm(forms.Form):
	search = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))