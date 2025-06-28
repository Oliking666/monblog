from django import forms
from .models import Article
from monblog.validators import validate_image_extension, validate_file_size

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].validators.extend([
            validate_image_extension,
            lambda x: validate_file_size(x, max_size=5)  # 5MB pour les articles
        ])
