from django.shortcuts import render

from django.views.generic import CreateView
from .models import Contacts
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import ContactForm


class ContactCreate(CreateView):
    model = Contacts
    success_url = reverse_lazy('success_page')
    form_class = ContactForm

    def form_valid(self, form):
        data = form.data
        subject = f'Сообщение с формы от {data["name"]} Почта отправителя: {data["email"]}'
        email(subject, data['message'])
        return super().form_valid(form)


def email(subject, content):
    send_mail(subject,
              content,
              'polja.malygina@gmail.com',
              ['polja.malygina@gmail.com']
              )


def success(request):
    return render(request, 'contact_form/success_page.html')
