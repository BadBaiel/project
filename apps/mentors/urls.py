from apps.mentors import views
from django.urls import path, include
# from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('mentor/', views.MentorListAPIView.as_view()),
    path('mentor/create/', views.MentorCreateAPIView.as_view()),
    path('mentor/<int:pk>/', views.MentorDetailAPIView.as_view()),
]

# router = DefaultRouter()
# router.register('mentor', views.MentorApiView, basename='mentor')
# urlpatterns = router.urls
