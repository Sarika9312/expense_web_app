
from flask import Flask, render_template, request, redirect, session

import csv
from datetime import datetime

app = Flask(__name__)
app.secret_key = "super_secret_key_change_later"

FILE_NAME = "expenses.csv"


def init_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "date", "amount", "category", "note"])

    except FileExistsError:
        pass

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # simple hard-coded login
        if username == "admin" and password == "1234":
            session["user"] = username
            return redirect("/")
        else:
            return "<h3>Invalid credentials</h3><a href='/login'>Try again</a>"

    return render_template("login.html")

@app.route("/")
def home():
    if "user" not in session:
        return redirect("/login")

    init_file()
    expenses = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            expenses.append(row)

    return render_template("home.html", expenses=expenses)


@app.route("/add", methods=["POST"])
def add():
    amount = request.form["amount"]
    category = request.form["category"]
    note = request.form["note"]

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)
            rows = list(reader)
            new_id = len(rows) + 1
    except FileNotFoundError:
        new_id = 1

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            new_id,
            datetime.now().strftime("%Y-%m-%d"),
            amount,
            category,
            note
        ])

    return redirect("/")



@app.route("/summary", methods=["POST"])
def summary():
    month = request.form["month"]
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0].startswith(month):
                total += float(row[1])

    return f"<h2>Total expenses for {month}: ₹{total}</h2><a href='/'>Back</a>"
@app.route("/delete/<id>")
def delete(id):
    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    new_rows = [rows[0]]  # header only

    for row in rows[1:]:
        if row[0] != id:
            new_rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(new_rows)

    return redirect("/")
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
