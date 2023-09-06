from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', include('do_order.urls')),
    path('order/', include('users.urls'))
]
