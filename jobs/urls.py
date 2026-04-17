from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:pk>/', views.job_detail, name='job_detail'),
    path('jobs/<int:pk>/apply/', views.apply_job, name='apply_job'),
    path('jobs/post/', views.post_job, name='post_job'),
    path('jobs/<int:pk>/edit/', views.edit_job, name='edit_job'),
    path('jobs/<int:pk>/delete/', views.delete_job, name='delete_job'),
    path('jobs/<int:pk>/applications/', views.view_applications, name='view_applications'),
    path('applications/<int:pk>/status/', views.update_application_status, name='update_status'),
]
