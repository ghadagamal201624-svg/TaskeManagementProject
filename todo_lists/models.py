from django.db import models
from django.contrib.auth.models import User  # هنستخدم جدول المستخدمين الجاهز

class TodoLists(models.Model):
    # ربط القائمة بالمستخدم (One-to-Many)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_lists')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
