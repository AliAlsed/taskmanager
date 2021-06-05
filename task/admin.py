import task
from django.contrib import admin
from .models import Task, Profile, News
# Register your models here.
admin.site.register(Task)
admin.site.register(Profile)
admin.site.register(News)
