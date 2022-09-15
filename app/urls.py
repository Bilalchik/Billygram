from django.urls import path

from . import views

urlpatterns = [
    path('', views.auth, name='login'),
    path('index/<int:pk>/', views.index, name='index'),
    path('register/', views.register_request, name="register"),
    path('list/', views.list_view, name='list'),
    path('detail/<str:pk>/', views.detail, name='detail'),
    path('create_post', views.create_post, name='create_post'),
    path('search/', views.search, name='search'),
    path('logout/', views.logoutView, name='logout')
]