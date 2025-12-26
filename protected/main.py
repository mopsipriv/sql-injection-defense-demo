from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import logging

app = Flask(__name__)

logging.basicConfig(
    filename="info.log",
    format="%(asctime)s %(message)s",
    level=logging.WARNING
)

@app.route("/", methods=["GET", "POST"])
def login():
    conn = get_db_connection()
    ip = request.remote_addr

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        username_l = username.lower()
        password_l = password.lower()

        suspicious_patterns = ["--", "union", "' or"]

        for pattern in suspicious_patterns:
            if pattern in username_l or pattern in password_l:
                logging.warning(
                    f"Possible SQLi attempt from {ip}: {username} | {password}")
                return render_template("login.html",error="Suspicious input detected")

        query = "SELECT * FROM initials WHERE username = ? AND password = ?"
        result = conn.execute(query, (username, password)).fetchone()

        if result:
            return redirect(url_for("welcome"))
        else:
            return render_template("login.html",error="Invalid username or password" )

    return render_template("login.html")


def get_db_connection():
    return sqlite3.connect("initials.db")


@app.route("/welcome")
def welcome():
    return "Welcome!"


if __name__ == "__main__":
    app.run(debug=True)
