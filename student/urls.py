from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='student.index'),
    path('add', add, name='student.add'),
    path('update/<int:id>', update, name='student.update'),
    path('delete/<int:id>', delete, name='student.delete'),
  
]
