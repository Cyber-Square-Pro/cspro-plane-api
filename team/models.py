
from django.db import models

class ProjectTeam(models.Model):
    TEAM_STATUS_CHOICES = [
        ('active', 'Active'),
        ('disabled', 'Disabled'),
    ]

    team_name = models.CharField(max_length=255, blank=False, null=False)
    team_description = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=8, choices=TEAM_STATUS_CHOICES, default='active')

    def _str_(self):
        return self.team_name
    
class Member(models.Model):
    member_name = models.CharField(max_length=255, blank=False, null=False)
    role = models.CharField(max_length=255, blank=False, null=False)
    team = models.ForeignKey(ProjectTeam, on_delete=models.CASCADE, related_name='members')

    def _str_(self):
        return self.member_name
    







class Attendance(models.Model):
    ATTENDANCE_TYPE_CHOICES = [
        ('scrum', 'Scrum'),
        ('sprint_review', 'Sprint_Review'),
        ('sprint_grooming', 'Sprint_Grooming'),
    ]

    ATTENDANCE_STATUS_CHOICES = [
        ('present', 'Present'),
        ('reportedleave', 'Reportedleave'),
           ('absent', 'Absent'),
    ]

    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    type = models.CharField(max_length=50, choices=ATTENDANCE_TYPE_CHOICES)
    status = models.CharField(max_length=50, choices=ATTENDANCE_STATUS_CHOICES)
    last_updated_date = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255)
    reason = models.TextField(blank=True, null=True)

    def _str_(self):
        return f"{self.member}-{self.date}"
    
