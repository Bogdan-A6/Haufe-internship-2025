from ollama import chat
from ollama import ChatResponse
import requests  
import json


def putQuestion(mesaj):
    #question = str("You are a code reviewer and i want to tell me everythin wrong with this code: ") + str(test3.test())
    question = "Please perform a comprehensive code review of the following source code. Analyze the code for: Code Quality & Best Practices: Code structure and organization Adherence to language-specific conventions and style guidelines Code readability and maintainability Proper naming conventions for variables, functions, and classes Code duplication and opportunities for refactoring Potential Issues:Syntax errors and logical bugs Performance bottlenecks and inefficient algorithms Memory leaks or resource management issues Security vulnerabilities (SQL injection, XSS, input validation, etc.) Error handling and edge cases Race conditions or concurrency problems Design & Architecture: Design pattern implementation Code modularity and separation of concerns Function/method length and complexity Proper use of data structures Documentation: Code comments and documentation quality Self-documenting code practices Please provide: 1. A summary of overall code quality 2. Specific issues found with line numbers and explanations 3. Suggestions for improvement with code examples where appropriate 4. Any security concerns identified 5. Performance optimization recommendations. In the end i want you to redo the code and name the section Redone code Here's the code to review:" + str(mesaj)
    
    data = {
        "model": "qwen2.5:0.5b", 
        "messages": [{"role": "user", "content": question}],
        "stream": False,
    }
    url = "http://localhost:11434/api/chat"

    try:
        response = requests.post(url, data=json.dumps(data))  
        response.raise_for_status()  
        response_json = json.loads(response.text)

        ai_reply = response_json["message"]["content"]
        return ai_reply

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    
    
    
    