from django.urls import path     
from . import views
urlpatterns = [
    path('random', views.aleatoria),
    path('', views.index),
]