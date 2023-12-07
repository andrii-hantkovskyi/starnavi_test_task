from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have an email")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        unique=True, max_length=255, verbose_name='E-Mail')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_request = models.DateTimeField(verbose_name='Last request', null=True, blank=True)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return str(self.email)
