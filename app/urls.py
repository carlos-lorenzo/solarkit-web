from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("orbits/", views.orbits),
    path("spinograph/", views.spinograph),
    path("heliocentric/", views.heliocentric),
    path("third-law/", views.third_law),
]