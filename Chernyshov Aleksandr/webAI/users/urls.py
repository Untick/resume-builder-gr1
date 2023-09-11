from django.urls import path
from .views import RegistrationView, LoginView

urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("login/", LoginView.as_view(), name="login"),
    path("update/<int:user_id>/", RegistrationView.as_view(), name="update_user"),
    path("delete/<int:user_id>/", RegistrationView.as_view(), name="delete_user"),
]
