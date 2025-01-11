from django.db import models

# Create your models here.
class Movie(models.Model): 
    id = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=255) 
    genre = models.CharField(max_length=100) 
    director_name = models.CharField(max_length=255) 
    release_year = models.IntegerField() 
    synopsis = models.TextField() 
    
    def __str__(self): 
        return self.title