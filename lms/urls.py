from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .apps import LmsConfig
from .views import (CourseViewSet, LessonCreateAPIView, LessonDestroyAPIView, LessonListAPIView, LessonRetrieveAPIView,
                    LessonUpdateAPIView)

app_name = LmsConfig.name

# Регистрация ViewSet для курсов
router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="course")

urlpatterns = [
    # Маршруты для курсов (автоматически создаст /courses/ и /courses/<id>/)
    path("", include(router.urls)),
    # Маршруты для уроков (Generics)
    path("lessons/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_get"),
    path("lessons/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson_update"),
    path("lessons/delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson_delete"),
]
