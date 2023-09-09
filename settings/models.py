from django.db import models

# Create your models here.



class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company')
    subtitle = models.TextField(max_length=100)
    facebook_link = models.URLField(null=True,blank=True, max_length=200)
    twiter_link =  models.URLField(null=True,blank=True, max_length=200)
    youtube_link =  models.URLField(null=True,blank=True, max_length=200)
    phones= models.TextField(max_length=100,null=True,blank=True)
    email = models.TextField(max_length=100,null=True,blank=True)
    address = models.TextField(max_length=100,null=True,blank=True)
    android_app = models.TextField(max_length=100,null=True,blank=True)
    ios_app = models.TextField(max_length=100,null=True,blank=True)
    call_us = models.TextField(max_length=100,null=True,blank=True)
    email_us = models.CharField(max_length=100,null=True,blank=True)





    def __str__(self):

        return self.name