from django.db import models

# Create your models here.

class Register(models.Model):
    Fname=models.CharField(max_length=50)
    Lname=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Phoneno=models.BigIntegerField(default=0)
    Add= models.CharField(max_length=50,default='')
    def __str__(self):
        return self.Fname + self.Lname
    