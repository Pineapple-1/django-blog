from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='Post-View'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='Post-Update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='Post-Delete'),
    path('post/new/', PostCreateView.as_view(), name='Post-Create'),
    path('about/', views.about, name='blog-about')
]
 