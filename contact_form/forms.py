from django.forms import ModelForm
from django.forms import Textarea, TextInput, EmailInput
from .models import Contacts


class ContactForm(ModelForm):

    class Meta:
        model = Contacts
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name'}),
            'email': EmailInput(attrs={'placeholder': 'Email'}),
            'message': Textarea(
                attrs={'placeholder': 'Please, give a feedback'})
        }