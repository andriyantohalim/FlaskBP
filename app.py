from flask import Flask, render_template
from general.views import general_blueprint
from registration.views import registration_blueprint
from feedback.views import feedback_blueprint


app = Flask(__name__)
app.register_blueprint(general_blueprint)
app.register_blueprint(registration_blueprint)
app.register_blueprint(feedback_blueprint)


def main():
    app.run(debug=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# https://realpython.com/flask-blueprint/
# https://stackoverflow.com/questions/7974771/flask-blueprint-template-folder

