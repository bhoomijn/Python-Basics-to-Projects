from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/")
def home():
    return {"status": "WhatsApp Bot is running"}


@app.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    form = await request.form()

    incoming_message = form.get("Body", "")
    sender = form.get("From", "")

    print(f"Message from {sender}: {incoming_message}")

    response = MessagingResponse()
    reply = response.message()

    text = incoming_message.lower().strip()

    if text in ["hi", "hello", "hey"]:
        reply.body("Hello! 👋 Main tumhara WhatsApp bot hoon.")

    elif text == "help":
        reply.body(
            "Commands:\n"
            "hi - Greeting\n"
            "help - Show commands"
        )

    else:
        reply.body(f"Tumne kaha: {incoming_message}")

    return PlainTextResponse(
        str(response),
        media_type="application/xml"
    )
