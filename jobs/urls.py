from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [
    path('dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('create/', views.create_job, name='create_job'),
    path('<int:job_id>/applicants/', views.job_applicants, name='job_applicants'),
    path('application/<int:app_id>/status/<str:new_status>/', views.update_application_status, name='update_application_status'),
]
