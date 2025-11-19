from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    role = models.CharField(max_length=30,
                            choices=(('admin', 'Admin'),
                                     ('student', 'Student'),
                                     ('instructor', 'Instructor'),
                                     ),
                            default='student'
                            )

    def __str__(self):
        return self.username