important_sections = ['education', 'experience', 'skills', 'projects', 'certifications']
action_verbs = ['developed', 'created', 'designed', 'managed', 'implemented', 'led', 'built']
tech_keywords = ['python', 'flask', 'react', 'aws', 'sql', 'html', 'css', 'machine learning', 'git']

def analyze_resume(text):
    text = text.lower()
    score = 0
    feedback = []

    # Check sections
    for section in important_sections:
        if section in text:
            score += 10
        else:
            feedback.append(f"Missing section: {section.title()}")

    # Action verbs
    found_actions = [word for word in action_verbs if word in text]
    score += len(found_actions) * 2
    if len(found_actions) < 3:
        feedback.append("Add more action verbs like developed, managed, etc.")

    # Tech keywords
    found_tech = [tech for tech in tech_keywords if tech in text]
    score += len(found_tech) * 3
    if len(found_tech) < 5:
        feedback.append("Include more technical keywords (Python, Flask, AWS, etc.)")

    # Cap score at 100
    score = min(score, 100)

    return score, feedback
