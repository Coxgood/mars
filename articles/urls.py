"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('article/', article, name='article'),
    path('properties/', properties, name='properties'),
    path('reviews/', reviews, name='reviews'),
    path('review_add/', review_add, name='review_add'),
    path('office/', office, name='office'),
    path('article/<str:id>/', article_detail, name='article_detail'),
]