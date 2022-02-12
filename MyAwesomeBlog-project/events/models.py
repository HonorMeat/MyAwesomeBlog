from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=300, name="Title", default="Title")
    image = models.ImageField(upload_to='event_images/' ,name="Image")
    text = models.CharField(max_length=300, name="Text", default="Text")