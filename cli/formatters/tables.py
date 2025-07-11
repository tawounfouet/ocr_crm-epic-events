"""
Formatage des tableaux pour l'affichage des données avec Rich.
"""

from rich.table import Table
from rich.console import Console

console = Console()


def create_users_table(users):
    """Crée un tableau pour afficher la liste des utilisateurs."""
    table = Table(title="Liste des Utilisateurs")

    # Définition des colonnes
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Nom", style="green")
    table.add_column("Email", style="green")
    table.add_column("Rôle", style="magenta")

    # Ajout des lignes
    for user in users:
        table.add_row(
            str(user.id),
            f"{user.first_name} {user.last_name}",
            user.email,
            user.role.name if hasattr(user, "role") and user.role else "Non défini",
        )

    return table


def create_clients_table(clients):
    """Crée un tableau pour afficher la liste des clients."""
    table = Table(title="Liste des Clients")

    # Définition des colonnes
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Entreprise", style="green")
    table.add_column("Contact", style="green")
    table.add_column("Email", style="blue")
    table.add_column("Téléphone", style="blue")
    table.add_column("Commercial", style="magenta")

    # Ajout des lignes
    for client in clients:
        table.add_row(
            str(client.id),
            client.company_name,
            f"{client.first_name} {client.last_name}",
            client.email,
            client.phone,
            (
                f"{client.sales_contact.first_name} {client.sales_contact.last_name}"
                if client.sales_contact
                else "Non assigné"
            ),
        )

    return table


def create_contracts_table(contracts):
    """Crée un tableau pour afficher la liste des contrats."""
    table = Table(title="Liste des Contrats")

    # Définition des colonnes
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Client", style="green")
    table.add_column("Montant total", style="yellow")
    table.add_column("Reste à payer", style="red")
    table.add_column("Signé", style="magenta")
    table.add_column("Commercial", style="blue")

    # Ajout des lignes
    for contract in contracts:
        table.add_row(
            str(contract.id),
            contract.client.company_name if contract.client else "Unknown",
            f"{contract.total_amount} €",
            f"{contract.amount_due} €",
            "✓" if contract.signed else "✗",
            (
                f"{contract.sales_contact.first_name} {contract.sales_contact.last_name}"
                if contract.sales_contact
                else "Non assigné"
            ),
        )

    return table


def create_events_table(events):
    """Crée un tableau pour afficher la liste des événements."""
    table = Table(title="Liste des Événements")

    # Définition des colonnes
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Client", style="green")
    table.add_column("Date début", style="yellow")
    table.add_column("Date fin", style="yellow")
    table.add_column("Support", style="magenta")
    table.add_column("Lieu", style="blue")
    table.add_column("Participants", style="blue")
    table.add_column("Notes", style="dim")

    # Ajout des lignes
    for event in events:
        table.add_row(
            str(event.id),
            (
                event.contract.client.company_name
                if event.contract and event.contract.client
                else "Unknown"
            ),
            str(event.start_date),
            str(event.end_date),
            (
                f"{event.support_contact.first_name} {event.support_contact.last_name}"
                if event.support_contact
                else "Non assigné"
            ),
            event.location,
            str(event.attendees),
            (
                event.notes[:20] + "..."
                if event.notes and len(event.notes) > 20
                else (event.notes or "")
            ),
        )

    return table
