from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    return render(request, 'project/home_parallax.html')

def show_projects(request):
    projects = Project.objects.all()
    list = projects.values_list('title', flat=True)
    values = []
    for object in list:
        values.append(object)
    projects = values[::-1]
    return render(request, 'project/projects.html', {'projects': projects})