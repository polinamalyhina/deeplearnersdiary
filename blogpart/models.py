from django.db import models

# Create your models here.


class BlogPublications(models.Model):
    title = models.CharField('Title', max_length=300)
    theme = models.CharField('Theme of publication', max_length=150)
    anons = models.CharField('Anons', max_length=250)
    full_text_1 = models.TextField('Text')
    full_text_2 = models.TextField('Text')
    full_text_3 = models.TextField('Text')
    full_text_4 = models.TextField('Text')
    full_text_5 = models.TextField('Text')
    full_text_6 = models.TextField('Text')
    full_text_7 = models.TextField('Text')
    full_text_8 = models.TextField('Text')
    full_text_9 = models.TextField('Text')
    full_text_10 = models.TextField('Text')

    date = models.DateField('Date of publication')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
