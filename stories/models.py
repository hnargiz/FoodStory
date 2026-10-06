from django.db import models

# Create your models here.
class Story(models.Model):
    image = models.ImageField(upload_to='stories/')
    publish_date = models.DateField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'