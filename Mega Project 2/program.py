
def get_reply(message):
    message = message.lower().strip()

    if message in ["hi", "hello", "hey"]:
        return "Hello! 👋 Main tumhara WhatsApp Bot hoon."

    if message in ["help", "menu"]:
        return (
            "🤖 Bot Menu\n\n"
            "1. Hi - Greeting\n"
            "2. Help - Show menu\n"
            "3. About - Bot information"
        )

    if message == "about":
        return (
            "🤖 WhatsApp Bot\n"
            "Built with Python + FastAPI + WhatsApp Cloud API."
        )

    if "how are you" in message:
        return "I'm doing great! 😄"

    return (
        "Mujhe ye message samajh nahi aaya 😅\n"
        "Type 'help' to see available commands."
    )
