from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import AbstractBaseUser  # BASE withouth many functions
# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def __create_user(self, email: str, password: str, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user: CustomUser = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password: str = None, **extra_fields):
        # extra_fields.setdefault('is_staff', True)  # default is False
        extra_fields.setdefault('is_superuser', False)
        return self.__create_user(email, password, **extra_fields)

    def create_superuser(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser', False) is False:
            raise ValueError("superuser needs 'is_superuser=True'")

        if extra_fields.get('is_staff', False) is False:
            raise ValueError("superuser needs 'is_staff=True'")

        return self.__create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField('e-mail', unique=True)
    phone = models.CharField('Telefone', max_length=15)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email'  # qual campo será usado para login
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def __str__(self):
        return self.email

    objects = UserManager()  # who manage this user model
