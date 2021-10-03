from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    return render(request, 'project/home.html')

def show_projects(request):
    projects = Project.objects
    return render(request, 'project/projects.html', {'projects': projects})