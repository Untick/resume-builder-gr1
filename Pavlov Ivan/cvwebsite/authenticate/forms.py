from django import forms
from django.contrib.auth.forms import (AuthenticationForm,
                                       UserCreationForm,
                                       UserChangeForm)
from models import WebsiteUser


class WebsiteUserLogin(AuthenticationForm):
    class Meta:
        model = WebsiteUser
        fields = ('username',
                  'password')

    def __init__(self, *args, **kwargs):
        super(WebsiteUserLogin, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class WebsiteUserRegistration(UserCreationForm):
    class Meta:
        model = WebsiteUser
        fields = (
            'username',
            # 'password', Включить по необходимости
            # 'email',
        )

    def __init__(self, *args, **kwargs):
        super(WebsiteUserRegistration, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def save_user(self):
        user = super(WebsiteUserRegistration, self).save()
        user.is_active = True
        user.save()
        return user


class WebsiteUserEdit(UserChangeForm):
    class Meta:
        model = WebsiteUser
        fields = ()

    def __init__(self, *args, **kwargs):
        super(WebsiteUserEdit, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'password':
                field.widget = forms.HiddenInput()