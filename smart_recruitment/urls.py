from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/candidate/', accounts_views.register_candidate, name='register_candidate'),
    path('accounts/register/recruiter/', accounts_views.register_recruiter, name='register_recruiter'),
    path('dashboard/', accounts_views.dashboard_redirect, name='dashboard'),
    path('jobs/', include('jobs.urls', namespace='jobs')),
    path('resumes/', include('resumes.urls', namespace='resumes')),
    path('', accounts_views.dashboard_redirect, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
