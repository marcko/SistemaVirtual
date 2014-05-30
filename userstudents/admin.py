from django.contrib import admin
from .models import Userstudent
from subjects.models import Subject


class UserstudentAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','age','career','semester','control_number',)
	search_fields = ('control_number','first_name','last_name',)


admin.site.register(Userstudent, UserstudentAdmin)
