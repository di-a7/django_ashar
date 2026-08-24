from django.contrib import admin
from .models import Todolist
# Register your models here.


@admin.register(Todolist)
class TodolistAdmin(admin.ModelAdmin):
   list_display = ['id','title','status']
   search_fields = ['title']
   list_filter = ['status']

# admin.site.register(Todolist, TodolistAdmin)
