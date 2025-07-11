"""
Commandes de gestion des clients pour la CLI.
"""

import typer
from typing import Optional
from rich.console import Console
from cli.formatters.styles import print_success, print_error, print_info, print_title
from cli.formatters.tables import create_clients_table

app = typer.Typer(help="Gestion des clients")
console = Console()


@app.command("list")
def list_clients():
    """Liste tous les clients."""
    # TODO: Logique pour récupérer et afficher les clients
    # Exemple:
    # from crm.services.client_service import get_all_clients
    # clients = get_all_clients()
    # if clients:
    #     table = create_clients_table(clients)
    #     console.print(table)
    # else:
    #     print_info("Aucun client trouvé.")

    print_title("Liste des clients")
    print_info(
        "Fonctionnalité non implémentée: Cette commande affichera la liste des clients."
    )


@app.command("create")
def create_client(
    company_name: str = typer.Option(..., prompt=True, help="Nom de l'entreprise"),
    first_name: str = typer.Option(..., prompt=True, help="Prénom du contact"),
    last_name: str = typer.Option(..., prompt=True, help="Nom de famille du contact"),
    email: str = typer.Option(..., prompt=True, help="Email du contact"),
    phone: str = typer.Option(..., prompt=True, help="Numéro de téléphone du contact"),
    sales_contact_id: Optional[int] = typer.Option(
        None, help="ID du commercial responsable"
    ),
):
    """Crée un nouveau client."""
    # TODO: Logique pour créer un client
    print_success(f"Client {company_name} créé avec succès!")


@app.command("show")
def show_client(client_id: int = typer.Argument(..., help="ID du client à afficher")):
    """Affiche les détails d'un client spécifique."""
    # TODO: Logique pour récupérer et afficher un client spécifique
    print_title(f"Détails du client {client_id}")
    print_info(
        "Fonctionnalité non implémentée: Cette commande affichera les détails d'un client spécifique."
    )


@app.command("update")
def update_client(
    client_id: int = typer.Argument(..., help="ID du client à mettre à jour"),
    company_name: Optional[str] = typer.Option(None, help="Nom de l'entreprise"),
    first_name: Optional[str] = typer.Option(None, help="Prénom du contact"),
    last_name: Optional[str] = typer.Option(None, help="Nom de famille du contact"),
    email: Optional[str] = typer.Option(None, help="Email du contact"),
    phone: Optional[str] = typer.Option(None, help="Numéro de téléphone du contact"),
    sales_contact_id: Optional[int] = typer.Option(
        None, help="ID du commercial responsable"
    ),
):
    """Met à jour les informations d'un client."""
    # TODO: Logique pour mettre à jour un client
    print_success(f"Client {client_id} mis à jour avec succès!")


@app.command("delete")
def delete_client(
    client_id: int = typer.Argument(..., help="ID du client à supprimer"),
    confirm: bool = typer.Option(
        False, "--yes", "-y", help="Confirmer la suppression sans prompt"
    ),
):
    """Supprime un client."""
    if not confirm:
        confirm = typer.confirm(
            f"Êtes-vous sûr de vouloir supprimer le client {client_id}?"
        )
        if not confirm:
            print_info("Suppression annulée.")
            return

    # TODO: Logique pour supprimer un client
    print_success(f"Client {client_id} supprimé avec succès!")
