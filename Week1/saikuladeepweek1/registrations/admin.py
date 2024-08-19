# users/admin.py
from django.contrib import admin
from .models import Teacher,Student

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('get_first_name', 'get_last_name', 'emp_id')
    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last Name'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'get_email')

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'