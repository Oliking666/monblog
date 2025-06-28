from django.shortcuts import render
from blog.models import Article

# Create your views here.
from portfolio.models import Project

def home(request):
    latest_articles = Article.objects.all().order_by('-date_published')[:3]
    latest_projects = Project.objects.all().order_by('-date')[:3]
    return render(request, 'pages/home.html', {
        'latest_articles': latest_articles,
        'latest_projects': latest_projects
    })
