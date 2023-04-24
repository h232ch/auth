# urls.py
# from django.db import router
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from user.views import RegisterAPIView, AuthAPIView, UserViewSet, UserListView

router = DefaultRouter()
router.register('user_list', UserViewSet)

urlpatterns = [
    path("register/", RegisterAPIView.as_view()), # post - 회원가입
    path("auth/", AuthAPIView.as_view()),
    path("auth/refresh/", TokenRefreshView.as_view()), # jwt 토큰 재발급
    path('', include(router.urls)),
    path('test/', UserListView.as_view())
]
