from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    return render(request, 'project/home2.html')

def show_projects(request):
    projects = Project.objects.all()
    last_projects = sort_latest(projects)
    return render(request, 'project/projects.html', {'projects': last_projects})

# This is to print from last added to oldest
def sort_latest(projects):
    sorted = projects.order_by('-pub_date')
    print(sorted)
    return sorted