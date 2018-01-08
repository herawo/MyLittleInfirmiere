# MyLittleInfirmiere


## Team members

- Nicolas Bouyssounousse
- Romain Vincent
- Yaniss Fournet
- Michael Martinez
- Valentin Mele
- Alexis Clément

## Objectifs

Créer une plateforme de gestion de patients pour infirmières qui aura comme fonctionnalités:

### Fonctionnalitées attendues
- Page d’accueil qui affiche les différents patients gérés par l’infirmière
- Pouvoir Créer/modifier/supprimer une rubrique patient
- Une rubrique patient contient:
    - Nom,
    - Prénom
    - Numéro de sécurité sociale (générez automatiquement)
    - Pathologie
    - Date de la plus récente visite
- Gérer les utilisateurs :
    - login/register
    - Gestion de mots de passes oubliés
    - Gestion des patients d’une infirmière (affectation/ non affectation)


## Choix technologiques en suspend

- Backend:
    - Serveur: Flask, Django
    - ORM : SQLAlchemy, ...
    - Base de données : sqlite, 
    - Hébergement/support: ?
- Front-end:
    - Static (le serveur envoie les pages html toutes faites, genre php): Jinja
    - Dynamique (besoin application client en javascript): angularjs, ...
    - template css: Bootstrap
    - pas de preprocesseur css
- Versionning : Github
- Intégration continue: Travis CI, jenkins
- Tests unitaires: Pytest, ... ?