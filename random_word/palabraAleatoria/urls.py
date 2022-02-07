from django.urls import path     
from . import views
urlpatterns = [
    path('restart', views.restart_counter),
    path('random', views.aleatoria),
    path('', views.index),
]