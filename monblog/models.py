from django.db import models
from django.contrib.auth.models import User
from blog.validators import validate_image_extension, validate_file_size
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/', validators=[
            validate_image_extension,
            lambda x: validate_file_size(x, max_size=5)
        ], blank=True, null=True)
    
    def __str__(self):
        return self.title

class Post(models.Model):
    title= models.CharField(max_length=200)
    content=models.TextField()
    featured_image= modelss.ImageField(upload_to='blog_image/')
    thumbnail= ImageSpecField(
        sorce='featured_image',
        format='JPEG',
        options={'quality': 80}
    )
    def __str__(self):
        return self.title