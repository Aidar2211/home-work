from django.contrib import admin
from django.urls import path
from test_app import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('posts/<int:id>/', views.get_post, name="posts_id"),
    path('posts/', views.get_all_posts, name='posts'),
    path('add_product/', views.add_product_view),
    path('add_product_comments/', views.add_product_comment)


]
