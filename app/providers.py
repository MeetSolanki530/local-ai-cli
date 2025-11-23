# app/providers.py - AI provider selection & model loading

from rich.console import Console
from rich.prompt import Prompt
from openai import OpenAI

console = Console()

PROVIDERS = {
    "Ollama": {
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama-key"
    },
    "LMStudio": {
        "base_url": "http://localhost:1234/v1",
        "api_key": "lm-studio"
    },
    "LocalAI (Mudler)": {
        "base_url": "http://localhost:8080/v1",
        "api_key": "localai-key"
    }
}


def choose_provider():
    console.print("\n[bold yellow]Available Providers:[/bold yellow]\n")
    provider_list = list(PROVIDERS.keys())

    for idx, name in enumerate(provider_list, start=1):
        console.print(f"[cyan]{idx}.[/cyan] {name}")

    while True:
        choice = Prompt.ask("[bold green]Choose a provider number[/bold green]")

        if choice.isdigit() and 1 <= int(choice) <= len(provider_list):
            provider = provider_list[int(choice) - 1]
            config = PROVIDERS[provider]
            client = OpenAI(api_key=config["api_key"], base_url=config["base_url"])
            return provider, client

        console.print("[bold red]Invalid choice! Try again.[/bold red]")


def load_models(client):
    console.print("[bold green]Fetching models from provider...[/bold green]")
    models = client.models.list().data
    return models