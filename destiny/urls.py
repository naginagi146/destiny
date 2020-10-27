from django.urls import path
from . import views

app_name= 'destiny'

urlpatterns = [
    path('', views.RouletteListView.as_view(), name='roulette_list'),
    path('create/', views.RouletteCreateView.as_view(), name='roulette_create'),
]