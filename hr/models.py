from django.db import models


# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=30)
    email= models.EmailField()
    desc = models.TextField()

    def __str__(self):
        return self.name + "-"+ self.email

class task(models.Model):
    nam = models.CharField(max_length=30)
    desc = models.TextField()

    def __str__(self):
        return self.nam
    

class leave(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    leavetype = models.CharField(max_length=500)
    datestart = models.CharField(max_length=50)
    dateend = models.CharField(max_length=50)
    reason = models.TextField()
    halfday = models.CharField(max_length=10)

    def __str__(self):
        return self.name +'-'+ self.email
    
class login(models.Model):
    uname = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.uname