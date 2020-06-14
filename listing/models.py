from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    students_counter = models.IntegerField(default = 0)

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

    def __str__(self):
        return self.name
