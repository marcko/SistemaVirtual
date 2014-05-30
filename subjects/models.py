from django.db import models
from careers.models import Career
from teachers.models import Teacher
from semesters.models import Semester


class Subject(models.Model):
	name_subject = models.CharField(max_length=50)
	career = models.ForeignKey(Career)
	teacher = models.ForeignKey(Teacher)
	semester = models.ForeignKey(Semester)
	Hour = models.TimeField()


	def __str__(self):
		return u"%s" % self.name_subject