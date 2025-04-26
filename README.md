
# 📄 Resume Analyzer Web App

A smart, web-based application to help you analyze your resume!  
It provides **ATS Score checking**, **Job Description Matching**, and **Resume Grammar Fixing** — helping you boost your chances of getting shortlisted.
## ✨ Features

- 🔒 **User Authentication** (Register/Login)
- 📄 **ATS Score Checker**  
  Upload your resume and get an ATS (Applicant Tracking System) compatibility score along with improvement suggestions.
- 📑 **Job Description Matching**  
  Match your resume against a specific Job Description to see how well you fit.
- 📝 **Resume Grammar Fixer**  
  Identify and fix grammar mistakes in your resume text.
- 📂 **Secure File Uploads** (PDF resumes)
- ⚡ **Dashboard Interface** for easy navigation
- 🎨 **Modern UI** with Tailwind CSS
## 🚀 Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, Tailwind CSS
- **Libraries:** 
  - `Werkzeug` (for password hashing)
  - `Flask-Session` (for login sessions)
  - `Chart.js` (for graphical ATS score visualization, if used)
  - `PyMuPDF` or `pdfminer` (for PDF text extraction)
- **Other:** Resume Parsing, NLP for grammar and JD matching
## 📂 Project Structure

├── app.py                # Main Flask app
├── templates/            # HTML templates (login, register, dashboard, ats_score, jd_matching, resume_fix)
├── static/               # Static files (CSS, JS, images if any)
├── uploads/              # Uploaded resumes
├── resume_parser.py      # Extract text from PDF resumes
├── ats_checker.py        # Analyze resume and provide ATS score
├── grammar_checker.py    # Check and suggest grammar fixes
├── jd_matching.py        # Match resume content with job descriptions
└── README.md             # Project documentation

## ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/resume-analyzer-webapp.git
cd resume-analyzer-webapp
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
python app.py
```

The app will run at:  
🌐 http://127.0.0.1:5000/

---

## 🛡️ Important Notes

- This project uses **in-memory user storage** (`users = {}`) for demo purposes.  
  🔥 In production, you should integrate a **database** (like SQLite, PostgreSQL).
- Always set a strong `app.secret_key`.
- File uploads are saved inside the `/uploads` folder.
- Make sure to validate user inputs and file uploads securely if deploying publicly.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open a pull request or submit an issue.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
