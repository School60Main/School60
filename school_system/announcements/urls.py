from django.urls import path
from . import views

app_name = 'announcements'

urlpatterns = [
    path('', views.announcement_list, name='announcement_list'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('add/', views.add_announcement, name='add_announcement'),
    path('edit/<int:pk>/', views.edit_announcement, name='edit_announcement'),
    path('delete/<int:pk>/', views.delete_announcement, name='delete_announcement'),
]
