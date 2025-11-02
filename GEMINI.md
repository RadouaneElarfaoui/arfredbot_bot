# Fichier de Projet Gemini pour arfredbot_bot

Ce fichier contient des informations spécifiques au projet et du contexte pour l'agent IA Gemini.

## 1. Aperçu du Projet

Ce projet est un bot Telegram basé sur Python utilisant le framework Flask. Il est conçu pour être déployé en tant que fonction serverless sur Vercel.

## 2. Structure du Projet

```
/
|-- api/
|   |-- webhook.py
|-- .gitignore
|-- requirements.txt
|-- vercel.json
```

### Description des Fichiers :
*   **`api/webhook.py`**: L'application Flask principale qui gère les webhooks de Telegram.
*   **`.gitignore`**: Spécifie les fichiers que Git doit ignorer.
*   **`requirements.txt`**: Liste les dépendances Python du projet.
*   **`vercel.json`**: Fichier de configuration pour le déploiement sur Vercel.

## 3. Informations Clés & Commandes

### Dépendances
Installez les dépendances avec :
```bash
pip install -r requirements.txt
```

### Variables d'Environnement
*   `BOT_TOKEN`: Le token du bot Telegram. Doit être configuré dans les paramètres du projet sur Vercel. **Ne commitez jamais ce token sur Git.**

### Configuration du Webhook
Pour connecter le bot au déploiement Vercel, utilisez le modèle d'URL suivant en remplaçant les placeholders :
```
https://api.telegram.org/bot<VOTRE_TOKEN_DE_BOT>/setWebhook?url=<URL_DE_VOTRE_APP_VERCEL>
```

## 4. Instructions pour l'Agent

- Pour ajouter une nouvelle commande, il faut modifier `api/webhook.py` en ajoutant une nouvelle fonction de handler et en l'enregistrant auprès du dispatcher.
- Lorsque l'utilisateur demande la synchronisation du code, utilise les outils disponibles pour effectuer les étapes suivantes dans l'ordre :
    1.  `git status` : Pour visualiser l'état actuel du dépôt et identifier les fichiers modifiés.
    2.  `git diff` : Pour examiner les changements exacts avant de les "stager".
    3.  `git add .` : Pour "stager" toutes les modifications.
    4.  `git commit -m "Description significative des changements"` : Pour enregistrer les modifications avec un message de commit clair et descriptif.
    5.  `git push origin master` : Pour envoyer les changements vers le dépôt distant sur GitHub, ce qui déclenchera automatiquement un nouveau déploiement sur Vercel.
