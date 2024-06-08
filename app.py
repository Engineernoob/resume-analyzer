from flask import Flask, request, jsonify, render_template
from resume_parser import analyze_resume
from schemas import resume_schema, analysis_schema, v
import nltk

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if not v.validate(request.json, resume_schema):
        return jsonify(v.errors), 400
    
    resume_text = request.json["resume_text"]
    analysis = analyze_resume(resume_text)
    
    if not v.validate(analysis, analysis_schema):
        return jsonify({'error': 'Invalid analysis output'}), 500

    return jsonify(analysis)

if __name__ == "__main__":
    app.run(debug=True)

