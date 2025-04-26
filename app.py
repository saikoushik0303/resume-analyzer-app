from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Your existing config
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Temporary user storage (demo only — use database in production)
users = {}

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        if username in users:
            flash('Username already exists.')
        else:
            users[username] = password
            flash('Registered successfully! Please login.')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        stored_password = users.get(username)

        if stored_password and check_password_hash(stored_password, password):
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

from resume_parser import extract_text
from ats_checker import analyze_resume
from grammar_checker import checkgrammar
from jd_matching import match_resume_with_jd
import os

@app.route('/ats-score', methods=['GET', 'POST'])
def ats_score():
    if 'user' not in session:
        return redirect(url_for('login'))

    extracted_text = ""
    score = None
    suggestions = []

    if request.method == 'POST':
        file = request.files['resume']
        if file and file.filename.endswith('.pdf'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            extracted_text = extract_text(filepath)
            score, suggestions = analyze_resume(extracted_text)

    return render_template('ats_score.html', text=extracted_text, score=score, suggestions=suggestions)


@app.route('/jd-matching', methods=['GET', 'POST'])
def jd_matching():
    if 'user' not in session:
        return redirect(url_for('login'))

    extracted_text = ""
    jd_match = None

    if request.method == 'POST':
        file = request.files['resume']
        job_description = request.form.get('job_description')

        if file and file.filename.endswith('.pdf') and job_description:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            extracted_text = extract_text(filepath)
            jd_match = match_resume_with_jd(extracted_text, job_description)

    return render_template('jd_matching.html', text=extracted_text, jd_match=jd_match)


@app.route('/resume-fix', methods=['GET', 'POST'])
def resume_fix():
    if 'user' not in session:
        return redirect(url_for('login'))

    extracted_text = ""
    grammar_suggestions = []

    if request.method == 'POST':
        file = request.files['resume']
        if file and file.filename.endswith('.pdf'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            extracted_text = extract_text(filepath)
            grammar_suggestions = checkgrammar(extracted_text)

    return render_template('resume_fix.html', text=extracted_text, grammar=grammar_suggestions)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/')
def home():
    return redirect(url_for('login'))


if __name__=='__main__':
    app.run(debug=True)
