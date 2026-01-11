from django.contrib import admin
from .models import WeeklyPlan

@admin.register(WeeklyPlan)
class WeeklyPlanAdmin(admin.ModelAdmin):
    list_display = ('goal_title', 'user', 'week_start_date')

