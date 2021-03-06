from django.contrib import admin
from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','age','speciality','id_teacher')
	search_fields = ('first_name','last_name','age','speciality','id_teacher')
admin.site.register(Teacher,TeacherAdmin)
