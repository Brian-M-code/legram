from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='pictures/')
    caption = models.TextField(max_length=30)
    name = models.CharField(max_length=30)
    
    # def __str__(self):
    #     return self.name