from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    conn = get_db_connection()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        query = "SELECT * FROM initials WHERE username = ? AND password = ?"
        result = conn.execute(query, (username, password)).fetchone()

        if result:
            return redirect(url_for("welcome"))
        else:
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


def get_db_connection():
    return sqlite3.connect("initials.db")


@app.route("/welcome")
def welcome():
    return "Welcome!"


if __name__ == "__main__":
    app.run(debug=True)
