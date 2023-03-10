from django.db import models

# Create your models here.


class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.email

