from django import forms
from .models import *
from course.models import Course
class StudentAddForm(forms.Form):
    name=forms.CharField(required=True,max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    course=forms.ChoiceField(
        required=True,
        choices=[(course.id,course.name) for course in Course.objects.all()],
        widget=forms.Select(attrs={ 'class': 'form-control'}))
    
    def save(self):
        name = self.cleaned_data['name']
        course = self.cleaned_data['course']
        mymodel = Student(name=name, course=Course.objects.get(id=course))
        mymodel.save()
    
class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'course': forms.Select(attrs={
                'class': "form-control", 
                })
        }
