from django.db import models
from userstudents.models import Userstudent
from subjects.models import Subject
from semesters.models import Semester
from careers.models import Career



class Schedule(models.Model):
	id_schedule = models.IntegerField(primary_key=True)
	control_number = models.ForeignKey(Userstudent)
	subject = models.ForeignKey(Subject)
	semester = models.ForeignKey(Semester)
	career = models.ForeignKey(Career)

	def __str__(self):
		 return u"%s" % self.id_schedule
		