"""
Styles pour l'affichage des sorties CLI avec Rich.
"""

from rich.style import Style
from rich.console import Console

# Création d'une console personnalisée
console = Console()

# Styles pour les différents éléments d'interface
TITLE_STYLE = Style(color="blue", bold=True)
SUCCESS_STYLE = Style(color="green", bold=True)
ERROR_STYLE = Style(color="red", bold=True)
WARNING_STYLE = Style(color="yellow")
INFO_STYLE = Style(color="cyan")
HEADER_STYLE = Style(color="magenta", bold=True)


# Fonctions utilitaires pour l'affichage
def print_title(message):
    """Affiche un titre."""
    console.print(message, style=TITLE_STYLE)


def print_success(message):
    """Affiche un message de succès."""
    console.print(message, style=SUCCESS_STYLE)


def print_error(message):
    """Affiche un message d'erreur."""
    console.print(message, style=ERROR_STYLE)


def print_warning(message):
    """Affiche un avertissement."""
    console.print(message, style=WARNING_STYLE)


def print_info(message):
    """Affiche une information."""
    console.print(message, style=INFO_STYLE)
