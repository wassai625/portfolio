from django.urls import path, include
from api_post import views
from rest_framework.routers import DefaultRouter

app_name = 'post'

router = DefaultRouter()
# router.register('profile', views.ProfileViewSet)
# router.register('approval', views.FriendRequestViewSet)

urlpatterns = [
    path('create/', views.CreatePostView.as_view(), name='create'),
    path('', include(router.urls))
]
