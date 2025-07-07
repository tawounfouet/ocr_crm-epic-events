# Guide de Développement CRM Epic Events

Ce guide détaille toutes les étapes du développement du CRM Epic Events, de la mise en place de l'environnement jusqu'aux tests et au déploiement.

## Table des matières

1. [Préparation de l'environnement](#1-préparation-de-lenvironnement)
2. [Structure du projet](#2-structure-du-projet)
3. [Configuration de base](#3-configuration-de-base)
4. [Développement des modèles de données](#4-développement-des-modèles-de-données)
5. [Système d'authentification et sécurité](#5-système-dauthentification-et-sécurité)
6. [Développement des services métier](#6-développement-des-services-métier)
7. [Interface en ligne de commande](#7-interface-en-ligne-de-commande)
8. [Tests unitaires](#8-tests-unitaires)
9. [Tests d'intégration](#9-tests-dintégration)
10. [Documentation et finalisation](#10-documentation-et-finalisation)

---

## 1. Préparation de l'environnement

### 1.1. Prérequis système

Avant de commencer, assurez-vous d'avoir :
- Python 3.9 ou supérieur installé
- Git configuré
- Un éditeur de code (VS Code recommandé)
- PostgreSQL installé pour la production (optionnel en développement)

### 1.2. Création de l'environnement virtuel

```bash
# Créer l'environnement virtuel
python3.11 -m venv .venv

# Activer l'environnement virtuel
source .venv/bin/activate

# Vérifier la version de Python
python --version
```

### 1.3. Installation des dépendances

Créer le fichier `requirements.txt` :

```bash
# Créer le fichier requirements.txt
touch requirements.txt
```

Contenu du fichier `requirements.txt` :

```
# Base
sqlalchemy==1.4.46
alembic==1.13.1
psycopg2-binary==2.9.5

# CLI et interface
typer[all]==0.9.0
rich==13.7.0

# Validation et sérialisation
pydantic==1.10.13

# Sécurité
passlib[bcrypt]==1.7.4
pyjwt==2.8.0

# Configuration
python-dotenv==1.0.0

# Journalisation
loguru==0.7.2
sentry-sdk==1.38.0

# Tests
pytest==7.4.3
pytest-cov==4.1.0
pytest-mock==3.12.0

# Développement
black==23.11.0
flake8==6.1.0
mypy==1.7.1
pre-commit==3.6.0
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

### 1.4. Configuration Git et pre-commit

```bash
# Initialiser le repository Git (si pas déjà fait)
git init

# Créer .gitignore
touch .gitignore
```

Contenu du `.gitignore` :

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Database
*.db
*.sqlite3

# Environment variables
.env

# Logs
logs/
*.log

# Coverage
.coverage
htmlcov/
.pytest_cache/

# Alembic
alembic/versions/*.py
!alembic/versions/.gitkeep

# OS
.DS_Store
Thumbs.db
```

Configuration de pre-commit :

```bash
# Créer .pre-commit-config.yaml
touch .pre-commit-config.yaml
```

Contenu du `.pre-commit-config.yaml` :

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.11.0
    hooks:
      - id: black
        language_version: python3.9

  - repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
        args: [--max-line-length=88, --extend-ignore=E203]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.1
    hooks:
      - id: mypy
        additional_dependencies: [types-requests]
```

Installer pre-commit :

```bash
pre-commit install
```

---

## 2. Structure du projet

### 2.1. Création de la structure des dossiers

```bash
# Créer la structure de base
mkdir -p crm/{models,services,security,utils,schemas}
mkdir -p cli/{commands,formatters}
mkdir -p tests/{unit,integration,fixtures}
mkdir -p alembic/versions
mkdir -p logs

# Créer les fichiers __init__.py
touch crm/__init__.py
touch crm/models/__init__.py
touch crm/services/__init__.py
touch crm/security/__init__.py
touch crm/utils/__init__.py
touch crm/schemas/__init__.py
touch cli/__init__.py
touch cli/commands/__init__.py
touch cli/formatters/__init__.py
touch tests/__init__.py
touch tests/unit/__init__.py
touch tests/integration/__init__.py
touch alembic/versions/.gitkeep
```

### 2.2. Structure finale du projet

```
crm_epic_events/
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── README.md
├── requirements.txt
├── setup.py
├── conftest.py
├── alembic.ini
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── crm/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── user.py
│   │   ├── client.py
│   │   ├── contract.py
│   │   └── event.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── client.py
│   │   ├── contract.py
│   │   └── event.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── client.py
│   │   ├── contract.py
│   │   └── event.py
│   ├── security/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── permissions.py
│   │   └── token_storage.py
│   └── utils/
│       ├── __init__.py
│       ├── logging.py
│       └── helpers.py
├── cli/
│   ├── __init__.py
│   ├── main.py
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── auth_commands.py
│   │   ├── user_commands.py
│   │   ├── client_commands.py
│   │   ├── contract_commands.py
│   │   └── event_commands.py
│   └── formatters/
│       ├── __init__.py
│       ├── tables.py
│       └── styles.py
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── unit/
    └── integration/
```

---

## 3. Configuration de base

### 3.1. Configuration de l'application

```bash
# Créer le fichier de configuration
touch crm/config.py
```

Développer `crm/config.py` :

```python
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./epic_events.db")
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440"))
    
    # Sentry
    SENTRY_DSN: str = os.getenv("SENTRY_DSN", "")
    SENTRY_ENVIRONMENT: str = os.getenv("SENTRY_ENVIRONMENT", "development")
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    class Config:
        case_sensitive = True

settings = Settings()
```

### 3.2. Configuration de la base de données

```bash
# Créer le fichier de base de données
touch crm/database.py
```

Développer `crm/database.py` :

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from crm.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {},
    echo=False,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### 3.3. Configuration d'Alembic

```bash
# Initialiser Alembic
#alembic init alembic
alembic init migrations

```

Modifier `alembic/env.py` pour intégrer nos modèles :

```python
# Dans alembic/env.py, remplacer la ligne target_metadata
from crm.models.base import Base
target_metadata = Base.metadata
```

### 3.4. Fichier d'exemple d'environnement

```bash
# Créer .env.example
```python
# Dans alembic/env.py, remplacer la ligne target_metadata
from crm.models.base import Base
target_metadata = Base.metadata
```

### 3.4. Fichier d'exemple d'environnement

```bash
# Créer .env.example
touch .env.example
```

Contenu de `.env.example` :

```env
# Database
DATABASE_URL=sqlite:///./epic_events.db
# DATABASE_URL=postgresql://user:password@localhost/epic_events

# Security
SECRET_KEY=your-super-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# Sentry
SENTRY_DSN=https://your-sentry-dsn@sentry.io/project-id
SENTRY_ENVIRONMENT=development

# Logging
LOG_LEVEL=INFO
```

---

## 4. Développement des modèles de données

### 4.1. Modèle de base

```bash
# Créer le modèle de base
touch crm/models/base.py
```

Développer `crm/models/base.py` :

```python
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
```

### 4.2. Énumération des rôles

```bash
# Créer le fichier pour les énumérations
touch crm/models/enums.py
```

Développer `crm/models/enums.py` :

```python
from enum import Enum

class Role(str, Enum):
    SALES = "SALES"
    SUPPORT = "SUPPORT"
    MANAGEMENT = "MANAGEMENT"
```

### 4.3. Développement des modèles

Développer chaque modèle dans l'ordre de dépendance :

1. **User** (`crm/models/user.py`)
2. **Client** (`crm/models/client.py`)
3. **Contract** (`crm/models/contract.py`)
4. **Event** (`crm/models/event.py`)

### 4.4. Mise à jour du fichier __init__.py

```python
# crm/models/__init__.py
from .base import Base
from .user import User
from .client import Client
from .contract import Contract
from .event import Event

__all__ = ["Base", "User", "Client", "Contract", "Event"]
```

### 4.5. Première migration

```bash
# Créer la première migration
alembic revision --autogenerate -m "Initial migration"

# Appliquer la migration
alembic upgrade head
```

---

## 5. Système d'authentification et sécurité

### 5.1. Développement de l'authentification

Ordre de développement :

1. **Hachage des mots de passe** (`crm/security/auth.py`)
2. **Gestion des JWT** (dans le même fichier)
3. **Stockage des tokens** (`crm/security/token_storage.py`)
4. **Système de permissions** (`crm/security/permissions.py`)

### 5.2. Configuration de la journalisation

Développer `crm/utils/logging.py` :

```python
import os
import sentry_sdk
from loguru import logger
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from crm.config import settings

# Configuration de Sentry
if settings.SENTRY_DSN:
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        environment=settings.SENTRY_ENVIRONMENT,
        integrations=[SqlalchemyIntegration()],
        traces_sample_rate=1.0,
    )

# Configuration de Loguru
logger.remove()

# Créer le dossier logs s'il n'existe pas
os.makedirs("logs", exist_ok=True)

# Ajouter les handlers
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
```

---

## 6. Développement des services métier

### 6.1. Ordre de développement des services

1. **Service d'authentification** (`crm/services/auth.py`)
2. **Service utilisateur** (`crm/services/user.py`)
3. **Service client** (`crm/services/client.py`)
4. **Service contrat** (`crm/services/contract.py`)
5. **Service événement** (`crm/services/event.py`)

### 6.2. Schémas Pydantic

Développer les schémas Pydantic en parallèle des services :

1. `crm/schemas/user.py`
2. `crm/schemas/client.py`
3. `crm/schemas/contract.py`
4. `crm/schemas/event.py`

### 6.3. Pattern de développement pour chaque service

Pour chaque service, suivre ce pattern :

```python
# Exemple pour client.py
class ClientService:
    def __init__(self, db_session):
        self.db = db_session
    
    def create_client(self, client_data: ClientCreate, current_user: User) -> Client:
        # Validation des permissions
        # Validation des données
        # Création de l'objet
        # Sauvegarde en base
        # Journalisation
        # Retour du résultat
        pass
    
    def get_client(self, client_id: int, current_user: User) -> Optional[Client]:
        pass
    
    def update_client(self, client_id: int, client_data: ClientUpdate, current_user: User) -> Client:
        pass
    
    def list_clients(self, current_user: User, filters: Optional[dict] = None) -> List[Client]:
        pass
```

---

## 7. Interface en ligne de commande

### 7.1. Développement de l'interface principale

Développer `cli/main.py` :

```python
import typer
from cli.commands import (
    auth_commands,
    user_commands,
    client_commands,
    contract_commands,
    event_commands
)

app = typer.Typer(
    name="epic-events",
    help="Système CRM pour Epic Events",
    add_completion=True,
)

# Ajout des sous-commandes
app.add_typer(auth_commands.app, name="auth", help="Gestion de l'authentification")
app.add_typer(user_commands.app, name="user", help="Gestion des utilisateurs")
app.add_typer(client_commands.app, name="client", help="Gestion des clients")
app.add_typer(contract_commands.app, name="contract", help="Gestion des contrats")
app.add_typer(event_commands.app, name="event", help="Gestion des événements")

if __name__ == "__main__":
    app()
```

### 7.2. Développement des commandes

Ordre de développement :

1. **Commandes d'authentification** (`cli/commands/auth_commands.py`)
2. **Commandes utilisateur** (`cli/commands/user_commands.py`)
3. **Commandes client** (`cli/commands/client_commands.py`)
4. **Commandes contrat** (`cli/commands/contract_commands.py`)
5. **Commandes événement** (`cli/commands/event_commands.py`)

### 7.3. Formatage avec Rich

Développer les modules de formatage :

1. **Styles** (`cli/formatters/styles.py`)
2. **Tables** (`cli/formatters/tables.py`)

### 7.4. Configuration du point d'entrée

Créer `setup.py` :

```python
from setuptools import setup, find_packages

setup(
    name="epic-events-crm",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy>=1.4.46",
        "typer[all]>=0.9.0",
        "rich>=13.7.0",
        "pydantic>=1.10.13",
        "passlib[bcrypt]>=1.7.4",
        "pyjwt>=2.8.0",
        "python-dotenv>=1.0.0",
        "loguru>=0.7.2",
        "sentry-sdk>=1.38.0",
        "alembic>=1.13.1",
    ],
    entry_points={
        "console_scripts": [
            "epic-events=cli.main:app",
        ],
    },
    python_requires=">=3.9",
)
```

Installation en mode développement :

```bash
pip install -e .
```

---

## 8. Tests unitaires

### 8.1. Configuration des tests

Développer `conftest.py` (à la racine) :

```python
import pytest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from crm.models.base import Base
from crm.database import get_db

# Configuration de test
os.environ["DATABASE_URL"] = "sqlite:///:memory:"

@pytest.fixture(scope="session")
def test_engine():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    return engine

@pytest.fixture(scope="function")
def db_session(test_engine):
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.rollback()
        session.close()

@pytest.fixture
def override_get_db(db_session):
    def _override_get_db():
        try:
            yield db_session
        finally:
            pass
    return _override_get_db
```

### 8.2. Tests des modèles

Créer `tests/unit/test_models.py` :

```python
import pytest
from crm.models.user import User
from crm.models.client import Client
from crm.models.enums import Role

def test_user_creation(db_session):
    user = User(
        first_name="John",
        last_name="Doe",
        email="john@example.com",
        hashed_password="hashed_password",
        role=Role.SALES
    )
    db_session.add(user)
    db_session.commit()
    
    assert user.id is not None
    assert user.email == "john@example.com"
    assert user.role == Role.SALES
```

### 8.3. Tests des services

Structure des tests pour chaque service :

```python
# tests/unit/test_client_service.py
import pytest
from crm.services.client import ClientService
from crm.schemas.client import ClientCreate

class TestClientService:
    def test_create_client(self, db_session, sample_user):
        service = ClientService(db_session)
        client_data = ClientCreate(
            full_name="Test Client",
            email="test@client.com",
            phone="1234567890",
            company_name="Test Company"
        )
        
        client = service.create_client(client_data, sample_user)
        
        assert client.id is not None
        assert client.full_name == "Test Client"
        assert client.sales_contact_id == sample_user.id
```

### 8.4. Tests de sécurité

Créer `tests/unit/test_security.py` :

```python
import pytest
from crm.security.auth import hash_password, verify_password, create_access_token, decode_token

def test_password_hashing():
    password = "secure_password123"
    hashed = hash_password(password)
    
    assert hashed != password
    assert verify_password(password, hashed) is True
    assert verify_password("wrong_password", hashed) is False

def test_jwt_tokens():
    data = {"sub": "test@example.com", "role": "SALES"}
    token = create_access_token(data)
    
    assert isinstance(token, str)
    assert len(token) > 0
    
    decoded = decode_token(token)
    assert decoded["sub"] == data["sub"]
    assert decoded["role"] == data["role"]
```

### 8.5. Exécution des tests unitaires

```bash
# Exécuter tous les tests unitaires
pytest tests/unit/ -v

# Exécuter avec couverture
pytest tests/unit/ --cov=crm --cov-report=html

# Exécuter un fichier de test spécifique
pytest tests/unit/test_models.py -v
```

---

## 9. Tests d'intégration

### 9.1. Configuration des tests d'intégration

Créer `tests/integration/conftest.py` :

```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crm.models.base import Base
from crm.models.user import User
from crm.models.enums import Role
from crm.security.auth import hash_password

@pytest.fixture(scope="module")
def integration_engine():
    engine = create_engine("sqlite:///./test_integration.db")
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def integration_db(integration_engine):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=integration_engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@pytest.fixture
def sample_users(integration_db):
    users = []
    for role in [Role.MANAGEMENT, Role.SALES, Role.SUPPORT]:
        user = User(
            first_name="Test",
            last_name=role.value,
            email=f"test_{role.value.lower()}@example.com",
            hashed_password=hash_password("password123"),
            role=role
        )
        integration_db.add(user)
        users.append(user)
    
    integration_db.commit()
    return users
```

### 9.2. Tests de flux complets

Créer `tests/integration/test_complete_workflow.py` :

```python
import pytest
from crm.services.auth import AuthService
from crm.services.client import ClientService
from crm.services.contract import ContractService
from crm.services.event import EventService
from crm.schemas.client import ClientCreate
from crm.schemas.contract import ContractCreate
from crm.schemas.event import EventCreate

class TestCompleteWorkflow:
    def test_client_contract_event_workflow(self, integration_db, sample_users):
        # Services
        auth_service = AuthService(integration_db)
        client_service = ClientService(integration_db)
        contract_service = ContractService(integration_db)
        event_service = EventService(integration_db)
        
        # Utilisateur commercial
        sales_user = next(u for u in sample_users if u.role.value == "SALES")
        
        # 1. Créer un client
        client_data = ClientCreate(
            full_name="Integration Test Client",
            email="integration@test.com",
            phone="1234567890",
            company_name="Test Company"
        )
        client = client_service.create_client(client_data, sales_user)
        
        # 2. Créer un contrat
        contract_data = ContractCreate(
            client_id=client.id,
            total_amount=10000.00,
            amount_due=5000.00
        )
        contract = contract_service.create_contract(contract_data, sales_user)
        
        # 3. Signer le contrat
        contract_service.update_contract_status(contract.id, True, sales_user)
        
        # 4. Créer un événement
        event_data = EventCreate(
            name="Test Event",
            contract_id=contract.id,
            client_contact="test@client.com",
            start_date="2024-06-01 10:00:00",
            end_date="2024-06-01 18:00:00",
            location="Test Location",
            attendees=50
        )
        event = event_service.create_event(event_data, sales_user)
        
        # Vérifications
        assert client.id is not None
        assert contract.id is not None
        assert contract.signed_status is True
        assert event.id is not None
        assert event.contract_id == contract.id
```

### 9.3. Tests de permissions

Créer `tests/integration/test_permissions.py` :

```python
import pytest
from crm.services.client import ClientService
from crm.schemas.client import ClientCreate
from crm.security.exceptions import PermissionDenied

class TestPermissions:
    def test_sales_cannot_modify_other_sales_clients(self, integration_db, sample_users):
        client_service = ClientService(integration_db)
        
        sales_user1 = sample_users[1]  # Premier commercial
        sales_user2 = User(
            first_name="Sales",
            last_name="User2",
            email="sales2@example.com",
            hashed_password=hash_password("password123"),
            role=Role.SALES
        )
        integration_db.add(sales_user2)
        integration_db.commit()
        
        # Sales1 crée un client
        client_data = ClientCreate(
            full_name="Sales1 Client",
            email="sales1client@test.com",
            phone="1234567890",
            company_name="Sales1 Company"
        )
        client = client_service.create_client(client_data, sales_user1)
        
        # Sales2 tente de modifier le client de Sales1
        with pytest.raises(PermissionDenied):
            client_service.update_client(
                client.id,
                {"full_name": "Modified by Sales2"},
                sales_user2
            )
```

### 9.4. Exécution des tests d'intégration

```bash
# Exécuter tous les tests d'intégration
pytest tests/integration/ -v

# Exécuter un test spécifique
pytest tests/integration/test_complete_workflow.py::TestCompleteWorkflow::test_client_contract_event_workflow -v

# Exécuter tous les tests
pytest tests/ -v --cov=crm
```

---

## 10. Documentation et finalisation

### 10.1. Tests de la CLI

Créer `tests/integration/test_cli.py` :

```python
import pytest
from typer.testing import CliRunner
from cli.main import app

runner = CliRunner()

class TestCLI:
    def test_help_command(self):
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "epic-events" in result.stdout
    
    def test_auth_login_command(self):
        # Test avec des entrées mockées
        pass
```

### 10.2. Génération de la documentation

```bash
# Installer les outils de documentation
pip install sphinx sphinx-rtd-theme

# Générer la documentation
sphinx-quickstart docs_auto
```

### 10.3. Script de déploiement

Créer `scripts/deploy.sh` :

```bash
#!/bin/bash

echo "Déploiement du CRM Epic Events"

# Vérifier Python
python3 --version

# Créer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Variables d'environnement
if [ ! -f .env ]; then
    echo "Créer le fichier .env basé sur .env.example"
    cp .env.example .env
fi

# Migrations de base de données
alembic upgrade head

# Installation en mode production
pip install -e .

echo "Déploiement terminé !"
```

### 10.4. Script de tests complets

Créer `scripts/run_tests.sh` :

```bash
#!/bin/bash

echo "Exécution de tous les tests"

# Tests de qualité de code
echo "Tests de qualité de code..."
black --check .
flake8 .
mypy crm/ cli/

# Tests unitaires
echo "Tests unitaires..."
pytest tests/unit/ -v --cov=crm --cov-report=html

# Tests d'intégration
echo "Tests d'intégration..."
pytest tests/integration/ -v

echo "Tous les tests terminés !"
```

### 10.5. Finalisation

```bash
# Rendre les scripts exécutables
chmod +x scripts/deploy.sh
chmod +x scripts/run_tests.sh

# Commit final
git add .
git commit -m "Implementation complete du CRM Epic Events"

# Tag de version
git tag -a v1.0.0 -m "Version 1.0.0 - CRM Epic Events"
```

---

## Checklist de développement

### Phase 1: Environnement
- [ ] Environnement virtuel créé
- [ ] Dépendances installées
- [ ] Configuration Git et pre-commit
- [ ] Structure de projet créée

### Phase 2: Base de données
- [ ] Modèles développés
- [ ] Migrations configurées
- [ ] Base de données initialisée

### Phase 3: Sécurité
- [ ] Système d'authentification
- [ ] Hachage des mots de passe
- [ ] Gestion des JWT
- [ ] Système de permissions

### Phase 4: Logique métier
- [ ] Services développés
- [ ] Schémas Pydantic
- [ ] Validation des données

### Phase 5: Interface
- [ ] CLI développée
- [ ] Commandes implémentées
- [ ] Formatage avec Rich

### Phase 6: Tests
- [ ] Tests unitaires
- [ ] Tests d'intégration
- [ ] Tests de la CLI
- [ ] Couverture de tests > 80%

### Phase 7: Finalisation
- [ ] Documentation mise à jour
- [ ] Scripts de déploiement
- [ ] Validation complète

Ce guide fournit une approche structurée et progressive pour développer le CRM Epic Events en suivant les meilleures pratiques de développement Python.


## 📋 Contenu du Guide de Développement
1. Préparation de l'environnement
   - Configuration Python et environnement virtuel
   - Installation des dépendances
   - Configuration Git et pre-commit hooks
   - Structure des fichiers de configuration

2. Structure du projet
   - Création de l'arborescence complète
   - Organisation modulaire du code
   - Configuration des packages Python

3. Configuration de base
   - Configuration de l'application avec variables d'environnement
   - Setup de la base de données avec SQLAlchemy
   - Configuration d'Alembic pour les migrations

4. Développement des modèles de données
   - Implémentation des modèles User, Client, Contract, Event
   - Relations et contraintes de base de données
   - Premières migrations

5. Système d'authentification et sécurité
   - Hachage des mots de passe avec Passlib
   - Gestion des JWT
   - Système de permissions basé sur les rôles
   - Configuration de la journalisation (Sentry + Loguru)

6. Développement des services métier
   - Pattern de développement pour chaque service
   - Validation avec Pydantic
   - Logique métier et permissions

7. Interface en ligne de commande
   - Développement avec Typer
   - Formatage avec Rich
   - Configuration du point d'entrée

8. Tests unitaires
   - Configuration pytest
   - Tests des modèles
   - Tests des services
   - Tests de sécurité
   
9. Tests d'intégration
   - Tests de flux complets
   - Tests de permissions
   - Tests de la CLI

10. Documentation et finalisation
   - Scripts de déploiement
   - Scripts de tests automatisés
   - Checklist de validation

🎯 Points forts du guide
    - Approche progressive : Chaque étape s'appuie sur la précédente
    - Exemples concrets : Code complet pour chaque composant
    - Bonnes pratiques : Configuration de qualité de code, tests, sécurité
    - Scripts automatisés : Déploiement et validation automatisés
    - Checklist : Validation de chaque phase de développement

Ce guide servira de référence complète pour implémenter le CRM Epic Events en suivant une méthodologie structurée et en respectant les meilleures pratiques de développement Python.

