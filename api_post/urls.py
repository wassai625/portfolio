from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_post import views

app_name = 'api_post'

router = DefaultRouter()
router.register('post', views.PostViewSet, basename='post')
router.register('comments',views.PostCommentListView,basename='postponement')
router.register('post_search', views.PostListView, basename='post_search')

urlpatterns = [
    path('', include(router.urls)),
]
