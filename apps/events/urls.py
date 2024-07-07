from django.urls import path
from . import views

urlpatterns = [
  path('events/', views.EventsView.as_view(), name='list'),
  path('events/create', views.EventCreate.as_view(), name='create'),
  path('events/<int:event_id>', views.EventDetail.as_view(), name='detail'),
  path('events/enroll', views.EventEnrollCreate.as_view(), name='enroll'),
  path('events/my_enrollments', views.MyEnrolledEvents.as_view(), name='my_enrollments'),
]
