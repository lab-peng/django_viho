from django.urls import path
from . import views

urlpatterns = [
    path('', views.bootstrap_border_table, name='bootstrap_border_table'),
    path('index', views.index, name='index'),
    path('dropzone/', views.dropzone, name='dropzone'),
    path('file_manager/', views.file_manager, name='file_manager'),
    path('base_input/', views.base_input, name='base_input'),

    path('project_update/<int:pk>/', views.project_update, name='project_update'),
]
