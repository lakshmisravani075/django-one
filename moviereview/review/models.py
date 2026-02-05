from django.db import models



# Create your models here.

class movie_detials(models.Model):
    movie_name=models.CharField(max_length=100,unique=True)
    date=models.CharField(max_length=100)
    budget=models.CharField(max_length=100)
    rating=models.FloatField()
    
    
    
    
    class Users(models.Model):
     username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    password = models.CharField(max_length=255)   # store hashed password

    def __str__(self):
        return self.username


    
