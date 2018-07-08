"""CatchUp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from .views import CreateUserView,create_post,HomeView,PostDetailView,MyPostsView

urlpatterns = [
    path('', TemplateView.as_view(template_name='app/homepage.html'),name='homepage'),
    path('catchup/', HomeView.as_view(),name='home'),
    path('myposts/', MyPostsView.as_view(),name='myposts'),
    path('details/<int:pk>', PostDetailView.as_view(),name='details'),
    path('createpost/', create_post,name='create_post'),
    path('thankyou/', TemplateView.as_view(template_name='app/thankyou.html'),name='thankyou'),
    path('signup/',CreateUserView.as_view(),name='signup')
]
