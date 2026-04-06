from django.urls import path
from . import views

app_name = 'resumes'
urlpatterns = [
    path('dashboard/', views.candidate_dashboard, name='candidate_dashboard'),
    path('upload/', views.upload_resume, name='upload_resume'),
    path('jobs/', views.browse_jobs, name='browse_jobs'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
]
