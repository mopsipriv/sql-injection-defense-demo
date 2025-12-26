# 🛡️ SQL Injection Defense Demo (Educational Project)

## ⚠️ Educational Disclaimer
This repository is created **for educational purposes only**.  
It demonstrates **defensive programming techniques** used to protect web applications from SQL Injection vulnerabilities.

The goal of this project is **not hacking**, but understanding:
- How SQL Injection works
- Why insecure code is dangerous
- How to properly defend backend systems using industry standards

No real user data is used in this project. All examples are intentionally simplified for learning purposes.

---

## 📋 Project Overview
This is a Flask-based web application that simulates a simple user authentication system.

The project is intentionally split into two versions to demonstrate the **security lifecycle**:
- **Vulnerable version** — shows how SQL Injection attacks work
- **Protected version** — shows how the same attacks are prevented using secure coding practices

This **Before vs. After** approach highlights the impact of proper backend design.

---

## ❌ The Problem
Using string concatenation in SQL queries allows attackers to bypass authentication with malicious inputs such as:
' OR 1=1 --
admin' --

When user input is directly concatenated into SQL queries, the database interprets attacker-controlled input as executable SQL logic.

---


## 🚀 Key Security Features Implemented

### 1️⃣ SQL Injection Prevention (Parameterized Queries)

**Vulnerable approach (unsafe):**
python
# ❌ DANGEROUS: String concatenation
query = "SELECT * FROM users WHERE username = '" + username + "'"

# ✅ SECURE: Parameterized query
query = "SELECT * FROM users WHERE username = ?"
db.execute(query, (username,))

2️⃣ Suspicious Input Detection (WAF-like Logic)

As an additional defensive layer, the application inspects user input for common SQL Injection patterns such as:

' OR

--

UNION SELECT

This mechanism does not replace prepared statements, but helps with:

- Early detection of malicious behavior

- Security logging

- Application visibility

3️⃣ Security Logging & Monitoring

All detected suspicious activity is logged, simulating real-world Application Security (AppSec) monitoring:

- Timestamp of the event

- Client IP address

- Suspicious input provided

## 🧭 Project Structure
sql-injection-demo/
├── vulnerable/         # Intentionally unsafe implementation
│   ├── main.py
│   └── templates/
├── protected/          # Secure implementation
│   ├── main.py
│   └── templates/
├── init_db.py          # Database initialization script
├── requirements.txt    # Dependencies
└── README.md           # Documentation

## 🛠️ Installation & Setup

cd sql-injection-defense-demo


Install dependencies:

pip install flask


Initialize the database:

python init_db.py


Run the application:

python main.py

##🎓 Learning Outcomes
Through this project, I gained hands-on experience in:

- Identifying and reproducing SQL Injection vulnerabilities

- Implementing parameterized queries to prevent injection attacks

- Logging and monitoring suspicious activity

- Adopting a defensive security mindset during backend development