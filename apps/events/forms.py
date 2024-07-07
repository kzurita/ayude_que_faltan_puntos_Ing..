from django.forms import ModelForm
from .models import Event, Enrollment

class EventForm(ModelForm):
  class Meta:
    model = Event
    fields = [
      'name',
      'description',
      'location',
      'date_time',
    ]


class EnrollmentForm(ModelForm):
  class Meta:
    model = Enrollment
    fields = ['event', 'date']
