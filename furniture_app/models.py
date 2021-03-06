from django.db import models

# Create your models here.

class Register(models.Model):
    Fname=models.CharField(max_length=50)
    Lname=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Phoneno=models.BigIntegerField(default=0)
    Add= models.CharField(max_length=50,default='')
    Image=models.ImageField(upload_to='images/',default='avtar.png')
    def __str__(self):
        return self.Fname + " " + self.Lname
    
class Contact(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Subject=models.CharField(max_length=50)
    Message=models.TextField()

    def __str__(self):
        return self.Name

class Kitchen_Images(models.Model):
    Kitchen_Image=models.ImageField(upload_to='images/',default="",blank=True)
   
class Wardrobe_Image(models.Model): 
    Wardrobe_Image=models.ImageField(upload_to='images/',default="",blank=True)
    
class Tvcabinet_Image(models.Model):     
    Tvcabinet_Image=models.ImageField(upload_to='images/',default="",blank=True)

class Pvcdoor_Image(models.Model): 
    Pvcdoor_Image=models.ImageField(upload_to='images/',default="",blank=True)

class Wallpanelling_Image(models.Model):
    Wallpanelling_Image=models.ImageField(upload_to='images/',default="",blank=True)

class Designerceiling_Image(models.Model):
    Designerceiling_Image=models.ImageField(upload_to='images/',default="",blank=True)

class Upvcwindow_Image(models.Model): 
    Upvcwindow_Image=models.ImageField(upload_to='images/',default="",blank=True)

class Pvcparition_Image(models.Model): 
    Pvcparition_Image=models.ImageField(upload_to='images/',default="",blank=True)
    