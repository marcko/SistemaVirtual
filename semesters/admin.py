from django.contrib import admin
from .models import Semester


class SemesterAdmin(admin.ModelAdmin):
	list_display = ('id_semester','career')
	search_fields = ('id_semester','career__career_name')
admin.site.register(Semester,SemesterAdmin)
