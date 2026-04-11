from collections import defaultdict
from datetime import datetime, timedelta

# Store blocked IPs
blocked_ips = set()

# Track attempts per IP
ip_attempts = defaultdict(list)


def detect_bruteforce(ip, timestamp):
    current_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")

    ip_attempts[ip].append(current_time)

    # Keep last 2 minutes (so manual testing works)
    ip_attempts[ip] = [
        t for t in ip_attempts[ip]
        if current_time - t < timedelta(minutes=2)
    ]

    # Trigger brute force after 5 attempts
    return len(ip_attempts[ip]) >= 5


def detect_suspicious_username(username):
    suspicious = ["admin", "root", "administrator", "test"]
    return username.lower() in suspicious


def block_ip(ip):
    blocked_ips.add(ip)


def classify_attack(ip, username, timestamp):
    brute = detect_bruteforce(ip, timestamp)
    suspicious = detect_suspicious_username(username)

    attack_type = "Normal"

    # 🎯 SIMPLE + RELIABLE LOGIC
    if brute and suspicious:
        risk = "HIGH"
        attack_type = "Brute Force"

    elif brute:
        risk = "MEDIUM"
        attack_type = "Brute Force"

    elif suspicious:
        risk = "LOW"
        attack_type = "Suspicious Username"

    else:
        risk = "LOW"

    # 🚫 BLOCK HIGH RISK
    if risk == "HIGH":
        block_ip(ip)

    return risk, attack_type