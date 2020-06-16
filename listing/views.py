from django.shortcuts import render
from django.views.generic import ListView, DetailView
from listing.models import School, Student
from django.shortcuts import get_object_or_404
# Create your views here.

class SchoolList(ListView):
    model = School
    template_name="listing/schools.html"

class SchoolStudentList(ListView):
    template_name="listing/students.html"

    def get_queryset(self):
        self.school = get_object_or_404(School, name = self.kwargs['school'])
        return Student.objects.filter(school = self.school)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school'] = self.school
        return context

class StudentDetailView(DetailView):
    model = Student
    template_name="listing/student.html"
    pk_url_kwarg = "student"
