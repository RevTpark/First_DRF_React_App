from .views import (PostList, PostDetail, PostDetailFilter, PostCreate,
                    EditPost, AdminPostDetail, DeletePost)
from django.urls import path
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

# router = DefaultRouter()
# router.register('', PostList, basename='post')
# urlpatterns = router.urls

urlpatterns = [
    path('posts/<str:slug>/', PostDetail.as_view(), name='detail_create'),
    path("search/", PostDetailFilter.as_view(), name="filter_detail"),
    path('', PostList.as_view(), name='list_create'),

    # Post Admin
    path("admin/create/", PostCreate.as_view(), name="create_post"),
    path("admin/edit/postdetail/<int:pk>/", AdminPostDetail.as_view(), name="admin_post_detail"),
    path("admin/edit/<int:pk>/", EditPost.as_view(), name="edit_post"),
    path("admin/delete/<int:pk>/", DeletePost.as_view(), name="delete_post"),
]
