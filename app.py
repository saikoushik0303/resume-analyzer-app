from flask import Flask, render_template, request
import os
from resume_parser import extract_text
from ats_checker import analyze_resume
from grammar_checker import  checkgrammar

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = ""
    score = None
    suggestions = []
    grammar_suggestions=[]

    if request.method == 'POST':
        file = request.files['resume']
        if file and file.filename.endswith('.pdf'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            extracted_text = extract_text(filepath)
            score, suggestions = analyze_resume(extracted_text)
            grammar_suggestions = checkgrammar(extracted_text)


    return render_template('index.html', text=extracted_text, score=score, suggestions=suggestions, grammar=grammar_suggestions)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
