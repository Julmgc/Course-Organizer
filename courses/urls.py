from django.urls import path
from .views import CourseView, CourseViewQuery, CourseSubmissionsView

urlpatterns = [
    path("courses/", CourseView.as_view()),
    path("courses/<int:course_id>/", CourseViewQuery.as_view()),
    path("courses/<int:course_id>/registrations/", CourseSubmissionsView.as_view())
]

