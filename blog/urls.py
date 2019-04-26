from django.urls import path
from . import views
urlpatterns = [
    path('',views.posts,name='AllPosts'),
    path('posts/details/<int:id>', views.details, name="DetailsPage"),
]