from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='account'),    #http://127.0.0.1:8000/
    path('registration/', RegistrationUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('update/<int:user_id>/', RegistrationUser.as_view(), name='update_user'),
    path('delete/<int:user_id>/', RegistrationUser.as_view(), name='delete_user'),
]

