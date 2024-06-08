import spacy

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

def parse_resume(resume_text):
    # Process the text with SpaCy
    doc = nlp(resume_text)
    return doc

def extract_contact_info(doc):
    contact_info = {}
    for entity in doc.ents:
        if entity.label_ in ["PERSON", "EMAIL", "PHONE"]:
            contact_info[entity.label_] = entity.text
    return contact_info

def extract_education(doc):
    education = []
    for entity in doc.ents:
        if entity.label_ == "ORG" and "university" in entity.text.lower():
            education.append(entity.text)
    return education

def extract_experience(doc):
    experience = []
    for sent in doc.sents:
        if "experience" in sent.text.lower():
            experience.append(sent.text)
    return experience

def extract_skills(doc):
    skills = []
    for token in doc:
        if token.pos_ == "NOUN":
            skills.append(token.text)
    return skills

def analyze_resume(resume_text):
    doc = parse_resume(resume_text)
    contact_info = extract_contact_info(doc)
    education = extract_education(doc)
    experience = extract_experience(doc)
    skills = extract_skills(doc)

    return {
        "contact_info": contact_info,
        "education": education,
        "experience": experience,
        "skills": skills,
    }

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
# This script defines a set of functions for analyzing resumes. It uses the SpaCy library to process the resume text and extract contact information, education, experience, and skills. The analyze_resume function orchestrates the analysis process by calling the individual extraction functions and returning the results as a dictionary.