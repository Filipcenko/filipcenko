from django.contrib.auth.models import AbstractUser
from django.db import models
from task_manager_system import settings


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('employee', 'Employee'),
        ('client', 'Client'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='client')
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True, default='')

    # Добавляем related_name для полей groups и user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # изменяем related_name
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # изменяем related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

class Task(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Ожидает исполнителя'),
        ('in_progress', 'В процессе'),
        ('completed', 'Выполнена'),
    )
    client = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks_created', on_delete=models.CASCADE, limit_choices_to={'user_type': 'client'})
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks_assigned', on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'user_type': 'employee'})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    report = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def save(self, *args, **kwargs):
        if self.status == 'completed' and not self.report:
            raise ValueError("Report is required when closing the task.")
        super().save(*args, **kwargs)
