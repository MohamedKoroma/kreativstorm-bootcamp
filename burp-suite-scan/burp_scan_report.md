# 🔎 Burp Suite Web Vulnerability Scan – Demo Report

**Target**: `http://testphp.vulnweb.com`  
**Tool Used**: Burp Suite Community Edition  
**Scan Type**: Passive & Active Scan  
**Date**: [Insert Date]

---

## 🎯 Objective

To simulate a real-world web application penetration test using Burp Suite and identify common security flaws in a deliberately vulnerable website.

---

## ⚙️ Methodology

1. Configured browser proxy settings to route traffic through Burp.
2. Intercepted and examined HTTP requests/responses.
3. Added the target to Burp's scope.
4. Performed spidering to map out endpoints.
5. Initiated an automated vulnerability scan.
6. Analyzed reported issues and saved relevant screenshots.

---

## 🧪 Sample Findings

| Vulnerability       | Severity | Description                                       |
|---------------------|----------|---------------------------------------------------|
| Reflected XSS       | Medium   | Input not properly sanitized in the response      |
| SQL Injection       | High     | Input used in backend SQL queries without filtering |
| Information Leakage | Low      | Server banner reveals software version info       |

---

## 🖼️ Screenshots

📌 (Upload screenshots like these when ready, or reference future uploads):
- `scope-config.png` – Burp target scope setup
- `scan-results.png` – List of discovered issues
- `issue-detail.png` – Example vulnerability breakdown

---

## ✅ Conclusion

This test exercise demonstrated how to configure and operate Burp Suite for security testing. I gained practical experience identifying vulnerabilities like XSS and SQL Injection, and enhanced my understanding of request analysis, input validation, and secure web development practices.

---

*This project is part of the Kreativstorm Cybersecurity Bootcamp (September 2023).*
