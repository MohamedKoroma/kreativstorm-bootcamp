# Burp Suite Web Vulnerability Scan – Demo Report

**Target**: http://testphp.vulnweb.com  
**Tool Used**: Burp Suite Community Edition  
**Scan Type**: Passive & Active Scan  
**Date**: [Insert Date]

---

## 🔍 Objective
To demonstrate the use of Burp Suite for discovering vulnerabilities in a deliberately insecure web application.

---

## ⚙️ Methodology
1. Configured proxy to intercept browser traffic.
2. Added target to scope and initiated crawl.
3. Ran automated scanner and reviewed issues.
4. Documented findings with severity levels.

---

## 📊 Sample Findings

| Issue             | Severity | Description                          |
|------------------|----------|--------------------------------------|
| Reflected XSS     | Medium   | Input reflected without encoding     |
| SQL Injection     | High     | Input directly used in SQL queries   |
| Info Disclosure   | Low      | Server banner reveals version info   |

---

## 🖼️ Screenshots
- `scope-config.png`
- `scan-results.png`
- `issue-detail.png`

---

## ✅ Conclusion
This test demonstrated core concepts of web vulnerability scanning, input validation analysis, and Burp Suite usage within ethical hacking workflows.
