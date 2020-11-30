from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Listing(models.Model):
    image = models.ImageField(blank = True, null=True,upload_to='images/')
    name = models.CharField(max_length = 500 ,blank=True, null=True)
    agent = models.ForeignKey(User,on_delete= models.CASCADE,null=True)
    current_owner = models.CharField(max_length = 500 ,blank=True, null=True)
    price = models.CharField(max_length = 500 ,blank=True, null=True)
    address = models.TextField(max_length=2000,blank=True,null=True)
    desc = models.TextField(max_length=2000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_listing',args=[str(self.id)])
