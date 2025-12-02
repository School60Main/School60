from django.urls import path
from . import views

app_name = 'materials'

urlpatterns = [
    path('', views.material_list, name='material_list'),
    path('upload/', views.material_upload, name='material_upload'),
    path('<int:pk>/', views.material_detail, name='material_detail'),
]
