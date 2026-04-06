# AI-Powered Smart Recruitment & Resume Screening System

The objective is to build a robust Django-based recruitment portal where recruiters can post jobs, and candidates can upload their resumes. The system will leverage basic AI/NLP components to parse resumes, extract relevant skills, and rank candidates against specific job postings to significantly speed up the screening process.

## User Review Required

> [!IMPORTANT]
> Please review the core application logic and UI assumptions below. Since the project will be built from scratch, ensuring the data schema and parsing approach matches your expectations is essential. Once you approve, I will proceed to build out the project.

## Proposed Architecture

### 1. Project & Environment Setup
- **Framework:** Django 5.x with Python 3.10+
- **Database:** SQLite3 (as requested, perfect for rapid development/prototyping)
- **Dependencies:** `django`, `pillow` (for profile images), `django-crispy-forms` (for beautiful UI forms), `pdfplumber` or `PyPDF2` (for parsing PDF resumes), `spacy` or `scikit-learn` (for extracting skills and calculating job-resume match scores).

### 2. Application Modules

The Django project (`smart_recruitment`) will consist of the following apps:

#### `accounts`
- **Models:** Custom User model with two roles: `is_recruiter` and `is_candidate`.
- **Functionality:** Registration and Login routing based on the user's role. Profile management.

#### `jobs`
- **Models:** 
  - `JobPost` (Title, Description, Required Skills, Location, Salary, Created At).
- **Functionality:** Recruiter capability to Create, Read, Update, and Delete job posts. Candidates capability to view job listings.

#### `resumes`
- **Models:**
  - `Resume` (Candidate Foreign Key, FileField for PDF/DOCX, Extracted Text, Extracted Skills, Upload Timestamp).
  - `JobApplication` (Candidate, JobPost, Resume, Match Score, Status, Applied At).
- **Functionality:** Upload resumes, trigger the AI parsing utility, and execute the matching algorithm upon application.

### 3. AI & Data Processing Layer

- **Resume Parsing:** When a candidate uploads a resume, a utility function will read the document (e.g., using `pdfplumber`).
- **Data Cleaning:** Regex operations to clean stop-words, basic formatting, and special characters.
- **Feature Extraction & Matching:** Using a set of target skills, we will extract skills from the resume and compare them to the `Required Skills` of a `JobPost`. A **Similarity Score** (e.g., Jaccard similarity or TF-IDF Cosine Similarity) will be calculated and saved as the `match_score` in the `JobApplication`.

### 4. UI/UX Layer

- **Frontend Technologies:** HTML5, CSS3, JavaScript, and Bootstrap 5.
- **Design Elements:** 
  - A clean, modern navigation bar.
  - A dedicated "Recruiter Dashboard" displaying job postings and a ranked list of candidate matches.
  - A "Candidate Dashboard" for applying to jobs and tracking their status.
  - Interactive alerts and glassmorphic/modern card designs to make the system feel premium and dynamic.

---

## Open Questions

Before moving to the execution phase, I have a few clarifying questions:
1. **Machine Learning Approach:** Would you prefer deploying a lightweight NLP library (like `spacy` to extract specific entities) or a simpler skill-matching algorithm (like keyword matching with term frequencies/TF-IDF)? For local ease, simpler text processing is usually faster, but `spacy` provides better entity recognition.
2. **Application Process:** Should candidates manually click "Apply" on a job, or should the system automatically parse their resume and match them against all open jobs instantly once they upload?
3. **File Formats:** Should we restrict uploaded resumes to PDFs, or do you need support for DOCX files as well?

## Verification Plan

### Automated/Local Testing
- Run Django's built-in `runserver` and test local navigation.
- Write simple automated tests for the skill-matching algorithm to ensure it generates consistent scores.
- Use dummy resumes (PDFs) to test text extraction.

### Manual Verification
- Walk through the user flow: Register as a Recruiter -> Post a Job -> Register as a Candidate -> Upload Resume -> Apply for a Job -> Verify matching score -> Recruiter views ranked Candidate.
