from django.forms import ModelForm
from django.forms import Textarea
from .models import Contacts


class ContactForm(ModelForm):

    class Meta:
        # Определяем модель, на основе которой создаем форму
        model = Contacts
        # Поля, которые будем использовать для заполнения
        fields = ['name', 'email', 'message']
        widgets = {
            'message': Textarea(
                attrs={
                    'placeholder': 'Please, give a feedback'
                })
        }