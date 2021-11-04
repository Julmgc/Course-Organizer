from django.urls import path
from .views import ActivitySubmissionView, SubmissionView, SubmissionGradeView


urlpatterns = [
    path("activities/<int:activity_id>/submissions/", ActivitySubmissionView.as_view()),
    path("submissions/", SubmissionView.as_view()),
    path("submissions/<int:submission_id>/", SubmissionGradeView.as_view())
]
