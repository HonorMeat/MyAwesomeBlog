from django.db import models

class Event(models.Model):
    i = models.ImageField(upload_to='event_images/')
    t = models.CharField(max_length=300)