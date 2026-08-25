from django.urls import path
from .views import *
urlpatterns = [
   # path('route/',function_name_from_view)
   path('home/',home),
   path('aboutus/',aboutus),
   path('task/',tasks),
   path('task/create/', create_task),
   path('task/<id>/edit/',task_details),
   path('task/<id>/status/',edit_status),
]
