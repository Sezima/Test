from django import forms
from django.contrib import admin

# Register your models here.
from .models import *


class GradeInline(admin.TabularInline):
    model = Grade
    raw_id_fields = ['students']


class GradeAdmin(admin.ModelAdmin):
    list_display = ['teachers', 'name']
    inlines = [GradeInline]


class SchoolGradeInline(admin.TabularInline):
    model = SchoolGrade
    raw_id_fields = ['grade']


class TeachAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [SchoolGradeInline]


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(School, TeachAdmin)
admin.site.register(Teach, GradeAdmin)
