# Student Expense Tracker (Flask)

A beginner-friendly Flask web app to record and review student expenses. Data is stored in a CSV file instead of a database, making it easy to run locally and understand how the pieces fit together.

## Features
- Basic login/logout gate to protect the tracker
- Add expenses with amount, category, and note
- View all expenses in a table
- Delete an expense entry
- Monthly summary via a simple form (expects `YYYY-MM`)

## Tech Stack
- Python 3, Flask
- HTML + CSS (vanilla)
- CSV file storage (no database)

## Project Structure
```
expense_web_app/
├─ app.py              # Flask app routes and CSV handling
├─ expenses.csv        # Data file (created on first run)
├─ templates/
│  ├─ home.html        # Main UI for add/list/delete/summary
│  └─ login.html       # Login page
└─ static_chart.png    # Sample image (optional)
```

## How to Run Locally
1) Install Python 3.10+.
2) Install dependencies:
```bash
pip install flask
```
3) Start the server:
```bash
python app.py
```
4) Open http://localhost:5000

## Default Login
- Username: admin
- Password: 1234

## Agile Development Notes
- Built in small sprints, each adding a single feature (add, list, delete, summary, auth).
- Frequent testing after each change to keep the app stable.

## Future Enhancements
- Switch CSV to a real database (SQLite/PostgreSQL) for reliability
- Input validation and friendlier error messages
- Editable categories and inline edits for notes
- Simple charts for category/month breakdowns
- Proper user accounts instead of a hard-coded login

## Learning Outcomes
- How Flask routes, templates, and forms work together
- Reading/writing CSV files for quick persistence
- Structuring a small web app and incrementally improving it
- Practicing Agile-style iterations on a tiny project
