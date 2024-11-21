from django.db import models

# Create your models here.
class Card(models.Model):
    img = models.ImageField(upload_to='cards/images')
    name = models.CharField(max_length=100)
    position = models.TextField()
    url = models.URLField()