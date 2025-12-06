\# Secure Coding Review — CodeAlpha Task 3



\## Vulnerabilities Found

\### 1. SQL Injection

\- Issue: Query is built using string formatting.

\- Impact: Attacker can manipulate query and bypass login.

\- Fix: Use parameterized queries.



\### 2. Hardcoded Credentials

\- Issue: Sensitive values exposed.



\### 3. Missing Input Validation

\- Issue: No sanitization of input values.



---



\## Improvements Made in secure\_code.py

✔ Parameterized queries  

✔ Removed hardcoding  

✔ Added secure handling  



---



\## Tools Used

\- Python

\- SQLite



