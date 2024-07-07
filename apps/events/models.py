from django.db import models
from django.conf import settings

# Create your models here.
class Event(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=255)
  location = models.CharField(max_length=200)
  date_time = models.DateTimeField(auto_created=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return self.name

  class Meta:
    db_table = 'event'
    verbose_name = 'event'
    verbose_name_plural = 'events'


class Enrollment(models.Model):
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_created=True)

  def __str__(self) -> str:
    return self.event

  class Meta:
    db_table = 'enrollment'
    verbose_name = 'enrollment'
    verbose_name_plural = 'enrollments'
