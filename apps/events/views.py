from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, View
from .models import Event, Enrollment
from .forms import EventForm, EnrollmentForm

# Create your views here.
class EventsView(ListView):
  model = Event
  template_name = 'list_events.html'
  context_object_name = 'events_data'


class EventCreate(CreateView):
  model = Event
  form_class = EventForm
  template_name = 'create_event.html'
  success_url = reverse_lazy('events:list')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class EventDetail(View):
  model = Event
  template_name = 'event_detail.html'

  def get(self, request, event_id):
    event = self.model.objects.get(id=event_id)

    if event is not None:
      return render(request, self.template_name, { 'event': event })

    return redirect('events:list')


class EventEnrollCreate(CreateView):
  model = Enrollment
  form_class = EnrollmentForm
  template_name = 'event_enroll.html'
  success_url = reverse_lazy('events:my_enrollments')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class MyEnrolledEvents(View):
  model = Enrollment
  template_name = 'list_enrolled_events.html'

  def get(self, request):
    user = self.request.user
    enrollments = self.model.objects.filter(user=user)

    enrolled_events = [enrollment.event for enrollment in enrollments]

    return render(request, self.template_name, { 'enrolled_events': enrolled_events })
