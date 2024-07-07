
from django.contrib import admin
from django.urls import path, include
from apps.authentication import views

urlpatterns = [
  path('admin/', admin.site.urls),

  # Authentication
  path('', include(('apps.authentication.urls', 'authentication'), namespace='authentication')),

  # Events
  path('', include(('apps.events.urls', 'events'), namespace='events')),
]
