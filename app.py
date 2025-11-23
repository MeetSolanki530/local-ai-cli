# app.py - main entry point

from app.providers import choose_provider, load_models
from app.ui import show_welcome, show_model_list, choose_model
from app.chat import chat_loop


def main():
    show_welcome()

    provider_name, client = choose_provider()
    print(f"Using provider: {provider_name}")

    models = load_models(client)
    if not models:
        print("No models found!")
        return

    show_model_list(models)
    selected_model_id = choose_model(models)

    print(f"You selected: {selected_model_id}")

    chat_loop(selected_model_id, client)


if __name__ == "__main__":
    main()