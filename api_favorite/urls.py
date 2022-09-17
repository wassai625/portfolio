from django.urls import path
from . import views

app_name = 'favorite'

urlpatterns = [
    path('post_list/', views.PostList.as_view(), name='post_list'),
    path('post_detail/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('favorite_for_post/', views.favorite_for_post, name='favorite_for_post'),
    path('favorite_for_comment/', views.favorite_for_comment, name='favorite_for_comment'),
]