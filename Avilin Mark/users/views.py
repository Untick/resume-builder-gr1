from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Registration
from django.contrib import messages
import requests


def checking_user(login, password):
    API = 'https://lk.neural-university.ru/api/'
    headers = {"Content-Type": "application/json"}
    response = requests.post(API + 'login_check', headers=headers,
                             data='{"username":"' + login + '","password":"' + password + '"}')
    if response.status_code == 200:
        return True
    return False


class RegistrationView(View):
    def get(self, request):
        users = Registration.objects.all()
        return render(request, 'registration.html',
                      {'users': users})

    def post(self, request):
        action = request.POST.get('action')

        if request.method == 'POST':
            if action == 'register':
                fullname = request.POST['fullname']
                email = request.POST['email']
                password = request.POST['password']

                if Registration.objects.filter(email=email).exists():
                    messages.error(request, 'This email is already registered. Please log in.')
                    return redirect('login')

                registration = Registration(fullname=fullname, email=email, password=password)
                registration.save()
                messages.success(request, 'Registration successful. Please log in.')
                return redirect('login')

            elif action == 'update':
                user_id = request.POST['user_id']
                user = get_object_or_404(Registration, pk=user_id)
                user.fullname = request.POST['fullname']
                user.email = request.POST['email']
                user.password = request.POST['password']
                user.save()
                messages.success(request, 'Информация о пользователе успешно обновлена.')
                return redirect('registration')

            elif action == 'delete':
                user_id = request.POST['user_id']
                user = get_object_or_404(Registration, pk=user_id)
                user.delete()
                messages.success(request, 'Пользователь успешно удален.')
                return redirect('registration')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            # Проверка, существует ли пользователь в локальной базе данных
            if Registration.objects.filter(email=email, password=password).exists():
                # Пользователь аутентифицирован в локальной базе данных
                # Теперь проверка с внешним API
                if checking_user(email, password):
                    # Пользователь аутентифицирован с использованием API
                    # Выполнение действия входа, если необходимо
                    messages.success(request, 'Вход выполнен успешно.')
                    return redirect('dashboard') 

            messages.error(request, 'Неверный email или пароль. Пожалуйста, попробуйте снова.')
            return redirect('login')  
