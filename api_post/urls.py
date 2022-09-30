from django.urls import path, include
from api_post import views
from rest_framework.routers import DefaultRouter

app_name = 'post'

router = DefaultRouter()
router.register('posts', views.PostViewSet)
# router.register('approval', views.FriendRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.CreatePostView.as_view(), name='create'),

]
