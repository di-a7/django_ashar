from django.shortcuts import render, redirect
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

# {"title":"enter_data"}

def tasks(request):
   
   task = Todolist.objects.all()
   context = {'tasks':task}
   return render(request, 'task.html', context)

def task_details(request,id):
   task = Todolist.objects.get(id=id)
   context = {'task':task}
   if request.method == 'POST':
      title = request.POST.get('title')
      task.title = title
      task.save()
      return redirect('/task/')
   return render(request,'get.html',context)

def edit_status(request, id):
   task = Todolist.objects.get(id=id)
   task.status = True
   task.save()
   return redirect('/task/')

def create_task(request):
   if request.method == 'POST':
      title = request.POST.get('title')
      Todolist.objects.create(title=title)
      return redirect('/task/')
   return render(request,'create.html')

# delete function, url and change the href in task.html with the url