from rest_framework import viewsets, generics, response, status
from django.shortcuts import get_object_or_404

from .models import Lesson, Course
from .serializers import CourseSerializer, LessonSerializer

# Create your views here.
#Courses
class CourseViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return response.Response(serializer.data)

    def create(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course)
        return response.Response(serializer.data)

    def update(self, request, pk=None):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    def partial_update(self, request, pk=None):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    def destroy(self, request, pk=None):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


#Lessons
class LessonCreateList(generics.ListCreateAPIView):

    serializer_class = LessonSerializer
    permission_classes = []

    def get_queryset(self):
        return Lesson.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class LessonDetail(generics.RetrieveAPIView):

    serializer_class = LessonSerializer
    permission_classes = []

    def get_object(self):
        queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.kwargs['pk'])

class LessonUpdate(generics.UpdateAPIView):

    serializer_class = LessonSerializer
    permission_classes = []

    def get_queryset(self):
        return Lesson.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.kwargs['pk'])

class LessonDelete(generics.DestroyAPIView):

    serializer_class = LessonSerializer
    permission_classes = []

    def get_queryset(self):
        return Lesson.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.kwargs['pk'])
