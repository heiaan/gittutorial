from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('porcelain', views.Porcelain, name='porcelain'),
    path('ancillary', views.Ancillary, name='ancillary'),
    path('interaction', views.Interaction, name='interaction'),
    path('interrogation', views.Interrogation, name='interrogation'),
    path('manipulation', views.Manipulation, name='manipulation'),
    path('syncing', views.Syncing, name='syncing'),
    path('helper', views.Helper, name='helper'),
    path('mistakes', views.Mistakes, name='mistakes'),
]
