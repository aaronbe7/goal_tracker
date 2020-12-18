from django.contrib import admin
from .models import GoalList, Goal, Photo

# Register your models here.
admin.site.register(GoalList)
admin.site.register(Goal)
admin.site.register(Photo)

