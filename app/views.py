"""
Definition of views.
"""
from django.shortcuts import render
from .models import Comment    # использование модели комментариев 
from .forms import CommentForm   # использование формы ввода комментария
from django.db import models 
from .models import Blog
from .forms import BlogForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':' ',
            'message':' ',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':' ',
            'message':' ',
            'year':datetime.now().year,
        }
    )

def tort1(request):
    
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tort1.html',
        {
            'title':'Детективы',
            'message':'Сведения о нас.',
            'year':datetime.now().year,
        }
    )

def tort2(request):
   
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tort2.html',
        {
            'title':'Фэнтези',
            'message':'Сведения о нас.',
            'year':datetime.now().year,
        }
    )

def tort3(request):

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tort3.html',
        {
            'title':'Исторические',
            'message':'Сведения о нас.',
            'year':datetime.now().year,
        }
    )

def tort4(request):

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tort4.html',
        {
            'title':'Детские',
            'message':'Сведения о нас.',
            'year':datetime.now().year,
        }
    )


def registration(request):
 """Renders the registration page."""
 
 if request.method == "POST": 
    regform = UserCreationForm (request.POST)
    if regform.is_valid(): 
        reg_f = regform.save(commit=False) 
        reg_f.is_staff = False 
        reg_f.is_active = True 
        reg_f.is_superuser = False 
        reg_f.date_joined = datetime.now()
        reg_f.last_login = datetime.now() 

        reg_f.save() 

        return redirect('home') 
 else:
     regform = UserCreationForm() 

 assert isinstance(request, HttpRequest)
 return render(
    request,
    'app/registration.html',
     {

        'regform': regform,

        'year':datetime.now().year,
    }
 )

def blog(request):
    """Renders the blog page."""
    posts = Blog.objects.order_by('-posted') # запрос на выбор всех статей
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        { 
            'title':'Блог',
            'posts': posts, # передача списка статей в шаблон веб-страницы
            'year':datetime.now().year,
        }
    )

def blogpost(request, parametr):
    """Renders the blogpost page."""
    post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной
    comments = Comment.objects.filter(post=parametr)

    if request.method == "POST": # после отправки данных формы на сервер методом POST
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя
            comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату
            comment_f.post = Blog.objects.get(id=parametr) # добавляем в модель Комментария (Comment) статью, для которой данный комментарий
            comment_f.save() # сохраняем изменения после добавления полей

            return redirect('blogpost', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки комментария
    else:
        form = CommentForm() # создание формы для ввода комментария
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1, 
            'comments': comments, # передача всех комментариев к данной статье в шаблон веб-страницы
            'form': form, # передача формы в шаблон веб-страницы 
            'year':datetime.now().year,
        }
    )

def newpost(request):
    """Renders the newpost page."""

    if request.method == "POST": 
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()

            blog_f.save() # сохраняем изменения после добавления полей

            return redirect('blog') 
    else:
        blogform = BlogForm() # создание формы для ввода комментария

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/newpost.html',
        {
 
            'blogform': blogform, # передача формы в шаблон веб-страницы 

            'year':datetime.now().year,
        }
    )