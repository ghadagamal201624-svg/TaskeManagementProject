from django.db import models
from django.contrib.auth.models import User  # هنستخدم جدول المستخدمين الجاهز

class MonthlyPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='monthly_plans')
    month = models.PositiveSmallIntegerField()  # رقم الشهر من 1 لـ 12
    year = models.PositiveIntegerField()
    goal_title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.month}/{self.year} - {self.user.username}"
    
