from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_member),
    path('<int:pk>/', views.read_member),
    path('update/<int:pk>/', views.update_member),
    path('delete/<int:pk>/', views.delete_member)
]