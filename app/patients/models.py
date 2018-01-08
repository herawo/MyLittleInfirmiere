from app import db
from app.users.models import User


# TODO: Début de modèle, à revoir
class Patients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.Unicode)
    lastname = db.Column(db.Unicode)
    social_id = db.Column(db.String, unique=True)
    pathology = db.Column(db.string)
    latest_medical_exam = db.Column(db.date)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    # TODO: Assign user devrait peut-être être ici plutôt que dans Users
