from flask import Blueprint, render_template


registration_blueprint = Blueprint("registration_blueprint", __name__,
                                   template_folder="pages/",
                                   static_folder="static")


@registration_blueprint.route("/registration")
def index():
    return render_template("registration/registration.html")
