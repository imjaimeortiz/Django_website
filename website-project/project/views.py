from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'project/home.html')

def show_projects(request):
    return render(request, 'project/projects.html')