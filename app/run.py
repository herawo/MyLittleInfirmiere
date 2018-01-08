#!/usr/bin/env python3

from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
mail = Mail(app)

from app.users.models import UserView
from app.patients.models import PatientView

UserView.register(app, route_base='/users')
PatientView.register(app, route_base='/patients')

if __name__ == '__main__':
    app.run()
