from flask import Flask, request, jsonify
from resume_parser import analyze_resume

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    resume_text = request.json["resume_text"]
    analysis = analyze_resume(resume_text)
    return jsonify(analysis)

if __name__ == "__main__":
    app.run(debug=True)
# This script defines a Flask app that provides an API endpoint for analyzing resumes. The /analyze route accepts a POST request with a JSON payload containing the resume text. It then calls the analyze_resume function from resume-parser.py to extract contact information, education, experience, and skills from the resume text. Finally, it returns the analysis as a JSON response.
