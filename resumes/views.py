from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Resume, JobApplication
from jobs.models import JobPost
from .utils import extract_text_from_pdf, calculate_match_score

@login_required
def candidate_dashboard(request):
    if not request.user.is_candidate:
        return redirect('dashboard')
    
    resume = request.user.resumes.last()
    applications = request.user.applications.all()
    
    return render(request, 'resumes/candidate_dashboard.html', {
        'resume': resume,
        'applications': applications
    })

@login_required
def upload_resume(request):
    if not request.user.is_candidate:
        return redirect('dashboard')
        
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            resume = Resume.objects.create(candidate=request.user, file=file)
            
            # Extract text
            file_path = resume.file.path
            text = extract_text_from_pdf(file_path)
            resume.extracted_text = text
            resume.save()
            return redirect('resumes:candidate_dashboard')
            
    return render(request, 'resumes/upload_resume.html')

@login_required
def browse_jobs(request):
    if not request.user.is_candidate:
        return redirect('dashboard')
        
    jobs = JobPost.objects.all().order_by('-created_at')
    resume = request.user.resumes.last()
    
    job_scores = []
    for job in jobs:
        score = 0.0
        if resume and resume.extracted_text:
            score = calculate_match_score(resume.extracted_text, job.required_skills)
        job_scores.append({
            'job': job,
            'score': score
        })
        
    # Sort descending by score
    job_scores.sort(key=lambda x: x['score'], reverse=True)
    
    return render(request, 'resumes/browse_jobs.html', {'job_scores': job_scores})

@login_required
def apply_job(request, job_id):
    if not request.user.is_candidate:
        return redirect('dashboard')
        
    job = get_object_or_404(JobPost, id=job_id)
    resume = request.user.resumes.last()
    
    if not resume:
        return redirect('resumes:upload_resume')
        
    if not JobApplication.objects.filter(candidate=request.user, job=job).exists():
        score = calculate_match_score(resume.extracted_text, job.required_skills)
        JobApplication.objects.create(
            candidate=request.user,
            job=job,
            resume=resume,
            match_score=score
        )
        
    return redirect('resumes:candidate_dashboard')
