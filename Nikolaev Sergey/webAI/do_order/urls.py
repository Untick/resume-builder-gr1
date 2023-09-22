from django.urls import path
from .views import OrderCVCreateView, OrderCVUpdateView

urlpatterns = [
    path("cv-order/", OrderCVCreateView.as_view(), name="order_cv_create"),
    path(
        "update-cv-order/<int:pk>/", OrderCVUpdateView.as_view(), name="order_cv_update"
    ),
    path("cl-order/", OrderCVCreateView.as_view(), name="order_cl_create"),
    path(
        "update-cl-order/<int:pk>/", OrderCVUpdateView.as_view(), name="order_cl_update"
    ),
]
