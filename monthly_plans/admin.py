from django.contrib import admin
from .models import MonthlyPlan


@admin.register(MonthlyPlan)
class MonthlyPlanAdmin(admin.ModelAdmin):
    list_display = ('goal_title', 'user', 'month', 'year')
    
