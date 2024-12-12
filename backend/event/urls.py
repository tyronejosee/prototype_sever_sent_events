"""Urls for Events App."""

from django.urls import path
from django.urls.resolvers import URLPattern

from .views import event_stream


urlpatterns: list[URLPattern] = [
    path(
        "sse/",
        event_stream,
        name="event_stream",
    )
]
