"""django_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from listing.views import SchoolList, SchoolStudentList, StudentDetailView, StudentCreateView, StudentUpdateView, SchoolCreateView, StudentDeleteView, SchoolUpdateView, SchoolDeleteView

app_name = "listing"

urlpatterns = [
    path('schools', SchoolList.as_view(), name = "schools"),
    path('schools/<school>/', SchoolStudentList.as_view(), name = "school"),
    path('schools/school_form', SchoolCreateView.as_view(), name = "create_school"),
    path('schools/<school>/school_update_form', SchoolUpdateView.as_view(), name = "update_school"),
    path('schools/<school>/school_confirm_delete', SchoolDeleteView.as_view(), name = "delete_school"),
    path('schools/<school>/student_form', StudentCreateView.as_view(), name = "create_student"),
    path('schools/<school>/<student>/student_update_form', StudentUpdateView.as_view(), name = "update_student"),
    path('schools/<school>/<student>/student_confirm_delete', StudentDeleteView.as_view(), name = "delete_student"),
    path('schools/<school>/<student>', StudentDetailView.as_view(), name = "student"),
]
