from django.contrib import admin
from django.urls import path
from .views import LikePostView, PostLikeCountView, PostListByCommentCountView

from lionapp import views

urlpatterns = [
    path('create/', views.create_post),
    path('<int:pk>/', views.get_post),
    path('like_post/', views.LikePostView.as_view()),
    path('post_like_count/', views.PostLikeCountView.as_view()),
    path('post_list_by_comment_count/', views.PostListByCommentCountView.as_view()),
    path('delete/<int:pk>/', views.delete_post),
    path('comments/<int:post_id>',views.get_comment),
    path('v2/post/<int:pk>',views.PostApiView.as_view()),
    path('v2/post',views.create_post_v2)
]






