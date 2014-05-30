from django.db import models
from careers.models import Career

class Semester(models.Model):
	id_semester = models.CharField(max_length=20,primary_key=True)
	career = models.ForeignKey(Career)

	def __str__(self):
		return u"%s" % self.id_semester
