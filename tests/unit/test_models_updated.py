"""
Tests unitaires pour les modèles de données du CRM Epic Events.
"""

import pytest
from datetime import datetime, date
from decimal import Decimal
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from crm.models.base import Base
from crm.models.user import User, Role
from crm.models.client import Client
from crm.models.contract import Contract
from crm.models.event import Event


@pytest.fixture(scope="session")
def engine():
    """Créer une base de données en mémoire pour les tests."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    return engine


@pytest.fixture
def session(engine):
    """Créer une session de base de données pour chaque test."""
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()
    session.close()


@pytest.fixture
def sample_user(session):
    """Créer un utilisateur de test."""
    user = User(
        first_name="John",
        last_name="Doe",
        email="john.doe@epicevents.com",
        role=Role.SALES,
        hashed_password="hashed_password",
    )
    session.add(user)
    session.commit()
    return user


@pytest.fixture
def sample_client(session, sample_user):
    """Créer un client de test."""
    client = Client(
        company_name="Test Company",
        first_name="Jane",
        last_name="Smith",
        email="jane.smith@testcompany.com",
        phone="0123456789",
        sales_contact_id=sample_user.id,
    )
    session.add(client)
    session.commit()
    return client


@pytest.fixture
def sample_contract(session, sample_client):
    """Créer un contrat de test."""
    contract = Contract(
        client_id=sample_client.id,
        total_amount=Decimal("10000.00"),
        amount_due=Decimal("5000.00"),
        signed=True,
    )
    session.add(contract)
    session.commit()
    return contract


@pytest.fixture
def sample_event(session, sample_contract):
    """Créer un événement de test."""
    event = Event(
        contract_id=sample_contract.id,
        name="Test Event",
        start_date=date(2024, 6, 15),
        end_date=date(2024, 6, 16),
        location="Test Location",
        attendees=100,
        notes="Test notes",
    )
    session.add(event)
    session.commit()
    return event


class TestUser:
    """Tests pour le modèle User."""

    def test_user_creation(self, session):
        """Test la création d'un utilisateur."""
        user = User(
            first_name="Alice",
            last_name="Johnson",
            email="alice.johnson@epicevents.com",
            role=Role.MANAGEMENT,
            hashed_password="hashed_password",
        )
        session.add(user)
        session.commit()

        assert user.id is not None
        assert user.first_name == "Alice"
        assert user.last_name == "Johnson"
        assert user.email == "alice.johnson@epicevents.com"
        assert user.role == Role.MANAGEMENT
        assert user.created_at is not None
        assert user.updated_at is not None

    def test_user_full_name(self, sample_user):
        """Test la propriété full_name."""
        assert sample_user.full_name == "John Doe"

    def test_user_email_unique(self, session, sample_user):
        """Test l'unicité de l'email."""
        duplicate_user = User(
            first_name="Bob",
            last_name="Wilson",
            email=sample_user.email,  # Email dupliqué
            role=Role.SUPPORT,
            hashed_password="hashed_password",
        )
        session.add(duplicate_user)

        with pytest.raises(IntegrityError):
            session.commit()

    def test_user_repr(self, sample_user):
        """Test la représentation string."""
        expected = f"<User(id={sample_user.id}, email=john.doe@epicevents.com, role=Role.SALES)>"
        assert repr(sample_user) == expected


class TestClient:
    """Tests pour le modèle Client."""

    def test_client_creation(self, session, sample_user):
        """Test la création d'un client."""
        client = Client(
            company_name="New Company",
            first_name="Bob",
            last_name="Wilson",
            email="bob.wilson@newcompany.com",
            phone="0987654321",
            sales_contact_id=sample_user.id,
        )
        session.add(client)
        session.commit()

        assert client.id is not None
        assert client.company_name == "New Company"
        assert client.first_name == "Bob"
        assert client.last_name == "Wilson"
        assert client.email == "bob.wilson@newcompany.com"
        assert client.phone == "0987654321"
        assert client.sales_contact_id == sample_user.id
        assert client.created_at is not None
        assert client.updated_at is not None

    def test_client_sales_contact_relationship(self, sample_client, sample_user):
        """Test la relation avec le contact commercial."""
        assert sample_client.sales_contact == sample_user
        assert sample_client in sample_user.clients

    def test_client_email_unique(self, session, sample_client, sample_user):
        """Test l'unicité de l'email client."""
        duplicate_client = Client(
            company_name="Another Company",
            first_name="Charlie",
            last_name="Brown",
            email=sample_client.email,  # Email dupliqué
            phone="0555666777",
            sales_contact_id=sample_user.id,
        )
        session.add(duplicate_client)

        with pytest.raises(IntegrityError):
            session.commit()

    def test_client_repr(self, sample_client):
        """Test la représentation string."""
        expected = (
            f"<Client(id={sample_client.id}, company=Test Company, contact=Jane Smith)>"
        )
        assert repr(sample_client) == expected


class TestContract:
    """Tests pour le modèle Contract."""

    def test_contract_creation(self, session, sample_client):
        """Test la création d'un contrat."""
        contract = Contract(
            client_id=sample_client.id,
            total_amount=Decimal("15000.00"),
            amount_due=Decimal("10000.00"),
            signed=False,
        )
        session.add(contract)
        session.commit()

        assert contract.id is not None
        assert contract.client_id == sample_client.id
        assert contract.total_amount == Decimal("15000.00")
        assert contract.amount_due == Decimal("10000.00")
        assert contract.signed is False
        assert contract.created_at is not None
        assert contract.updated_at is not None

    def test_contract_is_paid_property(self, sample_contract):
        """Test la propriété is_paid."""
        assert sample_contract.is_paid is False

        sample_contract.amount_due = Decimal("0.00")
        assert sample_contract.is_paid is True

    def test_contract_payment_progress_property(self, sample_contract):
        """Test la propriété payment_progress."""
        # 5000 dû sur 10000 total = 50% payé
        assert sample_contract.payment_progress == 50.0

        sample_contract.amount_due = Decimal("0.00")
        assert sample_contract.payment_progress == 100.0

    def test_contract_amount_due_constraint(self, session, sample_client):
        """Test la contrainte amount_due <= total_amount."""
        contract = Contract(
            client_id=sample_client.id,
            total_amount=Decimal("10000.00"),
            amount_due=Decimal("15000.00"),  # Plus que le total
            signed=True,
        )
        session.add(contract)

        with pytest.raises(IntegrityError):
            session.commit()

    def test_contract_positive_amounts_constraint(self, session, sample_client):
        """Test les contraintes de positivité des montants."""
        contract = Contract(
            client_id=sample_client.id,
            total_amount=Decimal("-1000.00"),  # Négatif
            amount_due=Decimal("0.00"),
            signed=True,
        )
        session.add(contract)

        with pytest.raises(IntegrityError):
            session.commit()

    def test_contract_client_relationship(self, sample_contract, sample_client):
        """Test la relation avec le client."""
        assert sample_contract.client == sample_client
        assert sample_contract in sample_client.contracts

    def test_contract_repr(self, sample_contract):
        """Test la représentation string."""
        expected = f"<Contract(id={sample_contract.id}, client_id={sample_contract.client_id}, total=10000.00, signed=True)>"
        assert repr(sample_contract) == expected


class TestEvent:
    """Tests pour le modèle Event."""

    def test_event_creation(self, session, sample_contract):
        """Test la création d'un événement."""
        event = Event(
            contract_id=sample_contract.id,
            name="New Event",
            start_date=date(2024, 7, 1),
            end_date=date(2024, 7, 3),
            location="New Location",
            attendees=200,
            notes="New event notes",
        )
        session.add(event)
        session.commit()

        assert event.id is not None
        assert event.contract_id == sample_contract.id
        assert event.name == "New Event"
        assert event.start_date == date(2024, 7, 1)
        assert event.end_date == date(2024, 7, 3)
        assert event.location == "New Location"
        assert event.attendees == 200
        assert event.notes == "New event notes"
        assert event.created_at is not None
        assert event.updated_at is not None

    def test_event_duration_days_property(self, sample_event):
        """Test la propriété duration_days."""
        # Du 15 au 16 juin = 2 jours
        assert sample_event.duration_days == 2

    def test_event_has_support_assigned_property(self, sample_event):
        """Test la propriété has_support_assigned."""
        assert sample_event.has_support_assigned is False

        # Créer un utilisateur support et l'assigner
        support_user = User(
            first_name="Support",
            last_name="User",
            email="support@epicevents.com",
            role=Role.SUPPORT,
            password_hash="hashed_password",
        )
        sample_event.support_contact = support_user
        assert sample_event.has_support_assigned is True

    def test_event_date_constraint(self, session, sample_contract):
        """Test la contrainte end_date > start_date."""
        event = Event(
            contract_id=sample_contract.id,
            name="Invalid Event",
            start_date=date(2024, 6, 16),
            end_date=date(2024, 6, 15),  # Antérieure à start_date
            location="Test Location",
            attendees=50,
        )
        session.add(event)

        with pytest.raises(IntegrityError):
            session.commit()

    def test_event_positive_attendees_constraint(self, session, sample_contract):
        """Test la contrainte de positivité du nombre de participants."""
        event = Event(
            contract_id=sample_contract.id,
            name="Invalid Event",
            start_date=date(2024, 6, 15),
            end_date=date(2024, 6, 16),
            location="Test Location",
            attendees=-10,  # Négatif
        )
        session.add(event)

        with pytest.raises(IntegrityError):
            session.commit()

    def test_event_contract_relationship(self, sample_event, sample_contract):
        """Test la relation avec le contrat."""
        assert sample_event.contract == sample_contract
        assert sample_event in sample_contract.events

    def test_event_repr(self, sample_event):
        """Test la représentation string."""
        expected = f"<Event(id={sample_event.id}, name=Test Event, start=2024-06-15, location=Test Location)>"
        assert repr(sample_event) == expected


class TestRelationships:
    """Tests pour les relations entre modèles."""

    def test_cascade_delete_user_clients(self, session, sample_user):
        """Test la suppression en cascade des clients quand un utilisateur est supprimé."""
        # Créer un client lié à l'utilisateur
        client = Client(
            company_name="Test Company",
            first_name="Test",
            last_name="User",
            email="test@test.com",
            phone="0123456789",
            sales_contact_id=sample_user.id,
        )
        session.add(client)
        session.commit()

        client_id = client.id

        # Supprimer l'utilisateur
        session.delete(sample_user)
        session.commit()

        # Vérifier que le client a été supprimé aussi
        deleted_client = session.query(Client).filter_by(id=client_id).first()
        assert deleted_client is None

    def test_cascade_delete_client_contracts(self, session, sample_client):
        """Test la suppression en cascade des contrats quand un client est supprimé."""
        # Créer un contrat lié au client
        contract = Contract(
            client_id=sample_client.id,
            total_amount=Decimal("5000.00"),
            amount_due=Decimal("2500.00"),
            signed=True,
        )
        session.add(contract)
        session.commit()

        contract_id = contract.id

        # Supprimer le client
        session.delete(sample_client)
        session.commit()

        # Vérifier que le contrat a été supprimé aussi
        deleted_contract = session.query(Contract).filter_by(id=contract_id).first()
        assert deleted_contract is None

    def test_cascade_delete_contract_events(self, session, sample_contract):
        """Test la suppression en cascade des événements quand un contrat est supprimé."""
        # Créer un événement lié au contrat
        event = Event(
            contract_id=sample_contract.id,
            name="Test Event",
            start_date=date(2024, 8, 1),
            end_date=date(2024, 8, 2),
            location="Test Location",
            attendees=50,
        )
        session.add(event)
        session.commit()

        event_id = event.id

        # Supprimer le contrat
        session.delete(sample_contract)
        session.commit()

        # Vérifier que l'événement a été supprimé aussi
        deleted_event = session.query(Event).filter_by(id=event_id).first()
        assert deleted_event is None
