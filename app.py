from flask import Flask
from general.views import general_blueprint
from registration.views import registration_blueprint
from feedback.views import feedback_blueprint
from contact.views import contact_blueprint

app = Flask(__name__)

# for FlaskForm
app.secret_key = 'development key'

app.register_blueprint(general_blueprint)
app.register_blueprint(registration_blueprint)
app.register_blueprint(feedback_blueprint)
app.register_blueprint(contact_blueprint)



def main():
    app.run(debug=True)
    app.config.from_object('config.Config')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# https://realpython.com/flask-blueprint/
# https://stackoverflow.com/questions/7974771/flask-blueprint-template-folder

