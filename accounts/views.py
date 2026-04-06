from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CandidateRegistrationForm, RecruiterRegistrationForm

def register_candidate(request):
    if request.method == 'POST':
        form = CandidateRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CandidateRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form, 'role': 'Candidate'})

def register_recruiter(request):
    if request.method == 'POST':
        form = RecruiterRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RecruiterRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form, 'role': 'Recruiter'})

def dashboard_redirect(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.is_recruiter:
        return redirect('jobs:recruiter_dashboard')
    elif request.user.is_candidate:
        return redirect('resumes:candidate_dashboard')
    return redirect('login')
