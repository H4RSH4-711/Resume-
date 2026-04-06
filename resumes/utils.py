import string
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
    except Exception as e:
        print(f"Error reading pdf: {e}")
    return text

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def calculate_match_score(resume_text, job_skills_text):
    if not resume_text or not job_skills_text:
        return 0.0
    
    clean_resume = clean_text(resume_text)
    clean_job = clean_text(job_skills_text)
    
    documents = [clean_job, clean_resume]
    
    tfidf = TfidfVectorizer(stop_words='english')
    try:
        tfidf_matrix = tfidf.fit_transform(documents)
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        # Returning a percentage score
        return round(float(similarity[0][0]) * 100, 2)
    except Exception as e:
        print(f"Error calculating score: {e}")
        return 0.0
