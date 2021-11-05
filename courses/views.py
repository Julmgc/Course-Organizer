from accounts.permissions import Instructor
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course
from .serializers import CourseSerializer


class CourseView(APIView):
    authentications_classes = [TokenAuthentication]
    permission_classes = [Instructor]

    def post(self, request):
      
        user = request.user

        if user.is_staff and user.is_superuser:
            data = request.data

            if Course.objects.filter(name=data["name"]).exists():

                return Response({'error': 'Course with this name already exists'}, status=status.HTTP_400_BAD_REQUEST)

            course = Course.objects.create(name=data["name"])
            serializer = CourseSerializer(course)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:

            return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
      

    def get(self, request):

        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True) 

        return Response(serializer.data, status=status.HTTP_200_OK)

class CourseViewQuery(APIView):
    authentications_classes = [TokenAuthentication]
    permission_classes = [Instructor]

    def put(self, request, course_id=''):
        try:
            course = get_object_or_404(Course, id=course_id)
            
            if not course:

                return Response(status=status.HTTP_404_NOT_FOUND)

            course.name = request.data["name"]
            course.save()
            serializer = CourseSerializer(course)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except IntegrityError:

            return Response({'error': 'Course with this name already exists'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, course_id=''):

        try:
            user = request.user

            if user.is_staff and user.is_superuser:
                course = Course.objects.get(id=course_id)
                course.delete()

                return Response(status=status.HTTP_204_NO_CONTENT)

            else:

                return Response(status=status.HTTP_403_FORBIDDEN)

        except Course.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, course_id=''):
        try:
            course =  Course.objects.get(id=course_id)

            serializer = CourseSerializer(course)

            return Response(serializer.data)
        
        except Course.DoesNotExist:

            return Response({"errors": "invalid course_id"}, status=status.HTTP_404_NOT_FOUND)

class CourseSubmissionsView(APIView):
    
    authentications_classes = [TokenAuthentication]
    permission_classes = [Instructor]

    def put(self, request, course_id=''):

        try:
            course =  Course.objects.get(id=course_id)
            students = request.data.pop("user_ids")

            if type(students) == list:

                for student in students:

                    try:
                        specific_student = User.objects.get(id=student)

                    except User.DoesNotExist:

                        return Response({"errors": "invalid user_id list."}, status=status.HTTP_404_NOT_FOUND)    

                    if  User.objects.filter(id=student) == None:

                        return Response({"errors": "invalid user_id."}, status=status.HTTP_404_NOT_FOUND)

                    if specific_student.is_staff or specific_student.is_superuser:

                        return Response({"errors": "Only students can be enrolled in the course."}, status=status.HTTP_400_BAD_REQUEST)
                
                course.users.set(students)
                serializer = CourseSerializer(course)

                return Response(serializer.data, status=status.HTTP_200_OK)

            else:

                return Response({"errors": "Please send a list with the students ids."}, status=status.HTTP_400_BAD_REQUEST)
 
        except Course.DoesNotExist:
            
            return Response({"errors": "invalid course_id"}, status=status.HTTP_404_NOT_FOUND)
