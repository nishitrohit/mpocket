from django.db import models

# Create your models here.

class userinfo(models.Model):
    Name = models.CharField(max_length=100,default='',editable=False)
    Mobileno = models.CharField(max_length=10,default='',editable=False)
    Email = models.EmailField(max_length=200,default='',editable=False)
    add = models.CharField(max_length=100,default='',editable=False)
    village = models.CharField(max_length=100,default='',editable=False)


