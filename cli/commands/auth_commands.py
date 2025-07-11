"""
Commandes d'authentification pour la CLI.
"""

import typer
from typing import Optional
import getpass
from rich.console import Console
from cli.formatters.styles import print_success, print_error, print_info

app = typer.Typer(help="Gestion de l'authentification")
console = Console()


@app.command("login")
def login(
    email: str = typer.Option(..., prompt=True, help="Email de l'utilisateur"),
    password: Optional[str] = None,
):
    """Se connecter à l'application."""
    if not password:
        password = getpass.getpass("Mot de passe: ")

    # TODO: Logique d'authentification à implémenter
    # Exemple:
    # from crm.security import authenticate_user
    # user = authenticate_user(email, password)
    # if user:
    #     print_success(f"Connexion réussie! Bienvenue {user.first_name}!")
    # else:
    #     print_error("Échec de l'authentification. Vérifiez votre email et mot de passe.")

    # Simulation de connexion réussie pour le moment
    print_success(f"Connexion réussie avec l'email {email}!")


@app.command("logout")
def logout():
    """Se déconnecter de l'application."""
    # TODO: Logique de déconnexion à implémenter
    print_info("Déconnexion réussie. À bientôt!")


@app.command("whoami")
def whoami():
    """Affiche l'utilisateur actuellement connecté."""
    # TODO: Récupérer et afficher les informations de l'utilisateur connecté
    print_info("Vous êtes connecté en tant que [utilisateur]")


@app.command("change-password")
def change_password(
    current_password: str = typer.Option(
        ..., prompt=True, hide_input=True, help="Mot de passe actuel"
    ),
    new_password: str = typer.Option(
        ...,
        prompt=True,
        hide_input=True,
        confirmation_prompt=True,
        help="Nouveau mot de passe",
    ),
):
    """Change le mot de passe de l'utilisateur connecté."""
    # TODO: Logique de changement de mot de passe à implémenter
    print_success("Mot de passe changé avec succès!")
