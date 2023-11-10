from django.contrib import admin
from .models import Registration


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'created_time')
    search_fields = ('fullname', 'email')
    ordering = ('-created_time',)


# Register the Registration model with the custom admin class
admin.site.register(Registration, RegistrationAdmin)
