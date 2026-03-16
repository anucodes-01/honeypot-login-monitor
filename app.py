from database import create_database, insert_log
from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__)

create_database()

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

   

    # Small delay to simulate real authentication
    time.sleep(2)

    return "Invalid username or password"


if __name__ == "__main__":
    app.run(debug=True)