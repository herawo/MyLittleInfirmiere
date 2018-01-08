
from flask_classy import FlaskView


# TODO: Ajouter les requètes concernant le patient
class PatientView(FlaskView):

    def index(self):
        return "Liste des patients", 200
