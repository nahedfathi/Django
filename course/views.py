from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Course
# Create your views here.




def index(req):
    courses=Course.objects.all()
    return render(req, "course/index.html", {"courses": courses})


def add(req):
    if req.method=='GET':
        return render(req, "course/add-course.html", {"test": "abc"})

    if req.POST['name'] and req.POST['duration']:
        name = req.POST['name']
        duration=req.POST['duration']
        Course.objects.create(name=name,duration=duration)
        return HttpResponseRedirect("/course")
    return render(req, "course/add-course.html", {"err": "All inputs are required"})

def update(req, id):
    course = Course.objects.get(id=id)
    # print(course.name)
    if req.method=='GET':
        return render(req, "course/update-course.html", {"course": course})
    
    if req.POST['name'] and req.POST['duration']:
        name = req.POST['name']
        duration = req.POST['duration']
        course.duration=duration
        course.name=name
        # print(course.duration)
        course.save()
        # print(course.duration)
        return HttpResponseRedirect("/course")
    return render(req, "course/update-course.html", {"err": "All inputs are required"})

def delete(req, id):
    course = Course.objects.get(id=id)
    course.delete()
    return HttpResponseRedirect("/course")
