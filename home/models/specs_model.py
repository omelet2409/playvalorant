from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Spec(models.Model):
    
    #Agent
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    img = CloudinaryField('img')
    slug = models.SlugField()
    
    

    class Meta:
        verbose_name = ("spec")
        verbose_name_plural = ("specs")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('specs_detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
