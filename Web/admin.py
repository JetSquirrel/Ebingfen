from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(college)
admin.site.register(active)
admin.site.register(tinker)
admin.site.register(banner)


# def add_college():
#
#
# class ArticleAdmin(admin.ModelAdmin):
#      list_display = ['title', 'status']
#      ordering = ['title']
#      actions = [make_published]