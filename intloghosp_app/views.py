from django.shortcuts import render
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required
import os
from dotenv import load_dotenv

# Create your views here.
def login(request):
  if request.method == "GET":
    return render(request, 'login.html')
  else:
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user:
      django_login(request, user)
      return redirect('home')
    else:
      return HttpResponse('Usuário ou senha inválidos.')

@login_required(login_url='/login/')
def home(request):
  return render(request, 'home.html')

@login_required(login_url='/login/')
def view_logout(request):
  logout(request)
  return redirect('login')

@login_required(login_url='/login/')
def prontuario(request):
  return render(request, 'prontuario/prontuario.html')

@login_required(login_url='/login/')
def cad_prontuario(request):
  return render(request, 'prontuario/cad_prontuario.html')

@login_required(login_url='/login/')
def gerenciamento(request):
  return render(request, 'gerenciamento/gerenciamento.html')