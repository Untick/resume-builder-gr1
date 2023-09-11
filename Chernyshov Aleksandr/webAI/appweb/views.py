from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def main_view(request: WSGIRequest) -> HttpResponse:
    return HttpResponse('Страница приложения')

def index(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/index.html')

def cv_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/cv.html}')

def dashboard_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/dashboard.html')

def edit_cv_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/edit_cv.html')

def edit_cv_order_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/edit_cv_order.html')

def edit_liter_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/edit_liter.html')

def edit_liter_order_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/edit_liter_order.html')

def liter_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/liter.html')

def login_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/login.html')

def registration_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/registration.html')