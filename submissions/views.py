from accounts.permissions import Instructor_Facilitator
from activities.models import Activities
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Submissions
from .serializers import SubmissionSerializer


class ActivitySubmissionView(APIView):
    authentications_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, activity_id=''):
        try:
            activity = Activities.objects.get(id=activity_id)
            data = request.data
            user = request.user
            if user.is_staff or user.is_superuser:
                return Response({"errors": "Only students can submit an activity."}, status=status.HTTP_403_FORBIDDEN)
            
            submission = Submissions.objects.create(grade=None, repo=data["repo"], user_id=user.id, activity_id=activity.id)
            serializer = SubmissionSerializer(submission)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Activities.DoesNotExist:
            return Response({'error': 'Activity not found'}, status=status.HTTP_404_NOT_FOUND)


class SubmissionView(APIView):
    authentications_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.is_staff or user.is_superuser:
            submissions = Submissions.objects.all()
            serializer = SubmissionSerializer(submissions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        submissions = user.submission_id
        serializer = SubmissionSerializer(submissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubmissionGradeView(APIView):
    authentications_classes = [TokenAuthentication]
    permission_classes = [Instructor_Facilitator]

    def put(self, request, submission_id=''):


        submission = Submissions.objects.get(id=submission_id)
        if not submission:
            return Response({"errors": "invalid submission_id."}, status=status.HTTP_404_NOT_FOUND)
        grade = request.data["grade"]
        submission.grade = grade
        submission.save()
        serializer = SubmissionSerializer(submission)
        return Response(serializer.data, status=status.HTTP_200_OK)


