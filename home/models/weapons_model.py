from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Weapon(models.Model):
    
    #Weapons
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    dmg_h = models.CharField(max_length=500)
    dmg_b = models.CharField(max_length=500)
    dmg_l = models.CharField(max_length=500)
    img = CloudinaryField('img')
    slug = models.SlugField()
    weapon_detail = models.CharField(max_length=500)
    

    class Meta:
        verbose_name = ("weapon")
        verbose_name_plural = ("weapons")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('weapon_detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
