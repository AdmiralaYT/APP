from django.urls import path
from . import views 

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout_user", views.logout_user, name="logout_user"),
]
