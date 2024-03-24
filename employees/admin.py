from django.contrib import admin

from employees.models import *


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'rank', 'chief', 'created_at', 'changed_at']
