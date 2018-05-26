from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

LEVELCHOICES = ((1, _('Teacher')), (2, _('Student')))

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	level = forms.ChoiceField(choices=LEVELCHOICES, label= "", initial = '', widget=forms.Select(), required = True) 

   class Meta:
       model = User
       fields = ('username', 'first_name', 'last_name', 'email', 'level', 'password1', 'password2', )