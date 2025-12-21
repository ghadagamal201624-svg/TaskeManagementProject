from django.contrib import admin
from .models import TodoList, Task, WeeklyPlan, MonthlyPlan

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')

@admin.register(Task)
class TaskAdmine(admin.ModelAdmin):
    list_display = ('title', 'todo_list', 'priority', 'is_completed', 'due_date')
    list_filter = ('is_completed', 'priority')

@admin.register(WeeklyPlan)
class WeeklyPlanAdmin(admin.ModelAdmin):
    list_display = ('goal_title', 'user', 'week_start_date')

@admin.register(MonthlyPlan)
class MonthlyPlanAdmin(admin.ModelAdmin):
    list_display = ('goal_title', 'user', 'month', 'year')
    
