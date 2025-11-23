# app/chat.py - Chat loop + streaming markdown render

from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()


def chat_loop(model_id, client):
    console.print(
        Panel(
            f"Chat started with model: [bold cyan]{model_id}[/bold cyan]\n"
            "[green]Type your message. Type 'exit' or 'bye' to stop.[/green]",
            border_style="cyan",
        )
    )

    history = []

    while True:
        user_input = Prompt.ask("[bold magenta]You[/bold magenta]")

        if user_input.lower() in ["exit", "bye"]:
            console.print("[bold red]Chat ended. Goodbye![/bold red]")
            break

        history.append({"role": "user", "content": user_input})
        console.print("\n[bold blue]Bot:[/bold blue]\n")

        response_stream = client.chat.completions.create(
            model=model_id,
            messages=history,
            stream=True
        )

        bot_reply = ""

        with Live(Markdown(""), refresh_per_second=10, console=console) as live:
            for chunk in response_stream:
                if chunk.choices and chunk.choices[0].delta.content:
                    chunk_text = chunk.choices[0].delta.content
                    bot_reply += chunk_text
                    live.update(Markdown(bot_reply))

        console.print()
        history.append({"role": "assistant", "content": bot_reply})
