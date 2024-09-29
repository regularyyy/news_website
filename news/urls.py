from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/new/', views.create_article, name='create_article'),
    path('article/<int:pk>/edit/', views.update_article, name='update_article'),
    path('article/<int:pk>/delete/', views.delete_article, name='delete_article'),
]
