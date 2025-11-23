# app/ui.py - UI helpers and model selection

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()


def show_welcome():
    console.clear()
    console.print(
        Panel.fit(
            "[bold cyan]🤖 Welcome to the CLI Chat Bot[/bold cyan]\n"
            "[yellow]Choose your AI Provider[/yellow]",
            title="[bold green]AI Terminal[/bold green]",
            border_style="bright_blue",
        )
    )


def show_model_list(models):
    console.print("\n[bold yellow]Available Models:[/bold yellow]\n")
    for idx, model in enumerate(models, start=1):
        console.print(f"[cyan]{idx}.[/cyan] {model.id}")
    console.print()


def choose_model(models):
    while True:
        choice = Prompt.ask("[bold green]Choose a model number[/bold green]")
        if choice.isdigit() and 1 <= int(choice) <= len(models):
            return models[int(choice) - 1].id
        console.print("[bold red]Invalid choice! Try again.[/bold red]")