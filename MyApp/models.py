from django.db import models
from django.utils import timezone

# Create your models here.
class MyUser(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    cpassword=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.TextField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipCode=models.CharField(max_length=100)
    genderType=models.CharField(max_length=100)

    def __str__(self):
	    return self.fname+" "+self.lname