from django.urls import path
from . import views

urlpatterns = [
    path('create_cv/', views.create_cv, name='create_cv'),
    path('update_cv', views.update_cv, name='update_cv'),
]
