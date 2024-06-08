from flask import Flask, request, jsonify
from resume_parser import analyze_resume

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    resume_text = request.form['resume_text']
    analysis = analyze_resume(resume_text)
    return jsonify(analysis)

if __name__ == "__main__":
    app.run(debug=True)
