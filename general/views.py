from flask import Blueprint, render_template

general_blueprint = Blueprint("general_blueprint", __name__,
                              template_folder="pages/",
                              static_folder="static")


@general_blueprint.route("/")
def index():
    return render_template("general/index.html")

