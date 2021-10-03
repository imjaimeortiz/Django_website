from django.db.models.base import Model
from django.shortcuts import get_object_or_404, render
from .models import Shooting

# Create your views here.
def show_model(request):
    shootings = Shooting.objects
    return render(request, 'model/model.html', {'shootings': shootings})

def show_shooting(request, shooting_id):
    shooting = get_object_or_404(Shooting, pk=shooting_id)
    return render(request, 'model/shooting.html', {'shooting': shooting})