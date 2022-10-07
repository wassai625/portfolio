from django.urls import path, include
from api_comment import views
from rest_framework.routers import DefaultRouter

app_name = 'comment'

router = DefaultRouter()
router.register('', views.Comment)

urlpatterns = [
    path('', include(router.urls)),
]
