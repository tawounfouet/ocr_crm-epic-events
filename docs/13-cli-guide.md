# Guide du CLI Epic Events

## Table des matières

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Architecture du CLI](#architecture-du-cli)
4. [Commandes disponibles](#commandes-disponibles)
5. [Guide d'utilisation par rôle](#guide-dutilisation-par-rôle)
6. [Développement et extension](#développement-et-extension)
7. [Bonnes pratiques](#bonnes-pratiques)
8. [Dépannage](#dépannage)

## Introduction

Le CLI (Command Line Interface) Epic Events est une interface en ligne de commande conçue pour faciliter la gestion du CRM d'Epic Events. Il permet aux différents utilisateurs (gestion, commerciaux, support) d'interagir avec le système CRM de manière efficace directement depuis un terminal.

### Objectifs du CLI

- Simplifier la gestion des clients, contrats et événements
- Offrir une interface accessible pour tous les rôles d'utilisateurs
- Automatiser les tâches récurrentes
- Fournir une alternative rapide à l'interface graphique

### Public cible

Ce guide s'adresse à trois types d'utilisateurs :

1. **Utilisateurs métier** : Employés d'Epic Events qui utiliseront le CLI pour leurs tâches quotidiennes
2. **Contributeurs techniques** : Développeurs qui souhaiteraient étendre ou modifier le CLI
3. **Étudiants** : Personnes qui étudient le projet à des fins éducatives

## Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- Un environnement virtuel (recommandé)

### Installation depuis le dépôt

1. Clonez le dépôt du projet :
```bash
git clone <URL_du_dépôt>
cd crm_epic_events
```

2. Créez et activez un environnement virtuel :
```bash
python -m venv .venv
source .venv/bin/activate  # Sur Unix/macOS
# ou
.venv\Scripts\activate  # Sur Windows
```

3. Installez le paquet en mode développement :
```bash
pip install -e .
```

4. Vérifiez l'installation :
```bash
epic-events --help
```

### Méthodes d'exécution

Il existe deux manières principales d'exécuter le CLI Epic Events :

#### Option 1 : Utiliser la commande installée

Si vous avez installé le package avec `pip install -e .`, vous pouvez utiliser directement la commande :

```bash
epic-events [commande]
```

Par exemple :
```bash
epic-events auth login
epic-events user list
```

#### Option 2 : Exécuter directement le module Python

Vous pouvez également exécuter le CLI directement depuis le module Python :

```bash
# Depuis la racine du projet
python -m cli.main [commande]
```

Par exemple :
```bash
python -m cli.main auth login
python -m cli.main user list
```

Cette option est particulièrement utile lors du développement ou si l'installation du package n'est pas possible.

## Architecture du CLI

Le CLI Epic Events est construit avec une architecture modulaire qui permet une maintenance facile et l'extension des fonctionnalités.

### Structure des dossiers

```
cli/
├── __init__.py
├── main.py                # Point d'entrée du CLI
├── commands/              # Modules de commandes
│   ├── __init__.py
│   ├── auth_commands.py   # Commandes d'authentification
│   ├── user_commands.py   # Gestion des utilisateurs
│   ├── client_commands.py # Gestion des clients
│   ├── contract_commands.py # Gestion des contrats
│   └── event_commands.py  # Gestion des événements
└── formatters/            # Formatage de sortie
    ├── __init__.py
    ├── styles.py          # Styles pour l'affichage
    └── tables.py          # Tableaux pour l'affichage des données
```

### Technologies utilisées

- **Typer** : Framework pour créer des applications CLI en Python
- **Rich** : Bibliothèque pour le formatage riche des sorties dans le terminal
- **SQLAlchemy** (en arrière-plan) : ORM pour l'interaction avec la base de données

## Commandes disponibles

Le CLI est organisé en plusieurs groupes de commandes correspondant aux différentes entités du CRM.

### Authentification (`auth`)

| Commande | Description | Exemples |
|----------|-------------|----------|
| `login` | Se connecter au système | `epic-events auth login` |
| `logout` | Se déconnecter | `epic-events auth logout` |
| `whoami` | Afficher l'utilisateur connecté | `epic-events auth whoami` |
| `change-password` | Changer son mot de passe | `epic-events auth change-password` |

### Utilisateurs (`user`)

| Commande | Description | Exemples |
|----------|-------------|----------|
| `list` | Lister tous les utilisateurs | `epic-events user list` |
| `create` | Créer un nouvel utilisateur | `epic-events user create` |
| `show` | Afficher les détails d'un utilisateur | `epic-events user show 1` |
| `update` | Mettre à jour un utilisateur | `epic-events user update 1 --email=nouveau@email.com` |
| `delete` | Supprimer un utilisateur | `epic-events user delete 1` |

### Clients (`client`)

| Commande | Description | Exemples |
|----------|-------------|----------|
| `list` | Lister tous les clients | `epic-events client list` |
| `create` | Créer un nouveau client | `epic-events client create` |
| `show` | Afficher les détails d'un client | `epic-events client show 1` |
| `update` | Mettre à jour un client | `epic-events client update 1 --phone="+33123456789"` |
| `delete` | Supprimer un client | `epic-events client delete 1` |

### Contrats (`contract`)

| Commande | Description | Exemples |
|----------|-------------|----------|
| `list` | Lister tous les contrats | `epic-events contract list` |
| `create` | Créer un nouveau contrat | `epic-events contract create` |
| `show` | Afficher les détails d'un contrat | `epic-events contract show 1` |
| `update` | Mettre à jour un contrat | `epic-events contract update 1 --total-amount=5000` |
| `sign` | Marquer un contrat comme signé | `epic-events contract sign 1` |
| `payment` | Enregistrer un paiement | `epic-events contract payment 1 --amount=2500` |
| `delete` | Supprimer un contrat | `epic-events contract delete 1` |

### Événements (`event`)

| Commande | Description | Exemples |
|----------|-------------|----------|
| `list` | Lister tous les événements | `epic-events event list` |
| `create` | Créer un nouvel événement | `epic-events event create` |
| `show` | Afficher les détails d'un événement | `epic-events event show 1` |
| `update` | Mettre à jour un événement | `epic-events event update 1 --location="Paris"` |
| `assign-support` | Assigner un contact support | `epic-events event assign-support 1 --support-id=3` |
| `delete` | Supprimer un événement | `epic-events event delete 1` |

### Options globales

Ces options sont disponibles pour toutes les commandes :

| Option | Description |
|--------|-------------|
| `--help` | Afficher l'aide |
| `--install-completion` | Installer l'autocomplétion pour le shell actuel |
| `--show-completion` | Afficher l'autocomplétion pour le shell actuel |

## Guide d'utilisation par rôle

### Pour l'équipe de gestion

L'équipe de gestion est responsable de la création et de la gestion des utilisateurs du système.

#### Création d'un nouvel utilisateur

```bash
epic-events user create
```

Le système vous demandera les informations nécessaires :
- Email de l'utilisateur
- Prénom
- Nom de famille
- Rôle (management, sales, support)
- Mot de passe

#### Modification d'un utilisateur existant

```bash
epic-events user update <id-utilisateur> --role=sales
```

#### Consultation des utilisateurs

```bash
epic-events user list
```

### Pour l'équipe commerciale

Les commerciaux sont responsables de la gestion des clients et des contrats.

#### Ajout d'un nouveau client

```bash
epic-events client create
```

#### Création d'un contrat pour un client

```bash
epic-events contract create
```

Le système vous demandera :
- ID du client
- Montant total du contrat
- Montant déjà payé (optionnel)
- Statut de signature

#### Marquer un contrat comme signé

```bash
epic-events contract sign <id-contrat>
```

#### Enregistrer un paiement

```bash
epic-events contract payment <id-contrat>
```

### Pour l'équipe support

L'équipe support gère les événements liés aux contrats signés.

#### Consulter les événements assignés

```bash
epic-events event list --support-id=<votre-id>
```

#### Mise à jour des informations d'un événement

```bash
epic-events event update <id-événement> --notes="Préparation en cours"
```

## Développement et extension

Cette section s'adresse aux développeurs qui souhaitent étendre ou modifier le CLI.

### Structure du code

Le CLI est construit avec Typer, qui permet une organisation hiérarchique des commandes.

#### Ajout d'une nouvelle commande

1. Identifiez le module approprié dans le dossier `cli/commands/`
2. Ajoutez votre fonction de commande avec le décorateur `@app.command()` :

```python
@app.command("nom-commande")
def nom_fonction(
    param1: str = typer.Option(..., help="Description du paramètre"),
    param2: int = typer.Argument(..., help="Description du paramètre")
):
    """Description de la commande."""
    # Votre code ici
    print_success("Opération réussie!")
```

3. Pour ajouter un nouveau groupe de commandes, créez un nouveau fichier dans `cli/commands/` et enregistrez-le dans `main.py` :

```python
from cli.commands import mon_module
app.add_typer(mon_module.app, name="nom-groupe", help="Description du groupe")
```

### Formatage des sorties

Utilisez les fonctions définies dans `cli/formatters/` pour assurer une cohérence visuelle :

```python
from cli.formatters.styles import print_title, print_success, print_error
from cli.formatters.tables import create_custom_table

# Afficher un titre
print_title("Mon titre")

# Afficher un tableau
table = create_custom_table(data)
console.print(table)
```

### Tests

Ajoutez des tests pour vos nouvelles commandes dans le dossier `tests/` :

```python
def test_ma_commande():
    # Votre test ici
    pass
```

## Récapitulatif des commandes

Pour faciliter la référence, voici une liste complète de toutes les commandes disponibles dans le CLI Epic Events :

```bash
# Commandes d'aide
epic-events --help                      # Afficher l'aide générale
epic-events [commande] --help           # Afficher l'aide d'une commande spécifique

# Authentification
epic-events auth login                  # Se connecter au système
epic-events auth logout                 # Se déconnecter
epic-events auth whoami                 # Afficher l'utilisateur actuellement connecté
epic-events auth change-password        # Changer son mot de passe

# Gestion des utilisateurs
epic-events user list                   # Lister tous les utilisateurs
epic-events user create                 # Créer un nouvel utilisateur
epic-events user show [id]              # Afficher les détails d'un utilisateur
epic-events user update [id] [options]  # Mettre à jour un utilisateur
epic-events user delete [id]            # Supprimer un utilisateur

# Gestion des clients
epic-events client list                 # Lister tous les clients
epic-events client create               # Créer un nouveau client
epic-events client show [id]            # Afficher les détails d'un client
epic-events client update [id] [options] # Mettre à jour un client
epic-events client delete [id]          # Supprimer un client

# Gestion des contrats
epic-events contract list               # Lister tous les contrats
epic-events contract list --client-id [id] # Filtrer les contrats par client
epic-events contract list --signed      # Filtrer les contrats signés
epic-events contract create             # Créer un nouveau contrat
epic-events contract show [id]          # Afficher les détails d'un contrat
epic-events contract update [id] [options] # Mettre à jour un contrat
epic-events contract sign [id]          # Marquer un contrat comme signé
epic-events contract payment [id] --amount [somme] # Enregistrer un paiement
epic-events contract delete [id]        # Supprimer un contrat

# Gestion des événements
epic-events event list                  # Lister tous les événements
epic-events event list --client-id [id] # Filtrer les événements par client
epic-events event list --support-id [id] # Filtrer les événements par support
epic-events event list --future-only    # Afficher uniquement les événements futurs
epic-events event create                # Créer un nouvel événement
epic-events event show [id]             # Afficher les détails d'un événement
epic-events event update [id] [options] # Mettre à jour un événement
epic-events event assign-support [id] --support-id [id] # Assigner un support
epic-events event delete [id]           # Supprimer un événement
```

Vous pouvez également exécuter ces commandes en utilisant le module Python directement :

```bash
python -m cli.main [commande]
```

Par exemple :
```bash
python -m cli.main user list
python -m cli.main event create
```

## Bonnes pratiques

### Utilisation du CLI

- Utilisez l'option `--help` pour découvrir les commandes disponibles
- Utilisez l'autocomplétion pour gagner du temps
- Préférez utiliser les IDs pour identifier précisément les ressources
- Utilisez l'option `-y` pour confirmer automatiquement les actions destructives en scripts

### Développement

- Maintenez une cohérence dans le nommage des commandes
- Documentez toutes les commandes avec des docstrings
- Utilisez des messages d'erreur clairs et informatifs
- Validez toutes les entrées utilisateur
- Suivez les principes SOLID pour la conception des commandes

## Dépannage

### Problèmes d'installation

**Problème** : `Command 'epic-events' not found`  
**Solution** : Vérifiez que le package est bien installé avec `pip list | grep epic-events-crm`. Si non, réinstallez avec `pip install -e .`

**Problème** : `TypeError: Parameter.make_metavar() missing 1 required positional argument: 'ctx'`  
**Solution** : Il y a un conflit de version entre Typer et Click. Exécutez :
```bash
pip uninstall typer click
pip install "typer[all]==0.9.0" "click==8.1.7"
```

### Problèmes d'authentification

**Problème** : Impossible de se connecter  
**Solution** : Vérifiez vos identifiants. Si vous avez oublié votre mot de passe, demandez à un administrateur de le réinitialiser.

**Problème** : Permission refusée pour une action  
**Solution** : Vérifiez que votre compte utilisateur a le rôle approprié pour cette action.

### Autres problèmes

Pour tout autre problème, consultez les logs dans le dossier `logs/` ou contactez l'équipe de développement.


## Conclusion Copilot

J'ai créé un guide détaillé pour le CLI Epic Events sous forme de fichier Markdown dans le dossier docs. Le document `13-cli-guide.md` est structuré pour répondre aux besoins de tous les publics cibles :

1. Pour les utilisateurs métier : Instructions claires sur l'utilisation quotidienne du CLI, organisées par rôle (gestion, commercial, support)
2. Pour les contributeurs techniques : Détails sur l'architecture, la structure du code et comment étendre les fonctionnalités
3. Pour les étudiants : Explications pédagogiques de la structure globale et des technologies utilisées

Le guide contient les sections suivantes :
- Introduction au CLI et ses objectifs
- Instructions d'installation détaillées
- Architecture du CLI et technologies utilisées
- Documentation complète de toutes les commandes disponibles
- Guides d'utilisation spécifiques pour chaque rôle
- Instructions pour le développement et l'extension du CLI
- Bonnes pratiques d'utilisation et de développement
- Section de dépannage pour les problèmes courants


### Sections supplémentaires
1. Une section `Méthodes d'exécution` juste après les instructions d'installation, qui explique en détail :
    - Comment exécuter le CLI avec la commande installée (`epic-events`)
    - Comment exécuter le CLI directement depuis le module Python (`python -m cli.main`)
    - Des exemples concrets pour chaque méthode

2. Un `Récapitulatif des commandes` complet avant la section des bonnes pratiques, qui :
  - Liste toutes les commandes disponibles, organisées par catégorie
  - Inclut toutes les variantes avec options et arguments
  - Fournit une explication concise de chaque commande
  - Rappelle également comment utiliser ces commandes avec la méthode d'exécution directe du module


Ces ajouts rendront le guide plus complet et pratique, permettant aux utilisateurs de trouver rapidement comment exécuter le CLI et d'avoir une référence rapide de toutes les commandes disponibles.




Ce document servira de référence complète pour quiconque souhaite utiliser ou contribuer au CLI Epic Events.