from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
#from .models import Post
from .forms import PostForm

from django.urls import reverse
# Create your views here.
def test_view(request: WSGIRequest) -> HttpResponse:
    return HttpResponse('Страница приложения appweb')

def index(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/index.html')

def cv_view(request: WSGIRequest) -> HttpResponse:
    #posts = Post.objects.all()
    return render(request, 'appweb/cv.html')

def dashboard_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/dashboard.html')

def edit_cv_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/edit_cv.html')

def edit_cv_order_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/edit_cv_order.html')

def edit_litter_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/edit_litter.html')

def edit_litter_order_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/edit_litter_order.html')

def litter_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/litter.html')

def login_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/login.html')

def registration_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/registration.html')

