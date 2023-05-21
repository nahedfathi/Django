from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='auth.index'),
    path('login/', CustomLoginView.as_view(), name='auth.login'),
    path('register/', RegisterPage.as_view(), name='auth.register'),
    path('logout/', logout, name='auth.logout'),

]
