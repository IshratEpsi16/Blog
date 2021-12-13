from django.urls import path
from . import views
app_name = 'blog_app'
urlpatterns = [
    
    path('',views.BlogList.as_view(),name='blog_list'),
    path('write',views.CreateBlog.as_view(),name='create_blog'),
    path('details/<int:pk>',views.blog_details, name='blog_details'),
    path('liked/<pk>/',views.liked, name='liked_post'),
    path('unliked/<pk>/',views.unliked, name='unliked_post'),
    path('my-blogs/',views.MyBlogs.as_view(), name='my_blogs'),
    path('edit-blogs/<pk>/',views.UpdateBlog.as_view(), name='edit_blogs'),
    path('delete-blogs/<pk>/',views.DeleteBlog.as_view(), name='delete_blogs'),    

]