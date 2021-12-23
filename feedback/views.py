import sqlite3

from flask import Blueprint, render_template, request
import feedback.model.model as mdl

feedback_blueprint = Blueprint("feedback_blueprint", __name__,
                               template_folder="pages",
                               static_folder="static")


@feedback_blueprint.route("/feedback")
def index():
    return render_template("feedback/feedback.html")


@feedback_blueprint.route("/submit_feedback", methods=["GET", "POST"])
def submit_feedback():
    mdl.create_db()

    conn = sqlite3.connect('feedback.db')
    msg = "Nothing happened"

    if request.method == 'POST':
        try:
            email = request.form["email"]
            comment = request.form["comment"]

            cur = conn.cursor()
            cur.execute("INSERT INTO feedback (email, comment) VALUES (?, ?)", (email, comment))

            conn.commit()
            msg = "Record successfully updated"
        except sqlite3.Error:
            conn.rollback()
            msg = "Error in insert operation"

        finally:
            return render_template("feedback/result.html", msg=msg)
            conn.close()


@feedback_blueprint.route("/list_feedback")
def list_feedback():
    mdl.create_db()

    conn = sqlite3.connect("feedback.db")
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute("SELECT * FROM feedback")

    rows = cur.fetchall()
    return render_template("feedback/list_feedback.html", rows=rows)
