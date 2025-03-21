from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Position(models.Model):
    class ITPositions(models.TextChoices):
        DEVELOPER = "Developer"
        QA_ENGINEER = "QA Engineer"
        SYSTEM_ADMIN = "System Admin"
        DEVOPS_ENGINEER = "DevOps Engineer"
        DATA_SCIENTIST = "Data Scientist"
        UX_DESIGNER = "UX Designer"

    name = models.CharField(
        max_length=50,
        choices=ITPositions.choices,
        default=ITPositions.DEVELOPER,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.get_name_display()}"


class TaskType(models.Model):
    class TaskTypes(models.TextChoices):
        BUG = "Bug"
        NEW_FEATURE = "New Feature"
        REFACTORING = "Refactoring"
        QA = "QA"
        BREAKING_CHANGE = "Breaking Change"

    name = models.CharField(
        max_length=50,
        choices=TaskTypes.choices,
        default=TaskTypes.BUG,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.get_name_display()}"


class Worker(AbstractUser):
    position = models.ForeignKey(Position,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("planer:worker-detail", kwargs={"pk": self.pk})


class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = "Low"
        MEDIUM = "Medium"
        HIGH = "High"

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=20,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker, blank=True)

    def __str__(self):
        return self.name


