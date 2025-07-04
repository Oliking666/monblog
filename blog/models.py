from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    date_published = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title
