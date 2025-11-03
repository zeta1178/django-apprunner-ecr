from django.urls import path
from .views import hello_world
from .views import health

urlpatterns = [
    path('hello/', hello_world),
    path('health/', health),
]
