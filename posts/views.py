from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import PostForm
# Create your views here.
def create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Successfully Created")
        return HttpResponseRedirect(reverse('list'))
    else:
        messages.error(request,"Not Successfully Created")
    context = {
        "form" : form,
    }
    return render(request, 'posts/post_form.html',context)

def detail(request,pk):
    id = pk
    instance = Post.objects.get(id=id)
    context = {
        "instance_id" : id,
        "instance" : instance,
    }
    return render(request, 'posts/post_detail.html',context)

def list(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'posts/home.html',context)

def update(request, pk):
    id = pk
    instance = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Successfully Updated")
        return HttpResponseRedirect(reverse('list'))

    else:
        messages.error(request,"Not Successfully Updated")
    context = {
        "instance_id" : id,
        "instance" : instance,
        "form" : form,
    }

    return render(request, 'posts/post_form.html',context)

def delete(request, pk):
    id = pk
    instance = Post.objects.get(id=id)
    instance.delete()
    messages.success(request,"Successfully Deleted")
    return HttpResponseRedirect(reverse('list'))
