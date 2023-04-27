from django.urls import path
from . import views

app_name = 'infobases'
urlpatterns = [
    path('', views.main, name='main'),
    path('create/', views.create, name='create'),
    path('<int:infobase_pk>/', views.detail, name='detail'),
    path('<int:infobase_pk>/delete/', views.delete, name='delete'),
    path('<int:infobase_pk>/update/', views.update, name='update'),
    path('<int:infobase_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:infobase_pk>/comments/<int:comment_pk>/delete', views.comments_delete, name='comments_delete'),
]
