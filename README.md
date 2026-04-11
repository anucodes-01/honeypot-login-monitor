# Honeypot Login Monitoring System

Cybersecurity mini project that simulates a login honeypot to capture attacker behavior.

## Features

- Fake admin login portal
- Captures login attempts
- Stores attacker data
- Logs attacks in SQLite database

## Setup

1. Clone the repository

git clone <repo_link>

2. Install dependencies

pip install -r requirements.txt

3. Run the server

python app.py

4. Open browser

http://127.0.0.1:5000

## Database

The application automatically creates:

honeypot.db

Table:

attempts

Columns:

id  
ip_address  
username  
password  
timestamp  
user_agent

Attack Detection and Security Module

Overview  
This module extends the honeypot system by introducing real-time attack detection, risk classification, and automated response mechanisms. It analyzes login behavior to identify malicious activity and applies appropriate security actions.

Detection Logic

The system evaluates each login attempt based on multiple behavioral indicators:

- Number of login attempts from the same IP within a short time window  
- Use of commonly targeted usernames  
- Frequency and pattern of requests  

Based on these factors, the system classifies activity into different categories.

Attack Types

The following attack types are identified:

- Normal: No suspicious behavior detected  
- Suspicious Username: Use of commonly targeted usernames such as "admin", "root", "administrator", or "test"  
- Brute Force: Multiple repeated login attempts from the same IP within a short duration  
- Automated Attack: Rapid and excessive requests indicating scripted or bot activity  

Risk Classification

Each login attempt is assigned a risk level based on severity:

- LOW: Minimal or no suspicious indicators  
- MEDIUM: Moderate suspicious activity detected  
- HIGH: Strong indicators of malicious behavior  

Risk levels are determined using a scoring mechanism derived from detection rules.

Brute Force Detection

- Tracks login attempts per IP address  
- Maintains a rolling time window of one minute  
- Flags brute force activity when attempts exceed a defined threshold  

Suspicious Username Detection

- Checks for predefined high-risk usernames  
- Helps identify targeted intrusion attempts  

Rapid Request Detection

- Detects high-frequency login attempts  
- Indicates possible automated or scripted attacks  

IP Blocking Mechanism

- IP addresses associated with HIGH risk activity are automatically blocked  
- Blocked IPs are stored in an in-memory blocklist  
- All subsequent requests from blocked IPs are denied  

Access Control

When a blocked IP attempts to interact with the system, access is denied with the following response:

Access Denied - Suspicious Activity

Alert System

The system generates real-time alerts in the server console when high-risk activity is detected.  
These alerts include:

- IP address  
- Detected attack type  
- Assigned risk level  

System Workflow

1. User submits login credentials  
2. System captures request metadata:
   - IP address  
   - Username  
   - Timestamp  
   - User agent  

3. Detection module evaluates the request  
4. Risk level and attack type are assigned  
5. If risk is HIGH:
   - Alert is triggered  
   - IP is blocked  

6. Attempt details are stored in the database  

Files Involved

detection.py  
- Contains detection algorithms  
- Implements risk classification logic  
- Manages IP blocking  

app.py  
- Integrates detection logic with Flask application  
- Handles request processing and response  
- Logs attack details to the database  

Outcome

- Enables identification of brute force and automated attacks  
- Prevents repeated malicious access through IP blocking  
- Enhances the realism of the honeypot system  
- Provides structured data for further analysis  

Contribution

Member 3 – Attack Detection and Security Logic

- Designed and implemented detection algorithms  
- Developed risk classification system  
- Implemented IP blocking mechanism  
- Integrated detection logic with application backend
