from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_model, name='model'),
    path('<int:shooting_id>/', views.show_shooting, name='shooting'),
]
