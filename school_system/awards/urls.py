# awards/urls.py
from django.urls import path
from . import views

app_name = 'awards'

urlpatterns = [
    path('', views.award_list, name='award_list'),
    path('create/', views.award_create, name='award_create'),
    path('update/<int:pk>/', views.award_update, name='award_update'),
    path('delete/<int:pk>/', views.award_delete, name='award_delete'),
    path('<int:pk>/', views.award_detail, name='award_detail'),
]
