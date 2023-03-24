from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Map(models.Model):
    
    #Maps
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    img = CloudinaryField('img')
    slug = models.SlugField()
    
    #map detail
    
    map_location = models.CharField(max_length=250)
    
    
    class Meta:
        verbose_name = ("map")
        verbose_name_plural = ("maps")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('map_detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
