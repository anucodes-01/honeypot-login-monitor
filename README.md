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