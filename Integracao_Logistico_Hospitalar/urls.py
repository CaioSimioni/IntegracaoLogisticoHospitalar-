from django.contrib import admin
from django.urls import path, include
from intloghosp_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('gerenciamento/', include('intloghosp_app.urls_gerenciamento')),
    path('prontuario/', include('intloghosp_app.urls_prontuario')),
    path('login/', views.login, name='login'),
    path('logout', views.view_logout, name='view_logout')
]