from django.db import models
from django.conf import settings
import uuid


ROLE_CHOICES = (
    (20, "Admin"),
    (15, "Member"),
    (10, "Viewer"),
    (5, "Guest"),
)


def get_default_props():
    return {
        "filters": {
            "priority": None,
            "state": None,
            "state_group": None,
            "assignees": None,
            "created_by": None,
            "labels": None,
            "start_date": None,
            "target_date": None,
            "subscriber": None,
        },
        "display_filters": {
            "group_by": None,
            "order_by": '-created_at',
            "type": None,
            "sub_issue": True,
            "show_empty_groups": True,
            "layout": "list",
            "calendar_date_range": "",
        },
    }


def get_default_preferences():
    return {"pages": {"block_display": True}}
 

class Project(models.Model):
    NETWORK_CHOICES = ((0, "Secret"), (2, "Public"))
    project_name = models.CharField(max_length=255, verbose_name="Project Name")
    description = models.CharField(max_length = 200, blank=True)
    description_text = models.JSONField(
        verbose_name="Project Description RT", blank=True, null=True
    )
   
    network = models.PositiveSmallIntegerField(default=2, choices=NETWORK_CHOICES)
    workspace = models.ForeignKey(
        "db.WorkSpace", on_delete=models.CASCADE, related_name="workspace_project"
    )
    identifier = models.CharField(
        max_length=12,
        verbose_name="Project Identifier",
    )
    default_assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="default_assignee",
        null=True,
        blank=True,
    )
    project_lead = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="project_lead",
        null=True,
        blank=True,
    )
    emoji = models.CharField(max_length=255, null=True, blank=True)
    icon_prop = models.JSONField(null=True)
    module_view = models.BooleanField(default=True)
    cycle_view = models.BooleanField(default=True)
    issue_views_view = models.BooleanField(default=True)
    page_view = models.BooleanField(default=True)
    inbox_view = models.BooleanField(default=False)
    cover_image = models.ImageField(upload_to="project/", default="", blank=True, null=True, max_length=800)
    default_state = models.ForeignKey(
        "db.State", on_delete=models.SET_NULL, null=True, related_name="default_state"
    )
    default_state = models.ForeignKey(
        "db.State", on_delete=models.SET_NULL, null=True, related_name="default_state"
    )


class BaseModel(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False, db_index=True, primary_key=True
    )

    class Meta:
        abstract = True

        
class ProjectBaseModel(BaseModel):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project_%(class)s"
    )
    workspace = models.ForeignKey(
        "db.Workspace", models.CASCADE, related_name="workspace_%(class)s"
    )



class ProjectMember(ProjectBaseModel):
    member = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="member_project",
    )
    comment = models.TextField(blank=True, null=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=10)

    def save(self, *args, **kwargs):
        if self._state.adding:
            smallest_sort_order = ProjectMember.objects.filter(
                workspace_id=self.project.workspace_id, member=self.member
            ) 
        super(ProjectMember, self).save(*args, **kwargs)
        
class State(ProjectBaseModel):
    name = models.CharField(max_length=255, verbose_name="State Name")
    description = models.TextField(verbose_name="State Description", blank=True)
    color = models.CharField(max_length=255, verbose_name="State Color")
    slug = models.SlugField(max_length=100, blank=True)
    sequence = models.FloatField(default=65535)
    group = models.CharField(
        choices=(
            ("backlog", "Backlog"),
            ("unstarted", "Unstarted"),
            ("started", "Started"),
            ("completed", "Completed"),
            ("cancelled", "Cancelled"),
        ),
        default="backlog",
        max_length=20,
    )
    default = models.BooleanField(default=False)
