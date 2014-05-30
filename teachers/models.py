from django.db import models

class Teacher(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	age = models.IntegerField()
	speciality = models.CharField(max_length=50)
	id_teacher = models.IntegerField(primary_key=50)


	def __str__(self):
		return u"%s" % self.first_name
