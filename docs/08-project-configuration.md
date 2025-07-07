# Configuration du projet et des dépendances

Ce document détaille la configuration du projet CRM Epic Events et les dépendances utilisées pour son développement.

## Structure des fichiers de configuration

### Fichier .env

Le fichier `.env` contient les variables d'environnement nécessaires à l'exécution du projet. Il n'est pas versionné (inclus dans `.gitignore`) pour des raisons de sécurité.

Voici un exemple de contenu pour le fichier `.env` :

```dotenv
# Base de données
DATABASE_URL=sqlite:///./epic_events.db
# Pour PostgreSQL en production :
# DATABASE_URL=postgresql://utilisateur:mot_de_passe@localhost/epic_events

# JWT
SECRET_KEY=votre_clé_secrète_très_longue_et_complexe
ACCESS_TOKEN_EXPIRE_MINUTES=1440  # 24 heures

# Sentry
SENTRY_DSN=https://votre-clé@sentry.io/votre-projet
SENTRY_ENVIRONMENT=development
```

### Fichier .env.example

Le fichier `.env.example` est une version modèle du fichier `.env` sans les valeurs sensibles. Il est inclus dans le dépôt pour montrer la structure attendue :

```dotenv
# Base de données
DATABASE_URL=sqlite:///./epic_events.db
# Pour PostgreSQL en production :
# DATABASE_URL=postgresql://utilisateur:mot_de_passe@localhost/epic_events

# JWT
SECRET_KEY=your_secret_key_here
ACCESS_TOKEN_EXPIRE_MINUTES=1440  # 24 heures

# Sentry
SENTRY_DSN=https://your-key@sentry.io/your-project
SENTRY_ENVIRONMENT=development
```

### Fichier setup.py

Le fichier `setup.py` définit la configuration du package Python :

```python
from setuptools import setup, find_packages

setup(
    name="epic-events",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "sqlalchemy>=1.4.0,<2.0.0",
        "alembic>=1.7.0,<2.0.0",
        "typer>=0.6.0,<1.0.0",
        "rich>=12.0.0,<13.0.0",
        "pydantic>=1.9.0,<2.0.0",
        "passlib>=1.7.4,<2.0.0",
        "pyjwt>=2.3.0,<3.0.0",
        "sentry-sdk>=1.5.0,<2.0.0",
        "loguru>=0.6.0,<1.0.0",
        "python-dotenv>=0.20.0,<1.0.0",
        "psycopg2-binary>=2.9.0,<3.0.0",  # Pour PostgreSQL
    ],
    entry_points={
        "console_scripts": [
            "epic-events=cli.main:app",
        ],
    },
    python_requires=">=3.9",
    author="Votre Nom",
    author_email="votre.email@exemple.com",
    description="Système CRM pour Epic Events",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
```

### Fichier requirements.txt

Le fichier `requirements.txt` liste toutes les dépendances du projet pour une installation facile :

```
sqlalchemy==1.4.46
alembic==1.8.1
typer==0.7.0
rich==12.6.0
pydantic==1.10.4
passlib==1.7.4
pyjwt==2.6.0
sentry-sdk==1.13.0
loguru==0.6.0
python-dotenv==0.21.0
psycopg2-binary==2.9.5
pytest==7.2.1
pytest-cov==4.0.0
black==23.1.0
flake8==6.0.0
mypy==1.0.0
```

### Fichier conftest.py

Le fichier `conftest.py` à la racine du projet configure les fixtures pour les tests avec pytest :

```python
import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from crm.models.base import Base
from crm.database import get_db, SessionLocal


@pytest.fixture(scope="session")
def test_db_engine():
    """Crée un moteur de base de données pour les tests"""
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    return engine


@pytest.fixture(scope="function")
def db_session(test_db_engine):
    """Crée une session de base de données pour les tests"""
    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=test_db_engine
    )
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.rollback()
        session.close()


@pytest.fixture(scope="function")
def override_get_db(db_session):
    """Remplace la fonction get_db pour les tests"""

    def _override_get_db():
        try:
            yield db_session
        finally:
            pass

    return _override_get_db
```

## Dépendances du projet

### Base de données et ORM

- **SQLAlchemy** : ORM (Object-Relational Mapping) pour interagir avec la base de données
- **Alembic** : Outil de migration de base de données pour SQLAlchemy
- **psycopg2-binary** : Pilote PostgreSQL pour Python

### Interface CLI

- **Typer** : Bibliothèque pour créer des interfaces en ligne de commande en Python
- **Rich** : Bibliothèque pour des sorties console enrichies et formatées

### Validation et Sécurité

- **Pydantic** : Bibliothèque de validation de données avec prise en charge des types statiques
- **Passlib** : Bibliothèque pour le hachage et la vérification des mots de passe
- **PyJWT** : Bibliothèque pour la création et validation des tokens JWT

### Logging et Monitoring

- **Sentry SDK** : Client pour l'intégration avec la plateforme Sentry
- **Loguru** : Bibliothèque de journalisation améliorée pour Python

### Utilitaires

- **python-dotenv** : Chargement des variables d'environnement depuis un fichier .env

### Outils de développement et de test

- **pytest** : Framework de test
- **pytest-cov** : Extension pytest pour la couverture de code
- **black** : Outil de formatage de code
- **flake8** : Linter pour le style de code
- **mypy** : Vérificateur de types statiques pour Python

## Configuration des outils de qualité de code

### Black

Fichier `pyproject.toml` pour la configuration de Black :

```toml
[tool.black]
line-length = 88
target-version = ['py39']
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''
```

### Flake8

Fichier `.flake8` pour la configuration de Flake8 :

```ini
[flake8]
max-line-length = 88
extend-ignore = E203
exclude = .git,__pycache__,docs/source/conf.py,old,build,dist,.venv
per-file-ignores =
    __init__.py:F401,F403
```

### Mypy

Fichier `mypy.ini` pour la configuration de Mypy :

```ini
[mypy]
python_version = 3.9
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
disallow_incomplete_defs = True

[mypy.plugins.sqlalchemy.ext.declarative.mapped_classes]
class_name_is_constructor = True

[mypy.plugins.pydantic.compilers]
ignore_missing_imports = True

[mypy-alembic.*]
ignore_missing_imports = True

[mypy-pytest.*]
ignore_missing_imports = True

[mypy-rich.*]
ignore_missing_imports = True
```

## Configuration de Sentry

La configuration de Sentry est faite dans le fichier `crm/utils/logging.py` :

```python
import os
import sentry_sdk
from loguru import logger
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

# Configuration de Sentry
sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    environment=os.getenv("SENTRY_ENVIRONMENT", "development"),
    integrations=[
        SqlalchemyIntegration(),
    ],
    traces_sample_rate=1.0,
    
    # Envoyer les informations d'utilisateur au serveur Sentry
    send_default_pii=True,
)

# Configuration de Loguru
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Supprimer le gestionnaire par défaut
logger.remove()

# Ajouter des gestionnaires personnalisés
logger.add(
    "logs/info.log",
    level="INFO",
    rotation="10 MB",
    retention="1 week",
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
)

logger.add(
    "logs/error.log",
    level="ERROR",
    rotation="10 MB",
    retention="1 month",
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {name}:{function}:{line} | {message}",
)

# Ajouter le gestionnaire de console
logger.add(
    lambda msg: print(msg),
    level=LOG_LEVEL,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    colorize=True,
)

def configure_sentry_scope(user_info=None):
    """Configure le contexte Sentry avec les informations utilisateur"""
    if user_info:
        with sentry_sdk.configure_scope() as scope:
            scope.set_user(user_info)
```

## Configuration de la base de données

La configuration de la connexion à la base de données est définie dans `crm/database.py` :

```python
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# URL de la base de données depuis les variables d'environnement
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./epic_events.db")

# Créer le moteur SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    # Ces arguments sont spécifiques à SQLite et ne sont pas nécessaires pour PostgreSQL
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

# Créer une classe de session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fonction pour obtenir une session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

## Configuration des migrations avec Alembic

La configuration des migrations avec Alembic est définie dans `alembic.ini` et dans le dossier `migrations/` :

```ini
# alembic.ini
[alembic]
script_location = migrations
prepend_sys_path = .

[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console
qualname =

[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S
```

Le script d'initialisation des migrations est dans `migrations/env.py` :

```python
from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool

import os
import sys
from dotenv import load_dotenv

# Ajouter le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Charger les variables d'environnement
load_dotenv()

# Importer les modèles pour qu'Alembic les détecte
from crm.models.base import Base
import crm.models.user
import crm.models.client
import crm.models.contract
import crm.models.event

# Configuration d'Alembic
config = context.config

# Remplacer l'URL de la base de données par celle des variables d'environnement
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))

# Configurer la journalisation depuis le fichier alembic.ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Définir les métadonnées cibles
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata,
            render_as_batch=True,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

## Configuration du déploiement

Pour déployer l'application en production, des configurations supplémentaires sont nécessaires. Voici quelques recommandations pour un déploiement sécurisé :

1. Utilisez PostgreSQL au lieu de SQLite
2. Définissez des variables d'environnement sécurisées
3. Utilisez un gestionnaire de processus comme Supervisor
4. Configurez Sentry pour l'environnement de production
5. Mettez en place des sauvegardes régulières de la base de données
