# Sommaire de la documentation

Bienvenue dans la documentation complète du CRM Epic Events. Ce sommaire vous aidera à naviguer à travers les différentes sections de la documentation.

## Présentation générale

- [01 - Introduction](01-introduction.md)
  - Aperçu du projet
  - Objectifs
  - Contexte d'utilisation
  - Fonctionnalités principales
  - Stack technologique

- [12 - Cahier des charges](12-cahier-des-charges.md)
  - Document de référence complet
  - Contexte et enjeux détaillés
  - Exigences fonctionnelles exhaustives
  - Exigences non fonctionnelles
  - Contraintes techniques et organisationnelles
  - Architecture et conception
  - Sécurité et conformité
  - Planning et jalons
  - Risques et mitigation
  - Livrables et critères d'acceptation

## Architecture et conception

- [02 - Architecture et structure du projet](02-architecture.md)
  - Vue d'ensemble
  - Architecture globale
  - Structure des répertoires
  - Description des composants
  - Flux de données
  - Principes architecturaux

- [03 - Modélisation des données](03-data-modeling.md)
  - Schéma de la base de données
  - Description détaillée des entités
  - Relations
  - Règles métier
  - Conception de la base de données
  - Code d'implémentation

- [07 - Schéma de la base de données](07-database-schema.md)
  - Diagramme Entité-Relation
  - Schéma SQL
  - Modèles SQLAlchemy
  - Règles d'intégrité
  - Migration de la base de données

## Sécurité et authentification

- [04 - Sécurité et authentification](04-security.md)
  - Architecture de sécurité
  - Authentification des utilisateurs
  - Gestion des tokens avec JWT
  - Système de permissions
  - Protection contre les attaques
  - Journalisation de sécurité
  - Bonnes pratiques de sécurité
  - Tests de sécurité

## Développement

- [11 - Guide de développement](11-guide-developpement.md)
  - Préparation de l'environnement
  - Structure du projet
  - Configuration de base
  - Développement des modèles de données
  - Système d'authentification et sécurité
  - Développement des services métier
  - Interface en ligne de commande
  - Tests unitaires
  - Tests d'intégration
  - Documentation et finalisation
  - Checklist de développement

## Guide d'utilisation

- [05 - Guide d'utilisation](05-user-guide.md)
  - Installation et configuration
  - Utilisation de l'interface en ligne de commande
  - Gestion des utilisateurs
  - Gestion des clients
  - Gestion des contrats
  - Gestion des événements
  - Exemples d'utilisation par rôle
  - Astuces et bonnes pratiques
  - Résolution des problèmes courants

## Développement et déploiement

- [06 - Plan d'action](06-action-plan.md)
  - Vue d'ensemble du plan
  - Détail des phases et tâches
  - Répartition du travail
  - Gestion des risques
  - Suivi de progression
  - Critères de succès
  - Ressources nécessaires
  - Livrables finaux

- [08 - Configuration du projet et des dépendances](08-project-configuration.md)
  - Structure des fichiers de configuration
  - Dépendances du projet
  - Configuration des outils de qualité de code
  - Configuration de Sentry
  - Configuration de la base de données
  - Configuration des migrations avec Alembic
  - Configuration du déploiement

## Diagrammes

La documentation contient plusieurs diagrammes Mermaid pour illustrer différents aspects du système :

1. Architecture globale (dans [02 - Architecture](02-architecture.md))
2. Flux de données (dans [02 - Architecture](02-architecture.md))
3. Schéma de la base de données (dans [03 - Modélisation des données](03-data-modeling.md) et [07 - Schéma de la base de données](07-database-schema.md))
4. Architecture de sécurité (dans [04 - Sécurité](04-security.md))
5. Processus d'authentification (dans [04 - Sécurité](04-security.md))
6. Structure des rôles et permissions (dans [04 - Sécurité](04-security.md))
7. Planification du développement (dans [06 - Plan d'action](06-action-plan.md))
8. Répartition du temps de développement (dans [06 - Plan d'action](06-action-plan.md))

## Pour aller plus loin

Pour toute question ou information supplémentaire, n'hésitez pas à consulter :

1. Le code source du projet
2. Les tests unitaires et d'intégration
3. Les issues et discussions sur le dépôt GitHub

---

Documentation créée pour le projet CRM Epic Events - Version 1.0
