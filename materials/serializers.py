from rest_framework import serializers

from .models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('title', 'preview', 'description', 'video_url', 'courses')

class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        return obj.lesson.count()

    class Meta:
        model = Course
        fields = ('title', 'image', 'description', 'lesson_count', 'lessons')