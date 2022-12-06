from django.urls import path, include
from api_post import views
from rest_framework.routers import DefaultRouter

app_name = 'api_post'

router = DefaultRouter()
router.register('post',views.PostViewSet,basename='post')

urlpatterns = [
    path('', include(router.urls))
]