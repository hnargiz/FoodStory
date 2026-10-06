from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')
    
    daily_visitors = models.IntegerField(default=0) 
    stories = models.IntegerField(default=0)
    recipes = models.IntegerField(default=0)
    users = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title 