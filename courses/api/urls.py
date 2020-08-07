from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'courses'
routers = routers.DefaultRouter()
routers.register('courses', views.CourseViewSet)

urlpatterns = [
    path('subjects/', views.SubjectListView.as_view(), name='subject_list'),
    path('subjects/<pk>/', views.SubjectDetailView.as_view(),
         name='subject_detail'),
    # path('courses/<pk>/enroll/', views.CourseEnrollView.as_view(),
    #   name='course_enroll'), # bỏ do k dùng đến khi có CourseViewSet
    path('', include(routers.urls)),
]