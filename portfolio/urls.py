from django.contrib import admin
from django.urls import path

from DjangoProject1 import views
from DjangoProject1.views import jobapp

urlpatterns = [
    path('portfolios/', views.list, name='list'),
    path('portfolios/<int:portfolio_id>/', views.detail, name='detail'),
    path('projects/', views.project, name='project'),
]
