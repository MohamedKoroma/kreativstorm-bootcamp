## 🗂️ Projects

- [Burp Suite Web Vulnerability Scan Demo](./burp-suite-scan/burp_scan_report.md)
- [Python IP Blocker Script](./python-ip-blocker/README.md)

---

## 🐍 Python Project – Failed Login IP Blocker

This script analyzes SSH logs and identifies repeated failed login attempts from the same IP address.

---

## 🛠️ How It Works

- Reads `log.txt` line by line  
- Matches lines with "Failed password from"  
- Tracks failed attempts per IP  
- Blocks IPs with 3+ failures by writing to `blocked_ips.txt`  

---

## 📁 Files

- `ip_blocker.py` – The core script  
- `log.txt` – Sample input log file  
- `blocked_ips.txt` – Output of blocked IPs  

---

## 🧪 Sample Output

**log.txt**:
```
Jan 01 10:01:11 sshd[1999]: Failed password from 192.168.1.10  
Jan 01 10:01:15 sshd[1999]: Failed password from 192.168.1.11  
Jan 01 10:01:17 sshd[1999]: Failed password from 192.168.1.10  
Jan 01 10:01:21 sshd[1999]: Failed password from 192.168.1.10  
```

**blocked_ips.txt**:
```
192.168.1.10
```
---
