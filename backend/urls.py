"""
URL configuration for backend project.

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
from django.urls import path,include,re_path
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from appadministrador.views import LoginView,LogoutView,UserInfoView

urlpatterns = [
    path('admin/', admin.site.urls),
     path('api/login/', LoginView.as_view(), name='login'),
     path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
     path('user-info/', UserInfoView.as_view(), name='user_info'),
    path('api/', include('appadministrador.urls')),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]
