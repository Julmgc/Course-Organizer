from django.urls import path
from .views import ActivityView, ActivitySerializer, ActivityViewQuery


urlpatterns = [
    path("activities/", ActivityView.as_view()),
    path("activities/<int:activity_id>/", ActivityViewQuery.as_view()),
]

