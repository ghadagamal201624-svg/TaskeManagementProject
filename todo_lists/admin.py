from django.contrib import admin
from .models import TodoLists

@admin.register(TodoLists)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')

