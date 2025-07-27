# 🔍 InternIntelligence-SecureCodeReview

### 📁 Virtual Internship Task – Cyber Security  
**Task 5: Secure Code Review**  
Completed as part of my internship at **Intern Intelligence** 🎉  

---

## 🚀 Overview

This repository contains the secure code review project completed for Task 5 during the **Intern Intelligence Cyber Security Virtual Internship**.

The objective was to analyze a Python script for security vulnerabilities and provide improvement recommendations.

🗓️ **Completed on:** July 27, 2025, at 09:28 PM PKT

---

## 📝 Codebase Reviewed

**File Reviewed:** `sample_app.py`  
**Description:** A basic Python script that accepts user input and checks for an "admin" role using a hardcoded password.

---

## ⚠️ Security Vulnerabilities Identified

1. **Improper Input Validation**  
   - Uses `input()` without any sanitization.  
   - Risks of **code injection** or **unexpected behavior**.

2. **Insecure Data Handling**  
   - Password `"1234"` is hardcoded and printed directly.  
   - Exposes sensitive data.

3. **Poor Authentication Mechanism**  
   - Lacks secure password hashing.  
   - No session or token management.

---

## 🌟 Recommendations

- ✅ Sanitize all user inputs using validation libraries (e.g., `re`, `pydantic`).
- 🔐 Use secure password hashing methods (e.g., `bcrypt`, `passlib`).
- 🌐 Implement secure authentication and session management using frameworks like **Flask**, **FastAPI**, or **Django**.

---

## 🛠️ Tools Used

- Manual code inspection (beginner-friendly approach)
- Optional extensions:
  - [SonarQube](https://www.sonarsource.com/products/sonarqube/)
  - GitHub Code Scanning

---

## 📬 Submission Details

- 🔖 Internship Task: **Intern Intelligence – Task 5**
- 🆔 Unique Submission ID: `p4vbalKvQc7qRpngB9F4`
- 📅 Date: **July 27, 2025**
- 🔗 Repository: [GitHub Repo](https://github.com/Iqra-Junejo/InternIntelligence-SecureCodeReview)

---

## 📧 Contact

- 🏢 **Organization:** Intern Intelligence  
- 📩 **Email:** hr.interintelligence@gmail.com  
- 🌐 **Website:** [internintelligence.org](https://internintelligence.org)
