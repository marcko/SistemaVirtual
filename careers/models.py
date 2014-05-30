from django.db import models

class Career(models.Model):
	id_career = models.IntegerField(primary_key=True)
	career_name = models.CharField(max_length=50)

	def __str__(self):
		return u"%s" % self.career_name