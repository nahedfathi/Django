from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='course.index'),
    path('add', add, name='course.add'),
    path('update/<int:id>', update, name='course.update'),
    path('delete/<int:id>', delete, name='course.delete'),

]
