#!/usr/bin/env python3
"""
Script de test pour vérifier que les modèles de données fonctionnent correctement
"""

import sys
import os
from datetime import datetime, timedelta

# Ajouter le répertoire racine au path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from crm.models import User, Client, Contract, Event, Role
from crm.database import SessionLocal, engine
from crm.models.base import Base


def test_models():
    """Test de création et de lecture des modèles"""

    # Créer une session de base de données
    db = SessionLocal()

    try:
        print("🔧 Test des modèles de données Epic Events CRM")
        print("=" * 50)

        # Test 1: Créer un utilisateur MANAGEMENT
        print("\n1. Création d'un utilisateur MANAGEMENT...")
        management_user = User(
            first_name="Alice",
            last_name="Manager",
            email="alice.manager@epicevents.com",
            phone="0123456789",
            hashed_password="hashed_password_here",
            role=Role.MANAGEMENT,
        )
        db.add(management_user)
        db.commit()
        db.refresh(management_user)
        print(f"✅ Utilisateur créé: {management_user}")

        # Test 2: Créer un utilisateur SALES
        print("\n2. Création d'un utilisateur SALES...")
        sales_user = User(
            first_name="Bob",
            last_name="Commercial",
            email="bob.commercial@epicevents.com",
            phone="0987654321",
            hashed_password="hashed_password_here",
            role=Role.SALES,
        )
        db.add(sales_user)
        db.commit()
        db.refresh(sales_user)
        print(f"✅ Utilisateur créé: {sales_user}")

        # Test 3: Créer un utilisateur SUPPORT
        print("\n3. Création d'un utilisateur SUPPORT...")
        support_user = User(
            first_name="Charlie",
            last_name="Support",
            email="charlie.support@epicevents.com",
            phone="0147258369",
            hashed_password="hashed_password_here",
            role=Role.SUPPORT,
        )
        db.add(support_user)
        db.commit()
        db.refresh(support_user)
        print(f"✅ Utilisateur créé: {support_user}")

        # Test 4: Créer un client
        print("\n4. Création d'un client...")
        client = Client(
            full_name="Jean Dupont",
            email="jean.dupont@startup.com",
            phone="0112233445",
            company_name="Startup Innovante",
            sales_contact_id=sales_user.id,
        )
        db.add(client)
        db.commit()
        db.refresh(client)
        print(f"✅ Client créé: {client}")

        # Test 5: Créer un contrat
        print("\n5. Création d'un contrat...")
        contract = Contract(
            client_id=client.id,
            sales_contact_id=sales_user.id,
            total_amount=15000.00,
            amount_due=7500.00,
            signed_status=True,
        )
        db.add(contract)
        db.commit()
        db.refresh(contract)
        print(f"✅ Contrat créé: {contract}")
        print(f"   💰 Progrès paiement: {contract.payment_progress}%")
        print(f"   ✅ Payé: {'Oui' if contract.is_paid else 'Non'}")

        # Test 6: Créer un événement
        print("\n6. Création d'un événement...")
        start_date = datetime.now() + timedelta(days=30)
        end_date = start_date + timedelta(days=2)

        event = Event(
            name="Conférence Startup 2025",
            contract_id=contract.id,
            client_id=client.id,
            client_contact="jean.dupont@startup.com",
            start_date=start_date,
            end_date=end_date,
            support_contact_id=support_user.id,
            location="Centre de Conférences Paris",
            attendees=150,
            notes="Événement de lancement avec démonstrations",
        )
        db.add(event)
        db.commit()
        db.refresh(event)
        print(f"✅ Événement créé: {event}")
        print(f"   📅 Durée: {event.duration_days} jours")
        print(f"   👥 Support assigné: {'Oui' if event.has_support_assigned else 'Non'}")

        # Test 7: Vérifier les relations
        print("\n7. Test des relations...")

        # Relation User -> Clients
        sales_clients = (
            db.query(Client).filter(Client.sales_contact_id == sales_user.id).all()
        )
        print(f"✅ Clients du commercial Bob: {len(sales_clients)} client(s)")

        # Relation Client -> Contracts
        client_contracts = (
            db.query(Contract).filter(Contract.client_id == client.id).all()
        )
        print(f"✅ Contrats du client: {len(client_contracts)} contrat(s)")

        # Relation Contract -> Events
        contract_events = db.query(Event).filter(Event.contract_id == contract.id).all()
        print(f"✅ Événements du contrat: {len(contract_events)} événement(s)")

        # Test 8: Propriétés et méthodes
        print("\n8. Test des propriétés...")
        print(f"✅ Nom complet utilisateur: {sales_user.full_name}")
        print(f"✅ Représentation client: {repr(client)}")
        print(f"✅ Représentation contrat: {repr(contract)}")
        print(f"✅ Représentation événement: {repr(event)}")

        print("\n🎉 Tous les tests sont passés avec succès !")
        print("📋 Résumé:")
        print(f"   👤 Utilisateurs créés: 3")
        print(f"   🏢 Clients créés: 1")
        print(f"   📄 Contrats créés: 1")
        print(f"   🎪 Événements créés: 1")

    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
        db.rollback()
        return False

    finally:
        db.close()

    return True


if __name__ == "__main__":
    # Vérifier que les tables existent
    Base.metadata.bind = engine

    success = test_models()
    sys.exit(0 if success else 1)
