from django.db import models

# Create your models here.

class Userdata(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=20)
    number=models.CharField(max_length=12)
    city=models.CharField(max_length=30)
    email=models.EmailField(max_length=200)
    regarding=models.TextField(max_length=200)
    
    def __str__(self):
        return self.firstname
        
    class Meta:
        verbose_name = 'Userdata'
        verbose_name_plural = 'Userdatas'    
    