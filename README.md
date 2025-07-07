
<h1 align="center">Epic Events CRM</h1>

## Aperçu du projet

Le CRM Epic Events est un système de gestion de la relation client développé pour Epic Events, une entreprise spécialisée dans l'organisation d'événements pour des startups. Cette application en ligne de commande permet aux différentes équipes de l'entreprise (commerciale, support, gestion) de gérer efficacement les clients, les contrats et les événements, avec un système d'accès sécurisé basé sur les rôles.

## Objectifs

- Fournir une interface en ligne de commande pour gérer les clients, contrats et événements
- Mettre en place une base de données sécurisée avec SQLAlchemy et PostgreSQL
- Implémenter un système d'authentification robuste avec gestion des permissions par rôle
- Assurer la journalisation des erreurs avec Sentry
- Respecter les bonnes pratiques de sécurité et de développement

## Contexte d'utilisation

Epic Events est structuré en trois départements distincts, chacun avec des responsabilités et des besoins spécifiques :

1. **Département commercial** : Gère les relations clients, crée de nouveaux clients dans le système et peut créer des événements une fois les contrats signés.

2. **Département support** : Responsable de l'organisation et du bon déroulement des événements assignés.

3. **Département gestion** : Administre le système, gère les utilisateurs et leurs permissions, et supervise les contrats.

## Fonctionnalités principales

- **Gestion des utilisateurs** : Création, authentification et gestion des permissions
- **Gestion des clients** : Ajout, consultation et mise à jour des informations clients
- **Gestion des contrats** : Création, suivi et mise à jour de contrats associés aux clients
- **Gestion des événements** : Organisation et suivi des événements liés aux contrats signés

## Stack technologique

- **Backend** : Python 3.9+
- **ORM** : SQLAlchemy
- **Base de données** : PostgreSQL (production), SQLite (développement)
- **CLI** : Typer, Rich
- **Validation de données** : Pydantic
- **Sécurité** : Passlib, PyJWT
- **Journalisation** : Sentry SDK, Loguru
- **Tests** : Pytest, Coverage
- **Qualité de code** : Black, Flake8, Mypy
- **Configuration** : python-dotenv


## Structure du projet
Voici la structure du projet CRM Epic Events :
```sh
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
```