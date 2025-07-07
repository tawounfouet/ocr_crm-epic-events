# Guide d'utilisation du CRM Epic Events

Ce guide détaille comment utiliser le système CRM Epic Events à travers son interface en ligne de commande (CLI).

## Installation et configuration

### Prérequis

- Python 3.9 ou supérieur
- PostgreSQL (pour l'environnement de production)
- SQLite (pour l'environnement de développement)

### Installation

1. Clonez le dépôt GitHub :
   ```bash
   git clone https://github.com/votre-utilisateur/crm_epic_events.git
   cd crm_epic_events
   ```

2. Créez un environnement virtuel et activez-le :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. Installez les dépendances :
   ```bash
   pip install -e .
   ```

4. Configurez les variables d'environnement en copiant le fichier `.env.example` :
   ```bash
   cp .env.example .env
   ```

5. Modifiez le fichier `.env` avec vos paramètres de configuration :
   ```
   # Base de données
   DATABASE_URL=sqlite:///./epic_events.db
   # ou pour PostgreSQL :
   # DATABASE_URL=postgresql://utilisateur:mot_de_passe@localhost/epic_events
   
   # JWT
   SECRET_KEY=votre_clé_secrète_très_longue_et_complexe
   
   # Sentry
   SENTRY_DSN=votre_dsn_sentry
   ```

6. Initialisez la base de données :
   ```bash
   epic-events db init
   ```

### Premier démarrage

Lors du premier démarrage, vous devez créer un utilisateur administratif :

```bash
epic-events user create-admin
```

Cette commande vous guidera pour créer un compte administrateur avec le rôle "MANAGEMENT".

## Utilisation de l'interface en ligne de commande

Le CRM Epic Events utilise une interface en ligne de commande (CLI) basée sur Typer. La commande principale est `epic-events` suivie de sous-commandes.

### Aide générale

Pour obtenir de l'aide sur les commandes disponibles :

```bash
epic-events --help
```

### Authentification

1. Connexion :
   ```bash
   epic-events auth login
   ```
   Vous serez invité à saisir votre email et votre mot de passe.

2. Afficher l'utilisateur actuellement connecté :
   ```bash
   epic-events auth whoami
   ```

3. Déconnexion :
   ```bash
   epic-events auth logout
   ```

### Gestion des utilisateurs

#### Lister les utilisateurs
```bash
epic-events user list
```

Options disponibles :
- `--role` : Filtrer par rôle (SALES, SUPPORT, MANAGEMENT)

#### Créer un utilisateur
```bash
epic-events user create
```

Vous serez guidé interactivement pour renseigner les informations de l'utilisateur :
- Prénom
- Nom de famille
- Email
- Téléphone
- Mot de passe
- Rôle

#### Mettre à jour un utilisateur
```bash
epic-events user update [ID]
```

#### Supprimer un utilisateur
```bash
epic-events user delete [ID]
```

### Gestion des clients

#### Lister les clients
```bash
epic-events client list
```

Options disponibles :
- `--sales-contact` : Filtrer par commercial responsable
- `--sort-by` : Trier par un champ spécifique
- `--search` : Rechercher dans les noms/emails/entreprises

#### Créer un client
```bash
epic-events client create
```

Vous serez guidé pour renseigner les informations du client :
- Nom complet
- Email
- Téléphone
- Nom de l'entreprise

Le client sera automatiquement associé à l'utilisateur commercial connecté.

#### Afficher les détails d'un client
```bash
epic-events client show [ID]
```

#### Mettre à jour un client
```bash
epic-events client update [ID]
```

#### Supprimer un client
```bash
epic-events client delete [ID]
```

### Gestion des contrats

#### Lister les contrats
```bash
epic-events contract list
```

Options disponibles :
- `--client` : Filtrer par client
- `--signed` : Filtrer par statut de signature (True/False)
- `--unpaid` : Afficher uniquement les contrats avec un montant restant à payer

#### Créer un contrat
```bash
epic-events contract create
```

Vous serez guidé pour renseigner les informations du contrat :
- ID du client
- Montant total
- Montant restant à payer
- Statut de signature

#### Afficher les détails d'un contrat
```bash
epic-events contract show [ID]
```

#### Mettre à jour un contrat
```bash
epic-events contract update [ID]
```

#### Supprimer un contrat
```bash
epic-events contract delete [ID]
```

### Gestion des événements

#### Lister les événements
```bash
epic-events event list
```

Options disponibles :
- `--client` : Filtrer par client
- `--support-contact` : Filtrer par membre du support
- `--period` : Filtrer par période (aujourd'hui, semaine, mois)
- `--no-support` : Afficher les événements sans support assigné

#### Créer un événement
```bash
epic-events event create
```

Vous serez guidé pour renseigner les informations de l'événement :
- Nom de l'événement
- ID du contrat (doit être signé)
- Contact client
- Date et heure de début
- Date et heure de fin
- Lieu
- Nombre de participants
- Notes

#### Afficher les détails d'un événement
```bash
epic-events event show [ID]
```

#### Mettre à jour un événement
```bash
epic-events event update [ID]
```

#### Assigner un membre du support à un événement
```bash
epic-events event assign [EVENT_ID] [SUPPORT_USER_ID]
```

#### Supprimer un événement
```bash
epic-events event delete [ID]
```

## Exemples d'utilisation par rôle

### Utilisateur Commercial (SALES)

1. Connexion :
   ```bash
   epic-events auth login
   # Entrez votre email et mot de passe
   ```

2. Créer un nouveau client :
   ```bash
   epic-events client create
   # Suivez les instructions pour remplir les informations du client
   ```

3. Consulter vos clients :
   ```bash
   epic-events client list
   ```

4. Créer un contrat pour un client :
   ```bash
   epic-events contract create
   # Suivez les instructions pour remplir les informations du contrat
   ```

5. Lister les contrats non signés :
   ```bash
   epic-events contract list --signed False
   ```

6. Marquer un contrat comme signé :
   ```bash
   epic-events contract update 1
   # Suivez les instructions et modifiez le statut de signature
   ```

7. Créer un événement pour un contrat signé :
   ```bash
   epic-events event create
   # Suivez les instructions pour remplir les informations de l'événement
   ```

### Utilisateur Support (SUPPORT)

1. Connexion :
   ```bash
   epic-events auth login
   # Entrez votre email et mot de passe
   ```

2. Consulter les événements dont vous êtes responsable :
   ```bash
   epic-events event list --support-contact votre_id
   ```

3. Mettre à jour les détails d'un événement :
   ```bash
   epic-events event update 1
   # Suivez les instructions pour modifier les informations
   ```

4. Consulter tous les événements à venir cette semaine :
   ```bash
   epic-events event list --period semaine
   ```

### Utilisateur Gestion (MANAGEMENT)

1. Connexion :
   ```bash
   epic-events auth login
   # Entrez votre email et mot de passe
   ```

2. Créer un nouvel utilisateur :
   ```bash
   epic-events user create
   # Suivez les instructions pour remplir les informations de l'utilisateur
   ```

3. Lister tous les utilisateurs par rôle :
   ```bash
   epic-events user list --role SUPPORT
   ```

4. Voir les événements sans support assigné :
   ```bash
   epic-events event list --no-support
   ```

5. Assigner un membre du support à un événement :
   ```bash
   epic-events event assign 1 3
   # Assigne l'utilisateur avec ID 3 à l'événement avec ID 1
   ```

## Astuces et bonnes pratiques

1. **Sécurité** :
   - Déconnectez-vous après utilisation du CRM
   - Ne partagez jamais votre mot de passe
   - Utilisez des mots de passe complexes

2. **Gestion des clients** :
   - Maintenez les informations clients à jour
   - Associez correctement chaque client à un commercial

3. **Contrats et événements** :
   - Créez un événement uniquement après la signature du contrat
   - Assurez-vous que les montants restants à payer sont exacts

4. **Conseils d'utilisation** :
   - Utilisez les options de filtrage pour naviguer efficacement
   - Préférez les IDs pour les opérations sur des entités spécifiques
   - Consultez l'aide avec `--help` en cas de doute

## Résolution des problèmes courants

### Erreurs d'authentification

- **Message "Token invalide"** : Votre session a expiré. Reconnectez-vous avec `epic-events auth login`.
- **Échec de connexion** : Vérifiez que votre email et mot de passe sont corrects.

### Erreurs de permission

- **Message "Permission refusée"** : Vous n'avez pas les droits nécessaires pour cette action. Vérifiez votre rôle et vos responsabilités.

### Erreurs de base de données

- **Erreur de connexion** : Vérifiez que la base de données est accessible et que les informations de connexion dans `.env` sont correctes.

### Autres problèmes

- **Commande non trouvée** : Vérifiez que vous êtes dans l'environnement virtuel et que l'installation est complète.
- **Erreurs inattendues** : Consultez les logs dans le dossier `logs/` pour plus d'informations.
