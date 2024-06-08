from flask import Flask, request, jsonify , render_template
from resume_parser import analyze_resume, match_job
from schemas import resume_schema, analysis_schema, v

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

@app.route("/match", methods=["POST"])
def match():
    if not v.validate(request.json, analysis_schema):
        return jsonify(v.errors), 400
    
    resume_data = request.json
    job_description = request.json["job_description"]
    score = match_job(resume_data, job_description)
    
    return jsonify({"score": score})

if __name__ == "__main__":
    app.run(debug=True)
