# GPTInterviewer-main

Bienvenue sur RHIA ! 👏 Cette partie représente la puissance de l'application de pointe alimentée par une IA générative conçue pour mener des entretiens simulés. Avec la capacité d'analyser votre CV téléchargé et les descriptions de poste, RHIA génère des questions personnalisées pour améliorer votre préparation aux entretiens. Vous avez même la possibilité de personnaliser votre propre expérience d'entretien !

## Sommaire

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Guide d'installation](#guide-dinstallation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)

## Fonctionnalités

- **Questions personnalisées :** RHIA génère des questions d'entretien personnalisées en fonction de votre CV téléchargé et des descriptions de poste.

- **Plusieurs écrans :** Accédez à différents écrans pour les aspects comportementaux, professionnels et liés au CV de l'entretien.

- **Expérience interactive :** Engagez une conversation avec RHIA, améliorant le réalisme du processus d'entretien.

- **Rafraîchissement facile :** Initiez une nouvelle session d'entretien simplement en actualisant la page.

- **Choix de l'interaction :** Sélectionnez entre un style d'interaction basé sur le chat ou sur la voix pour vos entretiens.

## Prérequis

- Python
- Pip (Python package installer)

## Guide d'installation

Ce guide vous aidera à installer et configurer facilement notre projet Streamlit sur votre environnement local.
Tout d'abord ouvrez votre terminal et effectuez les actions suivantes :

1. **Cloner le Repository :**
```bash
git clone https://github.com/LeoCarre/RHIA.git
cd RHIA/GPTInterviewer-main
```

2. **Installer Streamlit :**
```bash
pip install streamlit
```

3. **Installer les Dépendances :**
```bash
pip install -r requirements.txt
```

4. **Activer l'Environnement Virtuel :**
```bash
streamlit run Homepage.py
```

## Configuration

Avant d'exécuter l'application, vous devez configurer les clés d'API nécessaires. Suivez les étapes ci-dessous :

### Clés d'API AWS pour Synthesize Speech

Dans le fichier `synthesize_speech.py`, remplacez les lignes suivantes avec vos clés d'API AWS :

```bash
aws_access_key_id = 'votre_aws_access_key_id'
aws_secret_access_key = 'votre_aws_secret_access_key'
```

### Clé d'API OpenAI pour OpenAI Whisper

Dans le fichier `openai_whisper.py`, remplacez la ligne suivante avec votre clé d'API OpenAI :

```bash
openai.api_key = 'votre_openai_api_key'
```

Déclaration de la Variable d'Environnement
Pour sécuriser vos clés d'API, vous pouvez les stocker en tant que variables d'environnement. Voici comment déclarer une variable d'environnement avec la clé d'API OpenAI :

```bash
export YOUR_OPENAI_API_KEY="votre_clé_d'api_openai"
```

Assurez-vous de remplacer "votre_clé_d'api_openai" par votre propre clé d'API OpenAI. Vous pouvez également stocker vos clés d'API AWS de la même manière, en remplaçant "votre_aws_access_key_id" et "votre_aws_secret_access_key" par vos propres valeurs.


## Utilisation

### Questions personnalisées
RHIA offre la possibilité de générer des questions d'entretien personnalisées en fonction de votre CV téléchargé et des descriptions de poste. Pour profiter de cette fonctionnalité :

1. Téléchargez votre CV et les descriptions de poste pertinentes.
2. Lancez RHIA et sélectionnez l'option correspondante pour générer des questions personnalisées.
3. RHIA analysera les données téléchargées et générera des questions pertinentes pour votre préparation aux entretiens.

### Navigation entre les écrans
RHIA propose différents écrans pour vous aider à explorer différents aspects comportementaux, professionnels et liés à votre CV. Voici comment naviguer entre ces écrans :

- Utilisez la barre de navigation ou les boutons d'accès rapide pour passer d'un écran à un autre.
- Explorez les différents écrans pour vous préparer de manière exhaustive à divers scénarios d'entretien.

### Expérience interactive
L'interaction avec RHIA est conçue pour être immersive et réaliste. Voici comment profiter de cette expérience interactive :

- Engagez une conversation avec RHIA en répondant aux questions posées.
- Utilisez des réponses authentiques et réfléchies pour simuler au mieux un véritable entretien.
- Observez les réactions et les réponses de RHIA pour affiner vos compétences en entretien.

### Rafraîchissement facile
Pour initier une nouvelle session d'entretien ou pour actualiser l'interface, vous pouvez simplement rafraîchir la page. Voici comment faire :

1. Utilisez la fonction de rafraîchissement de votre navigateur ou appuyez sur la touche F5.
2. Vous serez redirigé vers la page d'accueil de RHIA, prêt à commencer une nouvelle session d'entretien ou à explorer d'autres fonctionnalités.

### Choix de l'interaction
RHIA propose deux styles d'interaction : chat et voix. Choisissez celui qui correspond le mieux à vos préférences et à vos besoins :

1. Sélectionnez l'option de chat pour interagir avec RHIA via une interface de messagerie.
2. Optez pour l'interaction vocale pour converser avec RHIA à l'aide de la reconnaissance vocale et des synthétiseurs vocaux.

