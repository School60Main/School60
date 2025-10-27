from django.urls import path
from . import views

app_name = "substitutions"

urlpatterns = [
    path('', views.substitution_list, name='substitution_list'),
    path('upload/', views.upload_substitutions, name='upload_substitutions'),
]
