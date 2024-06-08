from flask import Flask, request, jsonify
from resume_parser import analyze_resume
from schemas import resume_schema, analysis_schema, v

app = Flask(__name__)

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
