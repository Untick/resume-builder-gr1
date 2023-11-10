from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib import messages
import requests
from .models import Registration


def checking_user(email, password):
    API = 'https://lk.neural-university.ru/api/'
    headers = {"Content-Type": "application/json"}
    response = requests.post(API + 'login_check', headers=headers,
                             data='{"username":"' + email + '","password":"' + password + '"}')
    if response.status_code == 200:
        return True
    return False


def register(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the email and password are valid using checking_user function
        if not checking_user(email, password):
            messages.error(request,
                           "Используйте ту же информацию для входа в УИИ для регистрации на этом сайте. "
                           "Если нет, убедитесь в правильности данных для регистрации в УИИ.")
            return redirect('register')  # Redirect back to registration page

        # Create a new Registration object
        registration = Registration(fullname=fullname, email=email, password=password)
        registration.save()

        messages.success(request, "Регистрация прошла успешно! Теперь вы можете войти.")
        return redirect('login')  # Redirect to login page after successful registration

    return render(request, 'registration_form.html')


def user_login(self, request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Проверка, существует ли пользователь в локальной базе данных
        user = Registration.objects.filter(email=email, password=password).first()

        if user:
            # Получаем user_id пользователя
            user_id = user.id

            # Теперь проверка с внешним API
            if checking_user(email, password):
                # Пользователь аутентифицирован с использованием API
                # Переход на dashboard с передачей user_id
                login(request, user)
                return redirect('dashboard', user_id=user_id)

        messages.error(request, 'Неверный email или пароль. Пожалуйста, попробуйте снова.')
        return redirect('login')


def user_logout(request):
    logout(request)
    return redirect('login')


# Home page
def index(request):
    return render(request, 'index.html')
