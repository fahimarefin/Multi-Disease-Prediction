# prediction_app/forms.py
from django import forms
from .models import Contact
from .models import UserProfile
class ImageUploadForm(forms.Form):
    image = forms.ImageField()
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'description']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['fname', 'lname', 'email', 'password', 'dob', 'gender', 'mobile', 'profile_picture']