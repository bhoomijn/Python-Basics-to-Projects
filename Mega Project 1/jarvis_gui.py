import pygame
import math
import sys
import threading
import psutil

from main import take_command, process_command


pygame.init()

WIDTH = 1100
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JARVIS AI Assistant")
clock = pygame.time.Clock()

# =========================
# FONTS
# =========================

title_font = pygame.font.Font(None, 58)
subtitle_font = pygame.font.Font(None, 28)
status_font = pygame.font.Font(None, 32)
text_font = pygame.font.Font(None, 25)
small_font = pygame.font.Font(None, 21)
button_font = pygame.font.Font(None, 24)

# =========================
# COLORS
# =========================

BG = (7, 11, 20)
PANEL = (15, 22, 36)
PANEL_2 = (20, 29, 47)
TEXT = (235, 245, 255)
MUTED = (140, 155, 175)
ACCENT = (0, 210, 255)
ACCENT_2 = (80, 120, 255)
SUCCESS = (80, 220, 150)

# =========================
# STATE
# =========================

running = True
status = "READY"
input_text = ""
response_text = "Welcome. How can I help you?"

chat_history = []

input_active = True
processing = False

# =========================
# BUTTONS
# =========================

input_box = pygame.Rect(40, 595, 700, 48)

send_button = pygame.Rect(755, 595, 135, 48)
mic_button = pygame.Rect(905, 595, 135, 48)

google_button = pygame.Rect(40, 525, 135, 42)
youtube_button = pygame.Rect(190, 525, 135, 42)
github_button = pygame.Rect(340, 525, 135, 42)
status_button = pygame.Rect(490, 525, 135, 42)

# =========================
# SYSTEM INFO
# =========================

def get_system_info():

    cpu = psutil.cpu_percent(interval=0.1)
    ram = psutil.virtual_memory().percent

    battery = psutil.sensors_battery()

    if battery:
        battery_percent = int(battery.percent)
    else:
        battery_percent = 0

    return cpu, ram, battery_percent


# =========================
# DRAW TEXT
# =========================

def draw_text(text, font, color, x, y):

    surface = font.render(str(text), True, color)
    screen.blit(surface, (x, y))


def draw_centered(text, font, color, y):

    surface = font.render(str(text), True, color)

    rect = surface.get_rect(
        center=(WIDTH // 2, y)
    )

    screen.blit(surface, rect)


# =========================
# ORB
# =========================

def draw_orb(x, y, time):

    pulse = math.sin(time * 0.004) * 8

    for radius in (
        105 + pulse,
        85 + pulse / 2,
        65
    ):

        pygame.draw.circle(
            screen,
            ACCENT,
            (x, y),
            int(radius),
            2
        )

    pygame.draw.circle(
        screen,
        PANEL,
        (x, y),
        52
    )

    pygame.draw.circle(
        screen,
        ACCENT,
        (x, y),
        48,
        3
    )

    pygame.draw.circle(
        screen,
        ACCENT_2,
        (x, y),
        18
    )


# =========================
# ADD CHAT
# =========================

def add_chat(user, assistant):

    chat_history.append(
        ("YOU", user)
    )

    chat_history.append(
        ("JARVIS", assistant)
    )

    if len(chat_history) > 6:
        del chat_history[:-6]


# =========================
# COMMAND WORKER
# =========================

def execute_command(command):

    global response_text
    global status
    global processing
    global input_text

    if not command.strip():
        return

    processing = True
    status = "THINKING..."
    response_text = "Processing..."

    try:

        result = process_command(command)

        if result == "__EXIT__":

            processing = False
            return "__EXIT__"

        if result:

            response_text = str(result)

            add_chat(
                command,
                response_text
            )

        else:

            response_text = "Command completed."

            add_chat(
                command,
                response_text
            )

    except Exception as e:

        print("Command Error:", e)

        response_text = "Something went wrong."

        add_chat(
            command,
            response_text
        )

    status = "READY"
    processing = False
    input_text = ""

    return response_text


# =========================
# TYPED COMMAND
# =========================

def send_command():

    global input_text

    command = input_text.strip()

    if not command:
        return

    thread = threading.Thread(
        target=execute_command,
        args=(command,),
        daemon=True
    )

    thread.start()


# =========================
# VOICE COMMAND
# =========================

def voice_command():

    global status
    global response_text
    global processing

    if processing:
        return

    status = "LISTENING..."
    response_text = "Listening..."

    def voice_worker():

        global status
        global response_text
        global processing

        processing = True

        try:

            command = take_command()

            if command:

                execute_command(command)

            else:

                response_text = "I didn't hear anything."
                status = "READY"

        except Exception as e:

            print("Voice Error:", e)

            response_text = "Voice input failed."
            status = "READY"

        processing = False

    thread = threading.Thread(
        target=voice_worker,
        daemon=True
    )

    thread.start()


# =========================
# QUICK COMMAND
# =========================

def quick_command(command):

    thread = threading.Thread(
        target=execute_command,
        args=(command,),
        daemon=True
    )

    thread.start()


# =========================
# MAIN LOOP
# =========================

while running:

    current_time = pygame.time.get_ticks()

    cpu, ram, battery = get_system_info()

    # =====================
    # EVENTS
    # =====================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if input_box.collidepoint(event.pos):

                input_active = True

            elif send_button.collidepoint(event.pos):

                send_command()

            elif mic_button.collidepoint(event.pos):

                voice_command()

            elif google_button.collidepoint(event.pos):

                quick_command("open google")

            elif youtube_button.collidepoint(event.pos):

                quick_command("open youtube")

            elif github_button.collidepoint(event.pos):

                quick_command("open github")

            elif status_button.collidepoint(event.pos):

                quick_command("system status")

            else:

                input_active = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                running = False

            elif event.key == pygame.K_RETURN:

                if input_active:
                    send_command()

            elif event.key == pygame.K_BACKSPACE:

                if input_active:
                    input_text = input_text[:-1]

            else:

                if input_active and event.unicode:

                    if len(input_text) < 100:

                        input_text += event.unicode

    # =====================
    # BACKGROUND
    # =====================

    screen.fill(BG)

    # =====================
    # HEADER
    # =====================

    draw_centered(
        "J A R V I S",
        title_font,
        TEXT,
        45
    )

    draw_centered(
        "PERSONAL AI DESKTOP ASSISTANT",
        subtitle_font,
        MUTED,
        82
    )

    # =====================
    # SYSTEM PANEL
    # =====================

    pygame.draw.rect(
        screen,
        PANEL,
        (30, 110, 250, 145),
        border_radius=18
    )

    draw_text(
        "SYSTEM MONITOR",
        button_font,
        ACCENT,
        50,
        130
    )

    draw_text(
        f"CPU       {cpu:.0f}%",
        text_font,
        TEXT,
        50,
        165
    )

    draw_text(
        f"RAM       {ram:.0f}%",
        text_font,
        TEXT,
        50,
        195
    )

    draw_text(
        f"BATTERY   {battery}%",
        text_font,
        TEXT,
        50,
        225
    )

    # =====================
    # ORB
    # =====================

    draw_orb(
        WIDTH // 2,
        275,
        current_time
    )

    # =====================
    # STATUS
    # =====================

    draw_centered(
        status,
        status_font,
        ACCENT,
        395
    )

    # =====================
    # RESPONSE
    # =====================

    pygame.draw.rect(
        screen,
        PANEL,
        (320, 425, 740, 82),
        border_radius=15
    )

    display_response = response_text

    if len(display_response) > 90:

        display_response = (
            display_response[:90] + "..."
        )

    draw_text(
        display_response,
        text_font,
        TEXT,
        340,
        455
    )

    # =====================
    # QUICK BUTTONS
    # =====================

    buttons = [
        (google_button, "GOOGLE"),
        (youtube_button, "YOUTUBE"),
        (github_button, "GITHUB"),
        (status_button, "SYSTEM")
    ]

    for rect, label in buttons:

        pygame.draw.rect(
            screen,
            PANEL_2,
            rect,
            border_radius=10
        )

        pygame.draw.rect(
            screen,
            ACCENT,
            rect,
            1,
            border_radius=10
        )

        surface = button_font.render(
            label,
            True,
            TEXT
        )

        screen.blit(
            surface,
            surface.get_rect(
                center=rect.center
            )
        )

    # =====================
    # INPUT
    # =====================

    pygame.draw.rect(
        screen,
        PANEL,
        input_box,
        border_radius=12
    )

    pygame.draw.rect(
        screen,
        ACCENT if input_active else MUTED,
        input_box,
        2,
        border_radius=12
    )

    if input_text:

        draw_text(
            input_text,
            text_font,
            TEXT,
            input_box.x + 15,
            input_box.y + 13
        )

    else:

        draw_text(
            "Type your command...",
            text_font,
            MUTED,
            input_box.x + 15,
            input_box.y + 13
        )

    # =====================
    # SEND
    # =====================

    pygame.draw.rect(
        screen,
        ACCENT_2,
        send_button,
        border_radius=12
    )

    draw_centered(
        "SEND",
        button_font,
        TEXT,
        send_button.centery
    )

    # =====================
    # MIC
    # =====================

    pygame.draw.rect(
        screen,
        ACCENT,
        mic_button,
        border_radius=12
    )

    draw_centered(
        "🎙 MIC",
        button_font,
        BG,
        mic_button.centery
    )

    # =====================
    # CHAT HISTORY
    # =====================

    pygame.draw.rect(
        screen,
        PANEL,
        (760, 110, 300, 295),
        border_radius=18
    )

    draw_text(
        "RECENT ACTIVITY",
        button_font,
        ACCENT,
        785,
        130
    )

    y = 165

    for speaker, message in chat_history:

        short_message = message

        if len(short_message) > 32:

            short_message = (
                short_message[:32] + "..."
            )

        draw_text(
            speaker + ":",
            small_font,
            ACCENT if speaker == "JARVIS" else MUTED,
            785,
            y
        )

        y += 23

        draw_text(
            short_message,
            small_font,
            TEXT,
            785,
            y
        )

        y += 38

    # =====================
    # FOOTER
    # =====================

    draw_centered(
        "Python  •  Pygame  •  Groq AI  •  System Monitor",
        small_font,
        MUTED,
        680
    )

    pygame.display.flip()

    clock.tick(30)


pygame.quit()
sys.exit()
