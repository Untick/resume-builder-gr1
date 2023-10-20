from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from app_promt.models import Post
from app_promt.forms import PostForm
from django.urls import reverse
#from .models import Post

# Create your views here.

menu = ["Главная страница", "Анкета", "Вход", "litter"]
def test_view(request: WSGIRequest) -> HttpResponse:
    return HttpResponse('Страница приложения appweb')

def index(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/index.html', {'menu': menu, 'title': 'Главная страница'})

def cv_view(request: WSGIRequest) -> HttpResponse:
    #posts = Post.objects.all()
    return render(request, 'appweb/cv.html', {'menu': menu, 'title': 'Анкета'})

def dashboard_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/dashboard.html', {'menu': menu, 'title': 'dashboard'})

def edit_cv_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/edit_cv.html', {'menu': menu, 'title': 'edit_cv'})

def edit_cv_order_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/edit_cv_order.html', {'menu': menu, 'title': 'edit_cv_order'})

def edit_litter_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/edit_litter.html', {'menu': menu, 'title': 'edit_litter'})

def edit_litter_order_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/edit_litter_order.html', {'menu': menu, 'title': 'edit_litter_order'})

def litter_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/litter.html', {'menu': menu, 'title': 'litter'})

def login_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/login.html', {'menu': menu, 'title': 'Вход'})

def registration_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'appweb/registration.html', {'menu': menu, 'title': 'Регистрация'})

def promt_view(request):

    posts = Post.objects.all()
    return render(request, 'appweb/promt.html', context = {"posts": posts})

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'appweb/post.html', context = {"post": post})

def create_post(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, 'appweb/create_post.html', context = {'form': form})
    else:
        form = PostForm(request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("appweb:promt")) # После сохранения отправляем пользователя на главную страницу
        else:
            return render(request, 'appweb/create_post.html', context = {'form': form})
    return render(request, 'appweb/create_post.html')