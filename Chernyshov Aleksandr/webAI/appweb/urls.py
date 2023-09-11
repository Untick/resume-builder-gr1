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
#from .views import *

app_name = 'appweb'

urlpatterns = [
                path('', views.main_view),                       #, name='main_view'),
                path('index/', views.index), #, name='index'),
                path('cv_view/', views.cv_view), #, name='cv_view'),
                path('dashboard_view/', views.dashboard_view), #, name='dashboard_view'),
                path('edit_cv_view/', views.edit_cv_view) ,#, name='edit_cv_view'),
                path('edit_cv_order_view/', views.edit_cv_order_view), #, name='edit_cv_order_view'),
                path('edit_liter_view/', views.edit_liter_view), #, name='edit_liter_view'),
                path('edit_liter_order_view/', views.edit_liter_order_view), #, name='edit_liter_order_view'),
                path('liter_view/', views.liter_view), #, name='liter_view'),
                path('login_view/', views.login_view),#, name='login_view'),
                path('registration_view/', views.registration_view) #, name='registration_view'),
            ]
