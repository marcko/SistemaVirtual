from django.contrib import admin
from .models import Subject

class SubjectAdmin(admin.ModelAdmin):
	list_display = ('name_subject','career','teacher','semester','Hour')
	search_fields = ('name_subject','teacher__id_teacher','semester__id_semester','Hour')

admin.site.register(Subject,SubjectAdmin)