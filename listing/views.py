from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from listing.models import School, Student
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

# Create your views here.

class SchoolList(ListView):
    model = School
    template_name="listing/schools.html"

class StudentList(ListView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schools'] = School.objects.all()
        return context

class SchoolStudentList(ListView):
    template_name="listing/students.html"

    def get_queryset(self):
        self.school_name = get_object_or_404(School, name = self.kwargs['school'])
        return self.school_name.students.all()
        # return Student.objects.filter(school = self.school_name)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school_name'] = self.school_name
        return context

class StudentDetailView(DetailView):
    model = Student
    fields = ["name", "school"]
    template_name = "listing/student.html"
    pk_url_kwarg = "student"

class StudentCreateView(CreateView):
    model = Student
    fields = ["name"]

    def form_valid(self, form):
        form.instance.school = get_object_or_404(School, name = self.kwargs['school'])
        return super().form_valid(form)

class StudentUpdateView(UpdateView):
    model = Student
    fields = ["name", "school"]
    template_name_suffix = '_update_form'
    pk_url_kwarg = "student"

class StudentDeleteView(DeleteView):
    model = Student
    pk_url_kwarg = "student"
    def get_success_url(self, **kwargs):
        return reverse_lazy("listing:school", kwargs={"school":self.object.school})

class SchoolCreateView(CreateView):
    model = School
    fields = ["name", "location"]

class SchoolUpdateView(UpdateView):
    model = School
    template_name_suffix = '_update_form'
    fields = ["name", "location"]

    def get_object(self):
        school_name = self.kwargs["school"]
        return School.objects.get(name = school_name)

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("listing:schools")

    def get_object(self):
        school_name = self.kwargs["school"]
        return School.objects.get(name = school_name)
