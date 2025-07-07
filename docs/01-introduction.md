# Epic Events CRM - Introduction

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

## Documentations associées

- [Architecture et structure du projet](02-architecture.md)
- [Modélisation des données](03-data-modeling.md)
- [Sécurité et authentification](04-security.md)
- [Guide d'utilisation](05-user-guide.md)
- [Plan d'action](06-action-plan.md)
