from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Agent(models.Model):
    
    #Agent
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    img = CloudinaryField('img')
    slug = models.SlugField()
    
    #skill q
    skill_q_name = models.CharField( max_length=50)
    skill_q_icon = CloudinaryField('icon', transformation=[{'width' : 180, 'height' : 180,'crop' : 'fill'}])
    skill_q_video = CloudinaryField(resource_type='gif')
    skill_q_description = models.CharField(max_length=250)
    
    #skill e
    skill_e_name = models.CharField( max_length=50)
    skill_e_icon = CloudinaryField('icon', transformation=[{'width' : 180, 'height' : 180,'crop' : 'fill'}])
    skill_e_video = CloudinaryField(resource_type='gif')
    skill_e_description = models.CharField(max_length=250)
    
    #skill c
    skill_c_name = models.CharField( max_length=50)
    skill_c_icon = CloudinaryField('icon', transformation=[{'width' : 180, 'height' : 180,'crop' : 'fill'}])
    skill_c_video = CloudinaryField(resource_type='gif')
    skill_c_description = models.CharField(max_length=250)
    
    #skill x
    skill_x_name = models.CharField( max_length=50)
    skill_x_icon = CloudinaryField('icon', transformation=[{'width' : 180, 'height' : 180,'crop' : 'fill'}])
    skill_x_video = CloudinaryField(resource_type='gif') 
    skill_x_description = models.CharField(max_length=250)
    

    class Meta:
        verbose_name = ("agent")
        verbose_name_plural = ("agents")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('agent_detail', kwargs={'slug': self.slug})
        

    def save(self, *args, **kwargs):  #new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    