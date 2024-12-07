from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'profile for user: {self.user.first_name}-{self.user.last_name}'