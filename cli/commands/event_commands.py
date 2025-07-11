"""
Commandes de gestion des événements pour la CLI.
"""

import typer
from typing import Optional
from datetime import datetime
from rich.console import Console
from cli.formatters.styles import print_success, print_error, print_info, print_title
from cli.formatters.tables import create_events_table

app = typer.Typer(help="Gestion des événements")
console = Console()


@app.command("list")
def list_events(
    client_id: Optional[int] = typer.Option(None, help="Filtrer par ID client"),
    support_id: Optional[int] = typer.Option(None, help="Filtrer par ID support"),
    future_only: bool = typer.Option(
        False, help="Afficher uniquement les événements futurs"
    ),
):
    """Liste tous les événements."""
    # TODO: Logique pour récupérer et afficher les événements
    print_title("Liste des événements")

    filters = []
    if client_id:
        filters.append(f"client_id={client_id}")
    if support_id:
        filters.append(f"support_id={support_id}")
    if future_only:
        filters.append("événements futurs uniquement")

    if filters:
        print_info(f"Filtres appliqués: {', '.join(filters)}")

    print_info(
        "Fonctionnalité non implémentée: Cette commande affichera la liste des événements."
    )


@app.command("create")
def create_event(
    contract_id: int = typer.Option(..., prompt=True, help="ID du contrat associé"),
    start_date: datetime = typer.Option(
        ...,
        prompt=True,
        formats=["%Y-%m-%d %H:%M"],
        help="Date et heure de début (YYYY-MM-DD HH:MM)",
    ),
    end_date: datetime = typer.Option(
        ...,
        prompt=True,
        formats=["%Y-%m-%d %H:%M"],
        help="Date et heure de fin (YYYY-MM-DD HH:MM)",
    ),
    location: str = typer.Option(..., prompt=True, help="Lieu de l'événement"),
    attendees: int = typer.Option(
        ..., prompt=True, help="Nombre de participants attendus"
    ),
    notes: Optional[str] = typer.Option(None, help="Notes supplémentaires"),
    support_contact_id: Optional[int] = typer.Option(
        None, help="ID du contact support"
    ),
):
    """Crée un nouvel événement."""
    # TODO: Logique pour créer un événement
    print_success(f"Événement créé avec succès pour le contrat {contract_id}!")
    print_info(
        f"Date: {start_date.strftime('%Y-%m-%d %H:%M')} à {end_date.strftime('%Y-%m-%d %H:%M')} | Lieu: {location}"
    )


@app.command("show")
def show_event(
    event_id: int = typer.Argument(..., help="ID de l'événement à afficher")
):
    """Affiche les détails d'un événement spécifique."""
    # TODO: Logique pour récupérer et afficher un événement spécifique
    print_title(f"Détails de l'événement {event_id}")
    print_info(
        "Fonctionnalité non implémentée: Cette commande affichera les détails d'un événement spécifique."
    )


@app.command("update")
def update_event(
    event_id: int = typer.Argument(..., help="ID de l'événement à mettre à jour"),
    start_date: Optional[datetime] = typer.Option(
        None,
        formats=["%Y-%m-%d %H:%M"],
        help="Date et heure de début (YYYY-MM-DD HH:MM)",
    ),
    end_date: Optional[datetime] = typer.Option(
        None, formats=["%Y-%m-%d %H:%M"], help="Date et heure de fin (YYYY-MM-DD HH:MM)"
    ),
    location: Optional[str] = typer.Option(None, help="Lieu de l'événement"),
    attendees: Optional[int] = typer.Option(
        None, help="Nombre de participants attendus"
    ),
    notes: Optional[str] = typer.Option(None, help="Notes supplémentaires"),
    support_contact_id: Optional[int] = typer.Option(
        None, help="ID du contact support"
    ),
):
    """Met à jour les informations d'un événement."""
    # TODO: Logique pour mettre à jour un événement
    print_success(f"Événement {event_id} mis à jour avec succès!")


@app.command("assign-support")
def assign_support(
    event_id: int = typer.Argument(..., help="ID de l'événement"),
    support_id: int = typer.Option(
        ..., prompt=True, help="ID du contact support à assigner"
    ),
):
    """Assigne un contact support à un événement."""
    # TODO: Logique pour assigner un support à un événement
    print_success(f"Contact support {support_id} assigné à l'événement {event_id}!")


@app.command("delete")
def delete_event(
    event_id: int = typer.Argument(..., help="ID de l'événement à supprimer"),
    confirm: bool = typer.Option(
        False, "--yes", "-y", help="Confirmer la suppression sans prompt"
    ),
):
    """Supprime un événement."""
    if not confirm:
        confirm = typer.confirm(
            f"Êtes-vous sûr de vouloir supprimer l'événement {event_id}?"
        )
        if not confirm:
            print_info("Suppression annulée.")
            return

    # TODO: Logique pour supprimer un événement
    print_success(f"Événement {event_id} supprimé avec succès!")
