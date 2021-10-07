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
    return sorted

# Buttons for languages
def show_languages(request, language_id):

    projects_in_language = Project.objects.all().filter(language=language_id)    
    last_projects = sort_latest(projects_in_language)
    return render(request, 'project/language.html', {'projects' : last_projects, 'language' : language_id})