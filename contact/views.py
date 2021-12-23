from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, TextField
from wtforms.validators import DataRequired, Length, Email, email_validator

contact_blueprint = Blueprint("contact_blueprint", __name__,
                              template_folder="pages/",
                              static_folder="static")


class ContactForm(FlaskForm):
    name = StringField(
        "Name of Student",
        [DataRequired()]
    )
    email = EmailField(
        "Email",
        [DataRequired()]
    )
    body = StringField(
        "Message",
        [DataRequired()]
    )

    submit = SubmitField("Submit")


@contact_blueprint.route("/contact")
def index():
    form = ContactForm()

    return render_template("contact/contact.html", form=form)


# https://hackersandslackers.com/flask-wtforms-forms/