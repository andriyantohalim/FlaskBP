from flask import Flask, render_template
from general.controller import general_blueprint
from registration.controller import registration_blueprint
import sqlite3 as sql

app = Flask(__name__)
app.register_blueprint(general_blueprint)
app.register_blueprint(registration_blueprint)


def main():
    app.run(debug=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# https://realpython.com/flask-blueprint/
