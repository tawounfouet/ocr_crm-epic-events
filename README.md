
crm_epic_events/
├── .env.example               # Exemple de configuration des variables d'environnement
├── .gitignore                 # Fichiers à ignorer par Git
├── README.md                  # Documentation du projet
├── requirements.txt           # Dépendances du projet
├── setup.py                   # Configuration du package
├── conftest.py                # Configuration des tests pytest
├── crm/
│   ├── __init__.py
│   ├── config.py              # Configuration de l'application
│   ├── models/                # Modèles SQLAlchemy et Pydantic
│   │   ├── __init__.py
│   │   ├── base.py           # Classe de base pour les modèles
│   │   ├── user.py           # Modèle utilisateur
│   │   ├── client.py         # Modèle client
│   │   ├── contract.py       # Modèle contrat
│   │   └── event.py          # Modèle événement
│   ├── database.py            # Configuration SQLAlchemy
│   ├── schemas/               # Schémas Pydantic
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── client.py
│   │   ├── contract.py
│   │   └── event.py
│   ├── services/              # Logique métier
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── client.py
│   │   ├── contract.py
│   │   └── event.py
│   ├── security/              # Fonctions de sécurité
│   │   ├── __init__.py
│   │   ├── auth.py           # Authentification
│   │   └── permissions.py     # Système de permissions
│   └── utils/                 # Utilitaires
│       ├── __init__.py
│       ├── logging.py         # Configuration de Loguru et Sentry
│       └── helpers.py         # Fonctions d'aide générales
├── cli/                       # Interface en ligne de commande
│   ├── __init__.py
│   ├── main.py                # Point d'entrée CLI (avec Typer)
│   ├── commands/              # Commandes de la CLI
│   │   ├── __init__.py
│   │   ├── auth_commands.py
│   │   ├── client_commands.py
│   │   ├── contract_commands.py
│   │   └── event_commands.py
│   └── formatters/            # Formatage des sorties avec Rich
│       ├── __init__.py
│       ├── tables.py
│       └── styles.py
└── tests/                     # Tests
    ├── __init__.py
    ├── conftest.py            # Configuration des fixtures
    ├── unit/                  # Tests unitaires
    └── integration/           # Tests d'intégration