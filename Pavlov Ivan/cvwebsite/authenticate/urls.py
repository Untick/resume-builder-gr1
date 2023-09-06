from django.urls import path
import views as user_auth

app_name = 'authenticate'

urlpatterns = [
     path('login/', user_auth.login, name='login'),
     path('logout/', user_auth.logout, name='logout'),
     path('register/', user_auth.register, name='register'),
     path('edit/', user_auth.edit, name='edit'),
]