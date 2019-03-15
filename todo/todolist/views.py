from django.shortcuts import render,HttpResponse,redirect,get_list_or_404
from todolist.forms import taskList
from . import forms
from todolist.models import post
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
# from django.contrib.auth.models import User

# Create your views here.

# def index(request): 
#     show_post = post.objects.all().filter()[:10]
#     form = taskList(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = taskList()    
    
#     context ={
#         'form':form,    
#         'post':show_post, 

# }
# return render(request,'todo/index.html',context)


def index(request): 
    show_post = post.objects.all().filter()[:30]
    form = taskList(request.POST or None)   
    context ={
        'form':form,    
        'post':show_post, 
        'title':'Home',
    }
    if request.method == "POST":
        task = request.POST['task']
        p = post(task = task)
        p.save()
    return render(request,'todo/index.html',context)

@login_required(login_url="/login/")
def todo(request): 
    author=request.user
    show_post = post.objects.all().filter(author=author)[:10]
    form = taskList(request.POST or None)   
    context ={
        'form':form,    
        'post':show_post, 
         'title':'Todo',
    }
    if request.method == "POST":
        task = request.POST['task']
        p = post(task = task,author=request.user)
        # print(p.task)
        # print(p.author)
        p.save()
    return render(request,'todo/todo.html',context)

def delete(request, id):
    del_post = post.objects.get(pk=id)
    del_post.delete()   
    return redirect('/todo/')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/')
    else:
        form = AuthenticationForm()

    context = {
        'form':form,
        'title':'Login',
        }
    return render(request,'todo/login.html',context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            #login(request,user)
            #return redirect('/login')
            return redirect('/login')
    else:
        form = UserCreationForm()
    
    context = {
        'form':form,
        'title':'Signup',
        }
    return render(request,'todo/signup.html',context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
