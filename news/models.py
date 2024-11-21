from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='news/images')
    date = models.DateField(auto_now_add=True)