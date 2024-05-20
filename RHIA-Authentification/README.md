# RHIA-Authentification

Cette application web a été développée en utilisant le framework Django populaire et Bootstrap pour le frontend. Cette mini-application a été conçue pour être facilement intégrée dans un projet système plus large qui nécessite un système d'inscription et de connexion.

## Sommaire

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Guide d'installation](#guide-dinstallation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)

## Fonctionnalités
    
- **Inscription:** Les utilisateurs peuvent s'inscrire et créer un nouveau profil
- **Connexion:** Les utilisateurs enregistrés peuvent se connecter en utilisant leur nom d'utilisateur et leur mot de passe
- **Connexion aux applications sociales:** Les utilisateurs peuvent se connecter en utilisant leur compte GitHub ou Google
- **Profil utilisateur:** Une fois connectés, les utilisateurs peuvent créer et mettre à jour des informations supplémentaires telles que l'avatar et la bio dans la page de profil
- **Mise à jour du profil:** Les utilisateurs peuvent mettre à jour leurs informations telles que le nom d'utilisateur, l'e-mail, le mot de passe, l'avatar et la bio
- **Se souvenir de moi:** Option de cookie, les utilisateurs n'ont pas besoin de fournir leurs informations d'identification à chaque fois qu'ils accèdent au site
- **Mot de passe oublié:** – Les utilisateurs peuvent facilement récupérer leur mot de passe s'ils l'oublient
- **Panneau d'administration:** – l'administrateur peut créer, lire, mettre à jour et supprimer des utilisateurs

## Prérequis

- Python
- Pip (Python package installer)
- Virtualenv

## Guide d'installation

Ce guide vous aidera à installer et configurer facilement notre projet Django sur votre environnement local.
Tout d'abord ouvrez votre terminal et effectuez les actions suivantes :

1. **Cloner le Repository :**

```bash
git clone https://github.com/LeoCarre/RHIA.git
cd RHIA/RHIA-Authentification
```

2. **Créer un Environnement Virtuel :**

```bash
python -m venv myenv
```

3. **Activer l'Environnement Virtuel :**
- Sur Windows :

```bash
myenv\Scripts\activate
```
- Sur MacOS/Linux :

```bash
source myenv/bin/activate
```
4. **Installer les Dépendances :**
```bash
pip install -r requirements.txt
```

## Configuration

Appliquer les Migrations :
```bash
python manage.py migrate
```

Créer un Super Utilisateur :
```bash
python manage.py createsuperuser
```
Suivez les instructions pour créer un super utilisateur qui vous permettra d'accéder à l'interface d'administration.

Lancer le Serveur de Développement :
```bash
python manage.py runserver
```
Le serveur de développement sera accessible à l'adresse http://127.0.0.1:8000/.

## Utilisation

- Accédez à l'interface d'administration en ajoutant /admin à l'URL du serveur (par exemple : http://127.0.0.1:8000/admin) et connectez-vous avec les informations d'identification du super utilisateur que vous avez créé.
- Explorez les fonctionnalités de l'application et testez son fonctionnement.