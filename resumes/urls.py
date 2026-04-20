from django.urls import path
from . import views

urlpatterns = [
    # Upload & analyze
    path('upload/', views.upload_resume, name='upload_resume'),
    path('<int:pk>/', views.resume_detail, name='resume_detail'),
    path('<int:pk>/delete/', views.delete_resume, name='delete_resume'),
    path('<int:pk>/reanalyze/', views.reanalyze_resume, name='reanalyze_resume'),
    # Builder
    path('builder/', views.builder_list, name='builder_list'),
    path('builder/create/', views.builder_create, name='builder_create'),
    path('builder/<int:pk>/edit/', views.builder_edit, name='builder_edit'),
    path('builder/<int:pk>/save/', views.builder_save, name='builder_save'),
    path('builder/<int:pk>/ai/', views.builder_ai_enhance, name='builder_ai_enhance'),
    path('builder/<int:pk>/preview/', views.builder_preview, name='builder_preview'),
    path('builder/<int:pk>/delete/', views.builder_delete, name='builder_delete'),
]
