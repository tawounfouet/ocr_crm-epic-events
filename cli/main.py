import typer
from rich.console import Console
from cli.commands import (
    auth_commands,
    user_commands,
    client_commands,
    contract_commands,
    event_commands,
)
from cli.formatters.styles import print_title

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


@app.callback()
def main():
    """
    Epic Events CRM - Système de gestion de la relation client pour Epic Events.

    Utilisez les sous-commandes pour gérer les différentes entités du CRM.
    """
    console = Console()
    print_title("Epic Events CRM")


if __name__ == "__main__":
    app()
