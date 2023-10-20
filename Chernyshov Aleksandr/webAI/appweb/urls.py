"""
URL configuration for CV_maker_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from appweb import views
from django.urls import path, include
from django.contrib import admin
#from .views import *

app_name = 'appweb'

urlpatterns = [
                #path("admin/", admin.site.urls),
                path('test/', views.test_view), #, name='index'),
                path('', views.index, name='index'),
                path('cv_view/', views.cv_view, name='cv_view'),
                path('dashboard_view/', views.dashboard_view, name='dashboard_view'),
                path('edit_cv_view/', views.edit_cv_view, name='edit_cv_view'),
                path('edit_cv_order_view/', views.edit_cv_order_view, name='edit_cv_order_view'),
                path('edit_litter_view/', views.edit_litter_view, name='edit_litter_view'),
                path('edit_litter_order_view/', views.edit_litter_order_view, name='edit_litter_order_view'),
                path('litter_view/', views.litter_view, name='litter_view'),
                path('login_view/', views.login_view, name='login_view'),
                path('registration_view/', views.registration_view, name='registration_view'),
                path('promt_view/', views.promt_view, name='promt_view'),
                path('post/<int:id>/', views.post, name='post'),
                path('create_post/', views.create_post, name='create_post'),
            ]
