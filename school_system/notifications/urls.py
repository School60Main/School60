from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('create/', views.create_notification, name='create_notification'),
    path('', views.list_notifications, name='list_notifications'),
    path('<int:pk>/', views.notification_detail, name='notification_detail'),
]
