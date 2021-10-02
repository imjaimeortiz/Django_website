from django.shortcuts import render

# Create your views here.
def show_fitness(request):
    return render(request, 'fitness/fitness.html')