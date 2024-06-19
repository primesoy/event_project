from django.db import models
from django.core.mail import send_mail
import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    """Custom user manager für das CustomUser Model"""

    def send_confirmation_mail(self, user):
        """Sende Bestätigungsmail an an den User."""

        url = f"http://127.0.0.1/api/users/confirm/{user.pk}/{user.email_token}"
        send_mail(
            "Bitte bestätige Deine Email",
            f"Hallo\n\nBitte bestätige deine Email. Bitte klicke auf den Link:\n\n{url}",
            "info@example.com",
            [user.email]
        )


    def create_user(self, email, password=None, **extra_fields):
        """Methode zum Anlegen eines Standard-Users. wird von API aufgerufen"""
        user = self.model(email=email, **extra_fields)
        user.email_token = uuid.uuid1()
        user.set_password(password)
        user.save(using=self._db)
        self.send_confirmation_mail(user)
        return user
    
    def create_superuser(self, email, password=None):
        """Methode zum Anlegen eines Superusers. wird direkt von der Admin aufgerufen."""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True 
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    class Roles(models.TextChoices):
        USER = "User"
        MODERATOR = "Moderator"
        PREMIUM = "Premium"
        ADMIN = "Admin"

    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=100, unique=True, blank=True, null=True) # blank=Formular
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=20, 
                            choices=Roles.choices, 
                            default=Roles.USER, 
                            help_text="Das ist ein Hilfetext")
    
    email_token = models.UUIDField(
        null=True, blank=True, editable=False
    )

    email_confirmed = models.BooleanField(
        default=False, 
        help_text="User has to confirm email"
    )


    objects = CustomUserManager()
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email