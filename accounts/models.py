from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Agent(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(max_length=100,unique=True,blank=True)
    phone_number = models.CharField(max_length=10,unique=True,blank=True,null=True)
    profile_image = models.ImageField(upload_to='images/agents/', blank=True)
    slug = models.SlugField(null=True,blank=True,unique=True)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('accounts:agent',kwargs={'slug': self.slug})