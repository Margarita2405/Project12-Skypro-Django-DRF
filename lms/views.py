from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from lms.models import Course, Lesson, Subscription
from lms.paginators import LmsPagination
from lms.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsNotModerator, IsOwner


# CRUD для Курсов через ViewSet
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    pagination_class = LmsPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Course.objects.none()
        if user.groups.filter(name="moderators").exists():
            return Course.objects.all().order_by("id")  # Добавили сортировку
        return Course.objects.filter(owner=user).order_by("id")  # Добавили сортировку

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [IsAuthenticated, IsNotModerator]
        elif self.action in ["destroy", "update", "partial_update"]:
            self.permission_classes = [IsAuthenticated, IsNotModerator, IsOwner]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# CRUD для Уроков через Generics
class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    pagination_class = LmsPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Lesson.objects.none()
        if user.groups.filter(name="moderators").exists():
            return Lesson.objects.all().order_by("id")  # Добавили сортировку
        return Lesson.objects.filter(owner=user).order_by("id")  # Добавили сортировку


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsNotModerator]  # только не модераторы

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Lesson.objects.none()
        if user.groups.filter(name="moderators").exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=user)


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Lesson.objects.none()
        if user.groups.filter(name="moderators").exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=user)


class LessonDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsNotModerator]  # только не модераторы

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Lesson.objects.none()
        return Lesson.objects.filter(owner=user)


# Класс для добавления и удаления подписки у пользователя
class SubscriptionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Получаем пользователя
        user = request.user
        # Получаем id курса из тела запроса (data)
        course_id = request.data.get("course_id")

        # Проверяем, существует ли курс вообще
        course_item = get_object_or_404(Course, id=course_id)

        # Ищем подписку этого пользователя на этот курс
        subs_item = Subscription.objects.filter(user=user, course=course_item)

        # Если подписка у пользователя на этот курс есть - удаляем ее
        if subs_item.exists():
            subs_item.delete()
            message = "подписка удалена"

        # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = "подписка добавлена"

        # Возвращаем ответ в API
        return Response({"message": message}, status=status.HTTP_200_OK)
