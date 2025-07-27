# 🔐 Secure Code Review – Intern Intelligence Internship (Task 5)

## 🎯 Overview
This repository contains a **secure code review project** completed as part of the **Intern Intelligence Virtual Internship – Cyber Security Track (Task 5)**.  
The goal was to review a sample Python codebase for security vulnerabilities and suggest improvements.  
🗓️ **Completed on:** July 27, 2025 at 09:39 PM PKT

---

## 📝 Codebase Reviewed

- **File:** `sample_app.py`  
- **Description:** A simple Python script that accepts user input and checks for an `"admin"` role. The updated version replaces hardcoded credentials with a secure authentication mechanism using hashing.

---

## ⚠️ Security Vulnerabilities Identified

1. **Improper Input Validation:**  
   The original script used `input()` without sanitizing, leading to potential injection risks.  
   ✔️ **Fix:** `.strip()` added; further validation recommended.

2. **Insecure Data Handling:**  
   Hardcoded password `"1234"` was printed, exposing credentials.  
   ✔️ **Fix:** Replaced with `sha256` hashing and removed print statements.

3. **Poor Authentication:**  
   Original login lacked hashing or session security.  
   ✔️ **Fix:** Added hashing for secure credential handling. Session management is still a recommended next step.

---

## 🌟 Recommendations

- ✅ Use regex or input validation libraries for robust user input handling.
- 🔐 Replace `sha256` with a more secure hashing algorithm like **bcrypt** for production use.
- 🌐 Implement **session management** using frameworks like **Flask** or **Django**.
- 📁 Store hashed passwords and salt persistently in a database or file, rather than hardcoding.

---

## 🛠️ Tools Used

- Manual code review (beginner-friendly approach)
- Python’s `hashlib.sha256` for hashing (simulation)
- Suggestions to extend with:
  - ✅ `SonarQube`
  - ✅ GitHub Advanced Security Code Scanning

---

## 📬 Submission Details

- 🔖 Internship Task: **Intern Intelligence – Task 5**
- 🆔 Unique Submission ID: `p4vbalKvQc7qRpngB9F4`
- 📅 Date: **July 27, 2025**
- 🔗 Repository: https://github.com/Iqra-Junejo/InternIntelligence-SecureCodeReview
- **Date of Completion:** July 27, 2025

---

## 📧 Contact

- **Organization:** Intern Intelligence  
- **Email:** hr.interintelligence@gmail.com  
- **Website:** (http://internintelligence.org)

---
