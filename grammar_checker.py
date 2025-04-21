import os
os.environ["JAVA_HOME"] = "C:\\Program Files\\Java\\jdk-24"
os.environ["PATH"] += os.pathsep + "C:\\Program Files\\Java\\jdk-24\\bin"
import  language_tool_python
def checkgrammar(text):
    tool=language_tool_python.LanguageTool('en-US')
    matches=tool.check(text)
    suggestions=[]
    for match in matches:
        suggestions.append(f"✏️ Line {match.context}: {match.message} → Suggestion: {match.replacements}")
    return suggestions