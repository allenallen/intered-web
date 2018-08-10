from django.urls import path

from . import views

urlpatterns = [
    path('register/<int:pk>', views.registration, name='register'),
]
