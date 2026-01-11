from django.db import models
from django.contrib.auth.models import User  # هنستخدم جدول المستخدمين الجاهز

class WeeklyPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weekly_plans')
    goal_title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    week_start_date = models.DateField()
    week_end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Week of {self.week_start_date} - {self.user.username}"
    
