"""
URL configuration for projectwo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from django.contrib.auth import views as auth_views
from inputbook import views as inputbook_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('principal/', include('principal.urls')),  # Incluir las URLs de la aplicación principal
    path('inputbook/', include('inputbook.urls')),
    path('', include('registro.urls')),  # Incluir las URLs de registro
    path('', lambda request: redirect('principal/'), name='root'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Aquí está la URL de login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL de logout
    path('login/', inputbook_views.custom_login, name='login'),

]
