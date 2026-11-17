from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import CourseViewSet, LessonCreateList, LessonDetail, LessonUpdate, LessonDelete
from .apps import MaterialsConfig

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lessons/', LessonCreateList.as_view()),
    path('lessons/<int:pk>/', LessonDetail.as_view()),
    path('lessons/<int:pk>/update/', LessonUpdate.as_view()),
    path('lessons/<int:pk>/delete/', LessonDelete.as_view()),
]

urlpatterns += router.urls