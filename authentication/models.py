
# Create your models here.
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin


class UserAccount(AbstractUser):
  email = models.EmailField(null=True, unique=True)
  username = models.CharField(max_length=50, null=True,default="")
  created_at = models.DateTimeField(auto_now_add=True)


  # objects = UserAccountManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']