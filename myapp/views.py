from django.shortcuts import render,HttpResponse
from .models import TodoItem
#create your views here.

def home(request):
    return render(request,"home.html")

def task_list(request):
    items = TodoItem.objects.all()
    return render(request, "task_list.html",{"todos":items}) 