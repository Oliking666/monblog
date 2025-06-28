from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    url = models.URLField(blank=True)
    date = models.DateField()
    
    def __str__(self):
        return self.title
