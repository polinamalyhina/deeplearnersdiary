from django.shortcuts import render
#
# # Create your views here.
# from django.shortcuts import render
#
# # Create your views here.
#
#
# def contact_form(request):
#     return render(request, 'main/contacts_form.html')


from django.views.generic import CreateView
from .models import Contacts
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm


class ContactCreate(CreateView):
    model = Contacts
    # fields = ["first_name", "last_name", "message"]
    success_url = reverse_lazy('success_page')
    form_class = ContactForm

    def form_valid(self, form):
        # Формируем сообщение для отправки
        data = form.data
        subject = f'Сообщение с формы от {data["name"]} Почта отправителя: {data["email"]}'
        email(subject, data['message'])
        return super().form_valid(form)


# Функция отправки сообщения
def email(subject, content):
    send_mail(subject,
              content,
              'polja.malygina@gmail.com',
              ['polja.malygina@gmail.com']
              )


# Функция, которая вернет сообщение в случае успешного заполнения формы
def success(request):
    return render(request, 'contact_form/success_page.html')
