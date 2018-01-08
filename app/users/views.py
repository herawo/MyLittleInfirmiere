
from flask_classy import FlaskView


# TODO: Ajouter les requètes concernant l'utilisateur (infirmière)
class UserView(FlaskView):

    def index(self):
        return "Liste des utilisateurs", 200
