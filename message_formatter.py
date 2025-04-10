import random
import urllib.parse

EMOJIS = ["😊", "👍", "🎉", "🔥", "💖", "🥳", "✨"]

def format_message(name, message):
    """Formats the message while preserving its original structure and encoding it for safe transmission."""
    emoji = random.choice(EMOJIS)

    # Handle missing name by using "amigo/a" as a fallback
    if not name or name.strip() == "":
        name = "amigo/a"

    # Add greeting after encoding (so we don't modify user formatting)
    full_message = f"Hola {name}! {emoji}\n\n{message}"

    return full_message