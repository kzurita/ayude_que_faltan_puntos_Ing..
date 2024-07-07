from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.utils import timezone


class MyUserManager(BaseUserManager):
  def create_user(self, email, password=None, **extra_fields):
    if not email:
      raise ValueError('The Email field must be set')

    email = self.normalize_email(email)

    extra_fields.setdefault('date_joined', timezone.now())
    extra_fields.setdefault('is_active', True)

    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    return self.create_user(email, password, **extra_fields)


# Create your models here.
class User(AbstractUser):
  username = None
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=50, unique=True)
  password = models.CharField(max_length=200)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = MyUserManager()

  def __str__(self) -> str:
    return self.email

  class Meta:
    db_table = 'user'
    verbose_name = 'user'
    verbose_name_plural = 'users'
