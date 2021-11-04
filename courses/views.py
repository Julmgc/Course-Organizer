from accounts.permissions import Instructor
from django.contrib.auth.models import User
from rest_framework import  status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course
from .serializers import CourseSerializer


class CourseView(APIView):
    authentications_classes = [TokenAuthentication]
    permission_classes = [Instructor]

    def post(self, request):
        try:
            data = request.data
            if Course.objects.filter(name=data["name"]).exists():
                return Response({'error': 'Course with this name already exists'}, status=status.HTTP_400_BAD_REQUEST)
            course = Course.objects.create(name=data["name"])
            serializer = CourseSerializer(course)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e))

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)


class CourseViewQuery(APIView):
    authentications_classes = [TokenAuthentication]
    permission_classes = [Instructor]

    def put(self, request, course_id=''):
        course = Course.objects.get(id=course_id)

        if not course:
            return Response(status=status.HTTP_404_NOT_FOUND)

        course.name = request.data["name"]
        course.save()
        serializer = CourseSerializer(course)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, course_id=''):
        course = Course.objects.get(id=course_id)

        if not course:
            return Response(status=status.HTTP_404_NOT_FOUND)

        Course.objects.filter(id=course_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def get(self, request, course_id=''):
        course =  Course.objects.get(id=course_id)

        if not course:
            return Response({"errors": "invalid course_id"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(course)

        return Response(serializer.data)

class CourseSubmissionsView(APIView):
    authentications_classes = [TokenAuthentication]
    permission_classes = [Instructor]

    def put(self, request, course_id=''):
        course =  Course.objects.get(id=course_id)

        if not course:
            return Response({"errors": "invalid course_id"}, status=status.HTTP_404_NOT_FOUND)

        students = request.data.pop("user_ids")
        if type(students) == list:
            for student in students:
                specific_student = User.objects.get(id=student)
                
                if not User.objects.filter(id=student):
                    return Response({"errors": "invalid user_id"}, status=status.HTTP_404_NOT_FOUND)
                if specific_student.is_staff or specific_student.is_superuser:
                    return Response({"errors": "Only students can be enrolled in the course."}, status=status.HTTP_400_BAD_REQUEST)

            course.users.set(students)
            serializer = CourseSerializer(course)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"errors": "Please send a list with the students ids."}, status=status.HTTP_400_BAD_REQUEST)