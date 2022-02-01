from django.urls import path
from . import views


urlpatterns = [
	path('', views.main, name='main'),
    path('post_list/', views.post_list, name='post_list'),
    path('midpost/<int:pk>/', views.mid_post_list, name='mid_post_list'),
    path('lastpost/<int:pk>/', views.last_post_list, name='last_post_list'),
    path('post/<int:pk>/', views.post_result, name='post_result'),
    path('post/detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('servey/<int:pk>/', views.servey_form, name='servey_form'),
]
