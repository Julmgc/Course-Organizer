from accounts.permissions import Instructor_Facilitator
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Activities
from .serializers import ActivitySerializer


class ActivityView(APIView):
    authentications_classes = [TokenAuthentication]
    permission_classes = [Instructor_Facilitator]

    def post(self, request):
      try:
          data = request.data
          activity = Activities.objects.create(**data)
          serializer = ActivitySerializer(activity)
          return Response(serializer.data, status=status.HTTP_201_CREATED)

      except IntegrityError:
          return Response({'error': 'Activity with this name already exists'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = request.user
        if user.is_staff or user.is_superuser:
            activities = Activities.objects.all()
            serializer = ActivitySerializer(activities, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({ "detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)

class ActivityViewQuery(APIView):
    authentications_classes = [TokenAuthentication]
    permission_classes = [Instructor_Facilitator]

    def put(self, request, activity_id=''):
        try:
            data = request.data
            activity = get_object_or_404(Activities, id=activity_id)

            if hasattr(activity, "submissions"):
                if activity.submissions.first():
                    return Response({'error': 'You can not change an Activity with submissions'}, status=status.HTTP_400_BAD_REQUEST)
            title = data["title"]
            points = data["points"]
            activity.title = title
            activity.points = points
            activity.save()
            serializer = ActivitySerializer(activity)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({'error': 'Activity with this name already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
