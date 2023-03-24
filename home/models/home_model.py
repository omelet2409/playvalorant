from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Home(models.Model):
    
    
    
    
    
    class Meta:
        verbose_name = ("home")
        verbose_name_plural = ("homes")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home_detail', kwargs={'slug': self.slug})
        

    def save(self, *args, **kwargs):  #new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)