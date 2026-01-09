from pypdf import PdfReader
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


def load_pdf_text(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def analyze(resume_path, jd_path):
    resume_text = load_pdf_text(resume_path)
    jd_text = load_pdf_text(jd_path)

    llm = ChatOpenAI(model="gpt-4o")

    prompt = f"""
Compare the following resume and job description.

Resume:
{resume_text}

Job Description:
{jd_text}

Return ONLY:
Match score as a number followed by percent sign (example: 76%)
"""

    return llm.predict(prompt).strip()


def imp(resume_path, jd_path):
    resume_text = load_pdf_text(resume_path)
    jd_text = load_pdf_text(jd_path)

    llm = ChatOpenAI(model="gpt-4o")

    prompt = f"""
Compare the following resume and job description.

Resume:
{resume_text}

Job Description:
{jd_text}

Return within 100 words:
1. Missing skills
2. Improvement suggestions
"""

    return llm.predict(prompt).strip()
