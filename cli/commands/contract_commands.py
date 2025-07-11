"""
Commandes de gestion des contrats pour la CLI.
"""

import typer
from typing import Optional
from datetime import datetime
from rich.console import Console
from cli.formatters.styles import print_success, print_error, print_info, print_title
from cli.formatters.tables import create_contracts_table

app = typer.Typer(help="Gestion des contrats")
console = Console()


@app.command("list")
def list_contracts(
    client_id: Optional[int] = typer.Option(None, help="Filtrer par ID client"),
    signed: Optional[bool] = typer.Option(
        None, help="Filtrer par statut de signature (signé ou non)"
    ),
):
    """Liste tous les contrats."""
    # TODO: Logique pour récupérer et afficher les contrats
    print_title("Liste des contrats")

    filters = []
    if client_id:
        filters.append(f"client_id={client_id}")
    if signed is not None:
        filters.append(f"signed={'oui' if signed else 'non'}")

    if filters:
        print_info(f"Filtres appliqués: {', '.join(filters)}")

    print_info(
        "Fonctionnalité non implémentée: Cette commande affichera la liste des contrats."
    )


@app.command("create")
def create_contract(
    client_id: int = typer.Option(..., prompt=True, help="ID du client"),
    total_amount: float = typer.Option(
        ..., prompt=True, help="Montant total du contrat"
    ),
    amount_paid: Optional[float] = typer.Option(0.0, help="Montant déjà payé"),
    signed: bool = typer.Option(False, help="Le contrat est-il déjà signé?"),
    sales_contact_id: Optional[int] = typer.Option(
        None, help="ID du commercial responsable"
    ),
):
    """Crée un nouveau contrat."""
    ## A Faire: Logique pour créer un contrat
    paid = amount_paid if amount_paid is not None else 0.0
    amount_due = total_amount - paid
    print_success(f"Contrat créé avec succès pour le client {client_id}!")
    print_info(
        f"Montant total: {total_amount} € | Reste à payer: {amount_due} € | Signé: {'Oui' if signed else 'Non'}"
    )


@app.command("show")
def show_contract(
    contract_id: int = typer.Argument(..., help="ID du contrat à afficher")
):
    """Affiche les détails d'un contrat spécifique."""
    # TODO: Logique pour récupérer et afficher un contrat spécifique
    print_title(f"Détails du contrat {contract_id}")
    print_info(
        "Fonctionnalité non implémentée: Cette commande affichera les détails d'un contrat spécifique."
    )


@app.command("update")
def update_contract(
    contract_id: int = typer.Argument(..., help="ID du contrat à mettre à jour"),
    total_amount: Optional[float] = typer.Option(None, help="Montant total du contrat"),
    amount_paid: Optional[float] = typer.Option(None, help="Montant déjà payé"),
    signed: Optional[bool] = typer.Option(None, help="Le contrat est-il signé?"),
    sales_contact_id: Optional[int] = typer.Option(
        None, help="ID du commercial responsable"
    ),
):
    """Met à jour les informations d'un contrat."""
    # TODO: Logique pour mettre à jour un contrat
    print_success(f"Contrat {contract_id} mis à jour avec succès!")


@app.command("sign")
def sign_contract(
    contract_id: int = typer.Argument(..., help="ID du contrat à signer")
):
    """Marque un contrat comme signé."""
    # TODO: Logique pour signer un contrat
    print_success(f"Contrat {contract_id} signé avec succès!")


@app.command("payment")
def register_payment(
    contract_id: int = typer.Argument(..., help="ID du contrat"),
    amount: float = typer.Option(..., prompt=True, help="Montant du paiement"),
):
    """Enregistre un paiement pour un contrat."""
    # TODO: Logique pour enregistrer un paiement
    print_success(f"Paiement de {amount} € enregistré pour le contrat {contract_id}!")


@app.command("delete")
def delete_contract(
    contract_id: int = typer.Argument(..., help="ID du contrat à supprimer"),
    confirm: bool = typer.Option(
        False, "--yes", "-y", help="Confirmer la suppression sans prompt"
    ),
):
    """Supprime un contrat."""
    if not confirm:
        confirm = typer.confirm(
            f"Êtes-vous sûr de vouloir supprimer le contrat {contract_id}?"
        )
        if not confirm:
            print_info("Suppression annulée.")
            return

    # TODO: Logique pour supprimer un contrat
    print_success(f"Contrat {contract_id} supprimé avec succès!")
