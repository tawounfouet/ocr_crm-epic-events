"""
Commandes de gestion des utilisateurs pour la CLI.
"""

import typer
from typing import Optional
from rich.console import Console
from cli.formatters.styles import print_success, print_error, print_info, print_title
from cli.formatters.tables import create_users_table

app = typer.Typer(help="Gestion des utilisateurs")
console = Console()


@app.command("list")
def list_users():
    """Liste tous les utilisateurs."""
    # TODO: Logique pour récupérer et afficher les utilisateurs
    # Exemple:
    # from crm.services.user_service import get_all_users
    # users = get_all_users()
    # if users:
    #     table = create_users_table(users)
    #     console.print(table)
    # else:
    #     print_info("Aucun utilisateur trouvé.")

    print_title("Liste des utilisateurs")
    print_info(
        "Fonctionnalité non implémentée: Cette commande affichera la liste des utilisateurs."
    )


@app.command("create")
def create_user(
    email: str = typer.Option(..., prompt=True, help="Email de l'utilisateur"),
    first_name: str = typer.Option(..., prompt=True, help="Prénom"),
    last_name: str = typer.Option(..., prompt=True, help="Nom de famille"),
    role: str = typer.Option(
        ..., prompt=True, help="Rôle (management, sales, support)"
    ),
    password: str = typer.Option(
        ..., prompt=True, hide_input=True, confirmation_prompt=True, help="Mot de passe"
    ),
):
    """Crée un nouvel utilisateur."""
    # TODO: Logique pour créer un utilisateur
    # Exemple:
    # from crm.services.user_service import create_user
    # success = create_user(email=email, first_name=first_name, last_name=last_name, role=role, password=password)
    # if success:
    #     print_success(f"L'utilisateur {first_name} {last_name} a été créé avec succès!")
    # else:
    #     print_error("Erreur lors de la création de l'utilisateur.")

    print_success(
        f"Utilisateur {first_name} {last_name} créé avec succès avec le rôle {role}!"
    )


@app.command("show")
def show_user(
    user_id: int = typer.Argument(..., help="ID de l'utilisateur à afficher")
):
    """Affiche les détails d'un utilisateur spécifique."""
    # TODO: Logique pour récupérer et afficher un utilisateur spécifique
    print_title(f"Détails de l'utilisateur {user_id}")
    print_info(
        "Fonctionnalité non implémentée: Cette commande affichera les détails d'un utilisateur spécifique."
    )


@app.command("update")
def update_user(
    user_id: int = typer.Argument(..., help="ID de l'utilisateur à mettre à jour"),
    email: Optional[str] = typer.Option(None, help="Email de l'utilisateur"),
    first_name: Optional[str] = typer.Option(None, help="Prénom"),
    last_name: Optional[str] = typer.Option(None, help="Nom de famille"),
    role: Optional[str] = typer.Option(None, help="Rôle (management, sales, support)"),
):
    """Met à jour les informations d'un utilisateur."""
    # TODO: Logique pour mettre à jour un utilisateur
    print_success(f"Utilisateur {user_id} mis à jour avec succès!")


@app.command("delete")
def delete_user(
    user_id: int = typer.Argument(..., help="ID de l'utilisateur à supprimer"),
    confirm: bool = typer.Option(
        False, "--yes", "-y", help="Confirmer la suppression sans prompt"
    ),
):
    """Supprime un utilisateur."""
    if not confirm:
        confirm = typer.confirm(
            f"Êtes-vous sûr de vouloir supprimer l'utilisateur {user_id}?"
        )
        if not confirm:
            print_info("Suppression annulée.")
            return

    # TODO: Logique pour supprimer un utilisateur
    print_success(f"Utilisateur {user_id} supprimé avec succès!")
