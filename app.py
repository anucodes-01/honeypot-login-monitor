from flask import Flask, render_template, request
from datetime import datetime
import csv
import time

app = Flask(__name__)

# Route to display fake login page
@app.route("/")
def login_page():
    return render_template("login.html")


# Route to capture login attempts
@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.now()

    print("IP:", ip_address)
    print("Username:", username)
    print("Password:", password)
    print("Browser:", user_agent)
    print("Time:", timestamp)

    # Save attack data to CSV file
    with open("attack_logs.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([ip_address, username, password, timestamp, user_agent])

    # Small delay to simulate real authentication
    time.sleep(2)

    return "Invalid username or password"


if __name__ == "__main__":
    app.run(debug=True)