from django import forms
from ebiz import models as e_models


class ContactForm(forms.ModelForm):

	class Meta:
		model = e_models.Contacts
		fields = ['fullname']