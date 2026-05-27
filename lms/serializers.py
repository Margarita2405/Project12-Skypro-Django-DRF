from rest_framework import serializers

from lms.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    # Добавляем вложенный список уроков, которые принадлежат курсу (благодаря related_name="lessons")
    lessons = LessonSerializer(many=True, read_only=True)
    lessons_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ["id", "title", "description", "lessons", "lessons_count"]

    def get_lessons_count(self, obj):
        return obj.lessons.count()
