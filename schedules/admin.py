from django.contrib import admin
from .models import Schedule


class ScheduleAdmin(admin.ModelAdmin):
	list_display = ('id_schedule','control_number','subject','semester','career')
	search_fields= ('id_schedule','control_number__control_number','control_number__first_name','control_number__last_name')

admin.site.register(Schedule, ScheduleAdmin)
