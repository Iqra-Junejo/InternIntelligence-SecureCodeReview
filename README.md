# InternIntelligence-SecureCodeReview
Virtual Internship Task of Cyber Security
Secure Code Review for Intern Intelligence Internship 🎉
Overview 🚀
This repository contains a secure code review project completed as part of the Intern Intelligence internship (Task 5). The goal is to review a sample codebase for security vulnerabilities and provide recommendations for improvement. 💻🔒
Codebase Reviewed 📝

File: sample_app.py
Description: A simple Python script that takes user input and checks for an "admin" role with a hardcoded password. 🐍

Security Vulnerabilities Identified ⚠️

Improper Input Validation: The script uses input() without sanitizing, risking injection attacks. 💉
Insecure Data Handling: The password "1234" is hardcoded and printed, exposing it. 🔓
Poor Authentication: Basic username check lacks secure password hashing or session management. 🔐

Recommendations 🌟

Validate and sanitize user input using a library like re or a validation framework. ✅
Use a secure hashing library (e.g., bcrypt) to store and verify passwords. 🔐
Implement proper authentication with session management (e.g., using Flask or Django). 🌐

Tools Used 🛠️

Manual review (beginner-friendly approach).
Can be extended with SonarQube or GitHub’s code scanning for automation. 🤖





