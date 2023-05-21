from django.shortcuts import render,HttpResponseRedirect
from .models import AuthMain

from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView ,FormView


from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



# Create your views here.
def index(req):
    return render(req, "base.html", {"test": "abc"})

class CustomLoginView(LoginView):
    template_name = "authMain/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('course.index')
    
class RegisterPage(FormView):
    template_name='authMain/register.html'  
    form_class=UserCreationForm  
    redirect_authenticated_user = True
    success_url = reverse_lazy('course.index')
    
    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect("course.index")
        return super(RegisterPage, self).get(*args, **kwargs)

def logout(req):
    req.session.clear()
    return HttpResponseRedirect("/")
