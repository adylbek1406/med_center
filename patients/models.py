from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='patients/', null=True, blank=True)
    birth_date = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True, blank=True, null=True)

    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions_set", blank=True)

    def __str__(self):
        return self.username
