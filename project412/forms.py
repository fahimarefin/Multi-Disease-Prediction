# prediction_app/forms.py
from django import forms
from .models import Contact
class ImageUploadForm(forms.Form):
    image = forms.ImageField()
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'description']