from django.db import models
class Posts(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='event_images/')

    def get_summary(self):
        return self.text[:70]