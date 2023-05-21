from django.db import models
from authMain.models import AuthMain
from course.models import Course
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    course=models.ForeignKey(Course ,on_delete=models.CASCADE,related_name='user_course')
    
    def __str__(self) -> str:
        return self.user.username