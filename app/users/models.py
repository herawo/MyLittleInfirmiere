import hashlib
from passlib.apps import custom_app_context as pwd_context

from flask import render_template
from flask_mail import Message

from app import db, mail


# TODO: Revoir le modèle, ce n'est qu'une base de départ
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    firstname = db.Column(db.Unicode)
    lastname = db.Column(db.Unicode)
    admin = db.Column(db.Boolean, default=False)

    def register(self):
        pass

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def update_password(self, newpassword):
        self.password = pwd_context.encrypt(newpassword)

    def generate_token(self):
        h = hashlib.sha1()
        h.update('{0}{1}{2}'.format(self.id, self.email, self.password)
                            .encode())
        return h.hexdigest()

    def verify_token(self, token):
        return token == self.generate_token()

    def password_reset(self, reset_link):
        # msg = Message("Password reset", recipients=['ludovic@rwigo.com'])
        msg = Message("Récupération de mot de passe", recipients=[self.email])
        msg.body = render_template("mails/password_reset.txt",
                                   firstname=self.firstname,
                                   reset_link=reset_link)
        msg.html = render_template("mails/password_reset.html",
                                   firstname=self.firstname,
                                   reset_link=reset_link)

        mail.send(msg)

    def assign(self, patient_id):
        pass
