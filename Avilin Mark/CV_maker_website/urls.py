from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', views.index, name='home'),
    path('order/', include('do_order.urls')),
    path('auth/', include('users.urls'))
]
