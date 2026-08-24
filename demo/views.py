from django.shortcuts import render
from django.http import HttpResponse
from .models import Todolist
# Create your views here.

def home(request):
   people = [
      {"name":"Ram","age":20,"contact":"9+874856321"},
      {"name":"SHyam","age":20,"contact":"9+874856321"},
      {"name":"Hari","age":20,"contact":"9+874856321"},
      {"name":"Sita","age":20,"contact":"9+874856321"},
      {"name":"abc","age":20,"contact":"9+874856321"}
   ]
   context = {"title":"HOme page",
      "heading":"skjdbvknlgjfdsfgbn",
      "people":people,
   }
   return render(request, 'home.html', context)

# create aboutus, contactus function, urls
def aboutus(request):
   context = {
      "title":"ABout Us",
      "heading":"ABOUT US PAGE"
   }
   return render(request, 'aboutus.html', context)

def tasks(request):
   task = Todolist.objects.all()
   context = {
      'tasks':task
   }
   return render(request, 'task.html', context)

def task_details(request,id):
   task = Todolist.objects.get(id=id)
   print(task.title)
   context = {
      'task':task
   }
   return render(request,'get.html',context)