import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import ne_chunk, pos_tag
from nltk.corpus import stopwords

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')

def parse_resume(resume_text):
    sentences = sent_tokenize(resume_text)
    return sentences

def extract_contact_info(sentences):
    contact_info = {}
    for sentence in sentences:
        words = word_tokenize(sentence)
        if '@' in sentence:
            contact_info['EMAIL'] = sentence
        elif any(char.isdigit() for char in sentence):
            contact_info['PHONE'] = sentence
    return contact_info

def extract_education(sentences):
    education = []
    for sentence in sentences:
        if 'university' in sentence.lower() or 'college' in sentence.lower():
            education.append(sentence)
    return education

def extract_experience(sentences):
    experience = []
    for sentence in sentences:
        if 'experience' in sentence.lower():
            experience.append(sentence)
    return experience

def extract_skills(sentences):
    skills = []
    stop_words = set(stopwords.words('english'))
    for sentence in sentences:
        words = word_tokenize(sentence)
        for word in words:
            if word.isalpha() and word.lower() not in stop_words:
                skills.append(word)
    return skills

def extract_certifications(sentences):
    certifications = []
    for sentence in sentences:
        if "certified" in sentence.lower() or "certification" in sentence.lower():
            certifications.append(sentence)
    return certifications

def extract_languages(sentences):
    languages = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        for word, pos in pos_tag(words):
            if pos == 'NNP' and word.lower() not in stopwords.words('english'):
                languages.append(word)
    return languages

def analyze_resume(resume_text):
    sentences = parse_resume(resume_text)
    contact_info = extract_contact_info(sentences)
    education = extract_education(sentences)
    experience = extract_experience(sentences)
    skills = extract_skills(sentences)
    certifications = extract_certifications(sentences)
    languages = extract_languages(sentences)

    return {
        "contact_info": contact_info,
        "education": education,
        "experience": experience,
        "skills": skills,
        "certifications": certifications,
        "languages": languages,
    }

def match_job(resume_data, job_description):
    # Example matching logic
    score = 0
    for skill in resume_data["skills"]:
        if skill in job_description:
            score += 1
    return score

if __name__ == "__main__":
    sample_resume = """John Doe
    Email: john.doe@example.com
    Phone: 123-456-7890
    Education:
    - Bachelor of Science in Computer Science, Example University
    Work Experience:
    - Software Engineer at Tech Company
    Skills:
    - Python, Machine Learning, NLP
    """
    analysis = analyze_resume(sample_resume)
    print(analysis)
    job_description = "We are looking for a Python developer with experience in machine learning and NLP"