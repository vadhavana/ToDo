from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from . models import post
from . forms import inputForm
from django.views.generic import ListView

def index(request):
    all_post = post.objects.all()
    inputform = inputForm(request.POST or None) 
    context ={
        'form':inputform,
        'list':all_post,
    }
    if request.method == "POST":
        print(request.POST.get('List'))
        List = request.POST['List']
        p = post(l=List)
        p.save()

        all_post.objects.filter('id').delete

    return render(request,'todo/index.html',context)

