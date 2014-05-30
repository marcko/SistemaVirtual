from django.db import models
from careers.models import Career
from semesters.models import Semester
#from schedules.models import Schedule
from subjects.models import Subject

class Userstudent(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	age = models.IntegerField()
	career = models.ForeignKey(Career)
	semester = models.ForeignKey(Semester)
	control_number = models.IntegerField(primary_key=True)
	#schedule = models.ForeignKey(Schedule)




	def __unicode__(self):
		return u"%s" % self.control_number