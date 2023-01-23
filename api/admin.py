from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'fio', 'phone_num', 'entity_type', 'donate_amount']
    list_filter = ['status', 'updated', 'donate_amount']
    ordering = ['updated', 'fio']
