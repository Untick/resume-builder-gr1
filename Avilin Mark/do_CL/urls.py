from django.urls import path
from . import views

urlpatterns = [
    path('create_cl/', views.create_cl, name='create_cl'),
    path('update_cl', views.update_cl, name='update_cl'),
]
