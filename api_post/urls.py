from django.urls import path, include
from api_post import views
from rest_framework.routers import DefaultRouter

app_name = 'post'

router = DefaultRouter()
router.register('', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
