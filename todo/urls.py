from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('todo/<int:pk>/', views.post_detail, name='post_detail'),
    path('todo/<int:pk>/delete', views.post_delete, name='post_delete'),
    path('todo/new', views.post_new, name='post_new'),
    path('todo/<int:pk>/check', views.post_check, name='post_check'),
    path('todo/<int:pk>/priority_up', views.post_priority_up, name='post_priority_up'),
    path('todo/<int:pk>/priority_down', views.post_priority_down, name='post_priority_down'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]