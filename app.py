from database import create_database, insert_log
from flask import Flask, render_template, request
from datetime import datetime
from detection import classify_attack, blocked_ips

import time

app = Flask(__name__)

create_database()


# Route to display fake login page
@app.route("/")
def login_page():
    return render_template("login.html")


# Route to capture login attempts
@app.route("/login", methods=["POST"])
def login():

    ip_address = request.remote_addr

    # 🚨 BLOCK CHECK (BEFORE EVERYTHING)
    if ip_address in blocked_ips:
        print("⛔ BLOCKED IP HIT AGAIN:", ip_address)
        return "Access Denied - Suspicious Activity"

    username = request.form["username"]
    password = request.form["password"]

    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.now()

    print("\n--- NEW ATTEMPT ---")
    print("IP:", ip_address)
    print("Username:", username)
    print("Password:", password)
    print("Browser:", user_agent)
    print("Time:", timestamp)

    # 🔍 Detection FIRST
    risk, attack_type = classify_attack(ip_address, username, str(timestamp))

    print("Risk Level:", risk)
    print("Attack Type:", attack_type)

    # 🚨 IMPROVED ALERT (only change here)
    if risk == "HIGH":
        print(f"🚨 ALERT: {attack_type} detected from IP {ip_address} (Risk: {risk})")

    # 🚨 IMMEDIATE BLOCK CHECK AFTER DETECTION
    if ip_address in blocked_ips:
        print("⛔ BLOCK APPLIED IMMEDIATELY:", ip_address)
        return "Access Denied - Suspicious Activity"

    # Save log
    insert_log(ip_address, username, password, timestamp, user_agent, risk, attack_type)

    return "Invalid username or password"


if __name__ == "__main__":
    app.run(debug=True)