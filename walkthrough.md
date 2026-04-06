# AI-Powered Smart Recruitment Walkthrough

Congratulations! The **AI-Powered Smart Recruitment & Resume Screening System** has been fully implemented.

## What Was Built

The project is a full-stack Django application containing three primary modules:
1. **Accounts App (`accounts`)**: Contains the Custom User model and handles registration/authentication for both **Candidates** and **Recruiters**.
2. **Jobs App (`jobs`)**: Allows recruiters to create and manage job postings and view the applicants uniquely matched to their job specs.
3. **Resumes App (`resumes`)**: The core AI module. Candidates upload their resumes in PDF format, the text is extracted using `pdfplumber`, and a similarity `match_score` is generated using `scikit-learn`'s TF-IDF cosine similarity against the job's required skills.

> [!TIP]
> **Premium UI/UX:** The entire frontend is styled using custom Bootstrap 5 configurations, featuring a "glassmorphic" motif, hover animations, and FontAwesome icons, making the platform feel incredibly modern and engaging.

## How to Run the Project

You can run the application directly from the activated virtual environment.

### 1. Start the Server
Open your terminal in the project directory (`e:\Inspire Programs Feb 2026\Viswam - FSD Project Team\Project Folder\AI-Powered Smart Recruitment`).
Run the Python development server:
```powershell
.\venv\Scripts\python.exe manage.py runserver
```

### 2. View the Application
Navigate to [http://localhost:8000](http://localhost:8000) in your web browser. 
- You will be greeted by the login page.
- Select `Register Candidate` or `Register Recruiter` to test the completely isolated user flows.

## User Flow Testing Scenarios

> [!NOTE]
> If a candidate uploads a resume and the recruiter has posted a job, the candidate's browse feed will automatically display the job cards sorted by their personalized AI generated **Match Score**!

1. **Recruiter Flow**: Register -> Create Job (e.g., "Python Developer", list skills: Python, Django, SQL) -> Wait for applicants.
2. **Candidate Flow**: Register -> Upload PDF Resume -> Browse Open Jobs -> See match percentage -> Hit "Apply Now".
3. **Review Flow**: Recruiter visits the job -> Sees Candidates sorted from best Match Score -> Recruiter updates status from Pending to "Shortlisted".

Everything is persistent in the SQLite3 database, and files are saved into the `media/resumes/` directory automatically upon upload.
