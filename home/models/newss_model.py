from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse
# Create your models here.

class News(models.Model):
    
    #News
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    img = CloudinaryField('img')
    datetime = models.DateTimeField(auto_now=False)
    link = models.CharField(max_length=500)
    
    class Meta:
        verbose_name = ("news")
        verbose_name_plural = ("newss")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('newss', kwargs={'slug': self.slug})


