from django.db import models

# Create your models here.
# Todolist: task(string), status(boolean), priority(int)

class Todolist(models.Model):
   title = models.CharField(max_length=100)
   status = models.BooleanField(default=False)
   
   def __str__(self):
      return f"{self.title}- {self.status}"


# models -> migration file -> database changes

# migration file -> python manage.py makemigrations
# migrate to database/database changes -> python manage.py migrate

# git initializer
# github repo
# add gitignore file
# push into github