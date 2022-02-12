from cgitb import text
from unicodedata import name
from django.db import models
from django.forms import CharField
class Posts(models.Model):
    title = models.CharField(max_length=50, name='Заголовок')
    date = models.DateTimeField(name='Дата')
    text = models.TextField(name='Текст')
    image = models.ImageField(upload_to='event_images/', name='Картинка')
