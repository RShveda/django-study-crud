from django.shortcuts import render
from django.views.generic import ListView
from listing.models import School, Student
# Create your views here.

class SchoolList(ListView):
    model = School
    template_name="listing/schools.html"
