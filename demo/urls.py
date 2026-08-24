from django.urls import path
from .views import *
urlpatterns = [
   # path('route/',function_name_from_view)
   path('home/',home),
   path('aboutus/',aboutus),
   path('task/',tasks),
   path('task/<id>/',task_details)
]
