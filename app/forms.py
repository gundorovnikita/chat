from django import forms 
from .models import *

class send_message(forms.ModelForm):
	class Meta:
		model = Message 
		fields = ['content',]