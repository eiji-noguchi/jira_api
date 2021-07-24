from django.urls import path, include
from rest_framework import routers
from .views import CreateUserView, ListUserView, LoginUserView, ProfileViewSet, CategoryViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('tasks', TaskViewSet)
router.register('profile', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', CreateUserView.as_view(), name='create'),
    path('users/', ListUserView().as_view(), name='users'),
    path('loginuser/', LoginUserView.as_view(), name='loginuser'),
]