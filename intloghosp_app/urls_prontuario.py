from django.urls import path
from . import views

urlpatterns = [
  path('', views.prontuario, name='prontuario'),
  path('cadastrar/', views.cad_prontuario, name='cad_prontuario')
]