from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView
from . import views

urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='Post-View'),
    path('post/new/',PostCreateView.as_view(),name='Post-Create'),
    path('about/',views.about,name='blog-about')
    ]