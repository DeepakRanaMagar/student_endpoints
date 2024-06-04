from django.db import models
from django.utils.translation import gettext_lazy as _ 

# Create your models here.
grades = {
    "Distinction" : "A+",
    "Division I" : "A",
    "Division II" : "B",
    "Division III" : "C",
    "Fail" : "F"
}

GRADE_CHOICES = [(key, value) for key, value in grades.items()]

class Student(models.Model):
    '''
        Handles db schema for Student Model
    '''
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    name = models.CharField(_("Name"), max_length=50)
    age = models.IntegerField(_("Age"))
    address = models.CharField(_("Address"), max_length=50)
    grade = models.TextField(_("Grade"), choices=grades)
    major = models.CharField(_("Major"), max_length=50)

    def __str__(self):
        return self.name