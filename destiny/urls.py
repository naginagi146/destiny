from django.urls import path
from . import views

app_name= 'destiny'

urlpatterns = [
    path('', views.RouletteListView.as_view(), name='roulette_list'),
    path('detail/<int:pk>/', views.RouletteDetailView.as_view(), name='roulette_detail'),
    path('random/<int:pk>/', views.RandomRouletteView.as_view(), name='random'),
    path('result/<int:pk>/', views.ResultView.as_view(), name='result'),
    path('create/', views.RouletteCreateView.as_view(), name='roulette_create'),
    path('update/<int:pk>/', views.RouletteUpdateView.as_view(), name='roulette_update'),

]