from typing import Optional, TYPE_CHECKING, Any

import uuid
import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

if TYPE_CHECKING:
    from django.contrib.auth.models import User


def recipe_image_file_path(instance: Optional[Any], filename: str) -> str:
    """ Generate file path for new recipe image """
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"

    return os.path.join("uploads/recipe/", filename)


class UserManager(BaseUserManager):

    def create_user(self, email: str, password: Optional[str] = None, **extra_fields) -> "User":
        """Creates and saves a new User"""
        if not email:
            raise ValueError

        user = self.model(email=self.normalize_email(email), **extra_fields)
        # To store the password encrypted
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, password: Optional[str] = None) -> "User":
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'