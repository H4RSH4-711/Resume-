from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import JobPost
from resumes.models import JobApplication

@login_required
def recruiter_dashboard(request):
    if not request.user.is_recruiter:
        return redirect('dashboard')
    
    jobs = request.user.job_posts.order_by('-created_at')
    return render(request, 'jobs/recruiter_dashboard.html', {'jobs': jobs})

@login_required
def create_job(request):
    if not request.user.is_recruiter:
        return redirect('dashboard')
        
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        required_skills = request.POST.get('required_skills')
        location = request.POST.get('location')
        
        JobPost.objects.create(
            recruiter=request.user,
            title=title,
            description=description,
            required_skills=required_skills,
            location=location
        )
        return redirect('jobs:recruiter_dashboard')
        
    return render(request, 'jobs/create_job.html')

@login_required
def job_applicants(request, job_id):
    if not request.user.is_recruiter:
        return redirect('dashboard')
        
    job = get_object_or_404(JobPost, id=job_id, recruiter=request.user)
    applications = job.applications.order_by('-match_score')
    
    return render(request, 'jobs/job_applicants.html', {'job': job, 'applications': applications})

@login_required
def update_application_status(request, app_id, new_status):
    if not request.user.is_recruiter:
        return redirect('dashboard')
        
    application = get_object_or_404(JobApplication, id=app_id, job__recruiter=request.user)
    
    if new_status in dict(JobApplication.STATUS_CHOICES):
        application.status = new_status
        application.save()
        
    return redirect('jobs:job_applicants', job_id=application.job.id)
