from django.db import models

# Create your models here.
class prolductdb(models.Model):
    proname = models.CharField(max_length=50,null=True,blank=False)
    proprize = models.CharField(max_length=50,null=True,blank=False)
    prodesc = models.CharField(max_length=50,null=True,blank=False)
    proimage = models.ImageField(upload_to='proimage/',null=True,blank=False)
    
class cartdb(models.Model):
    name =  models.CharField(max_length=50,null=True,blank=False)
    prize = models.CharField(max_length=50,null=True,blank=False)
    quantity = models.CharField(max_length=50,null=True,blank=False)