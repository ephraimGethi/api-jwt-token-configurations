from django.urls import path

from .views import getRoutes,getNotes
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('',getRoutes,name='routes'),
    path('notes/',getNotes),
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view())
]