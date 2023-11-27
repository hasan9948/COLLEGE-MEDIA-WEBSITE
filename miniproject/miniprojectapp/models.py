from django.db import models

class academictable(models.Model):
    
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.FileField( upload_to="academicimg/", max_length=300,null=True,default=None)
    datetime=models.DateTimeField(auto_now=False,auto_now_add=True)
    type=models.CharField(max_length=50)
   
    
    



# Create your models here.
class culturaltable(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.FileField( upload_to="academicimg/", max_length=300,null=True,default=None)
    datetime=models.DateTimeField(auto_now=False,auto_now_add=True)
    type=models.CharField(max_length=50)
   


class eventstable(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.FileField( upload_to="academicimg/", max_length=300,null=True,default=None)
    datetime=models.DateTimeField(auto_now=False,auto_now_add=True)
    type=models.CharField(max_length=50)
    date = models.CharField(max_length=10) 
    




class nsstable(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.FileField( upload_to="academicimg/", max_length=300,null=True,default=None)
    datetime=models.DateTimeField(auto_now=False,auto_now_add=True)
    type=models.CharField(max_length=50)
    date = models.CharField(max_length=10) 
    


class placementstable(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.FileField( upload_to="academicimg/", max_length=300,null=True,default=None)
    datetime=models.DateTimeField(auto_now=False,auto_now_add=True)
    type=models.CharField(max_length=50)
    


class sportstable(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.FileField( upload_to="academicimg/", max_length=300,null=True,default=None)
    datetime=models.DateTimeField(auto_now=False,auto_now_add=True)
    type=models.CharField(max_length=50)
    


   
class rightmsgtable(models.Model):
    name=models.TextField()
    