from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Position, TaskType, Worker, Task


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ["name"]


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ["name"]


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("position",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "position",
                )
            },
        ),
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "priority", "deadline", "is_complete", "task_type")
    list_filter = ("priority", "task_type", "is_complete")
    search_fields = ("name", "description")
