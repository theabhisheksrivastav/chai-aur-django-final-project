from . import views
from django.urls import path

urlpatterns = [
    path('', views.posts, name='all_posts'),
    path('create/', views.create_post, name='create_post'),
    path('<int:post_id>/update/', views.update_post, name='update_post'),
    path('<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('register/', views.register, name='register'),
]
