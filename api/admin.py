from django.contrib import admin
from .models import Application, University, Student, SponsorShip


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'fio', 'phone_num', 'entity_type', 'donate_amount']
    list_filter = ['status', 'updated', 'donate_amount']
    ordering = ['updated', 'fio']


@admin.register(Student)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'fio', 'phone_num', 'otm', 'type', 'cont_amount']
    list_filter = ['cont_amount', 'type', 'otm']
    ordering = ['cont_amount', 'otm']


admin.site.register(University)
admin.site.register(SponsorShip)
