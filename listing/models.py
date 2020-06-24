from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    students_counter = models.IntegerField(default = 0)

    def get_absolute_url(self):
        return reverse('listing:school', kwargs={'school': self.name})

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=40)
    school = models.ForeignKey(School, on_delete = models.CASCADE)

    def save(self, *args, **kwargs):
        ## increment students counter for this particular school
        a = self.school
        a.students_counter = len(Student.objects.filter(school = a)) + 1
        a.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        ## increment students counter for this particular school
        a = self.school
        a.students_counter = len(Student.objects.filter(school = a)) - 1
        a.save()
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('listing:student', kwargs={"school": self.school.name, "student": self.pk})

    def __str__(self):
        return self.name
