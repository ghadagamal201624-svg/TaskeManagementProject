from django.db import models
from django.contrib.auth.models import User  # هنستخدم جدول المستخدمين الجاهز

class TodoList(models.Model):
    # ربط القائمة بالمستخدم (One-to-Many)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_lists')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    # ربط المهمة بقائمة معينة (زي الرسمة)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='tasks')
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # مطلوب في المشروع
    due_date = models.DateField(null=True, blank=True)
    
    # مطلوب في المشروع (Priority)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    
    # الحالة (Status)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)  # عشان نعرف خلصت امتى

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
