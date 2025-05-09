from collections import defaultdict

log_file = "log.txt"
block_file = "blocked_ips.txt"
fail_threshold = 3

failures = defaultdict(int)

with open(log_file, 'r') as f:
    for line in f:
        if "Failed password from" in line:
            parts = line.strip().split()
            ip = parts[-1]
            failures[ip] += 1

with open(block_file, 'w') as f:
    for ip, count in failures.items():
        if count >= fail_threshold:
            f.write(f"{ip}\n")

print("Suspicious IPs saved to blocked_ips.txt")
