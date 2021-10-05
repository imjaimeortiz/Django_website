from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    return render(request, 'project/home_parallax.html')

def show_projects(request):
    projects = Project.objects.all()
    # This is to print from last added to oldest
    last_projects = projects[::-1]
    return render(request, 'project/projects.html', {'projects': last_projects})