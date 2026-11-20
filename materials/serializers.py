from rest_framework import serializers

from .models import Course, Lesson

class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    def get_lessen_count(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ('title', 'image', 'description', 'lesson_count')

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('title', 'preview', 'description', 'video_url', 'courses')