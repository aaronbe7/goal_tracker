from django.contrib import admin
from .models import GoalList, Goal

# Register your models here.
admin.site.register(GoalList)
admin.site.register(Goal)