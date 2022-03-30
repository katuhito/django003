from django.urls import path
from . import views

app = 'first_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('article/<int:pk>/', views.ArticleView.as_view(), name='article'),
    path('article/new/', views.NewView.as_view(), name='new'),
    path('article/comment/', views.CommentView.as_view(), name='comment')
]