
import pygame
import math
import sys

from main import take_command, process_command


# =========================================================
# INITIALIZE PYGAME
# =========================================================

pygame.init()

WIDTH = 1100
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JARVIS AI Assistant")

clock = pygame.time.Clock()


# =========================================================
# FONTS
# =========================================================

title_font = pygame.font.Font(None, 64)
subtitle_font = pygame.font.Font(None, 28)
status_font = pygame.font.Font(None, 32)
small_font = pygame.font.Font(None, 22)
input_font = pygame.font.Font(None, 28)
history_font = pygame.font.Font(None, 20)


# =========================================================
# COLORS
# =========================================================

BG = (8, 12, 22)
PANEL = (15, 22, 38)
PANEL_2 = (20, 29, 48)
TEXT = (235, 245, 255)
MUTED = (145, 160, 180)
ACCENT = (0, 210, 255)
ACCENT_2 = (80, 120, 255)
DANGER = (220, 80, 100)


# =========================================================
# STATE
# =========================================================

status = "READY"
running = True

input_text = ""
response_text = ""

input_active = True

# Command history
command_history = []

MAX_HISTORY = 6


# =========================================================
# BUTTONS
# =========================================================

mic_button = pygame.Rect(
    WIDTH // 2 - 250,
    HEIGHT - 110,
    160,
    52
)

send_button = pygame.Rect(
    WIDTH // 2 - 70,
    HEIGHT - 110,
    140,
    52
)

clear_button = pygame.Rect(
    WIDTH // 2 + 90,
    HEIGHT - 110,
    160,
    52
)

input_box = pygame.Rect(
    100,
    HEIGHT - 175,
    WIDTH - 200,
    52
)


# =========================================================
# DRAW AI ORB
# =========================================================

def draw_orb(surface, x, y, time):

    pulse = math.sin(time * 0.004) * 8

    for radius in [
        105 + pulse,
        85 + pulse / 2,
        65
    ]:

        pygame.draw.circle(
            surface,
            ACCENT,
            (x, y),
            int(radius),
            2
        )

    pygame.draw.circle(
        surface,
        PANEL,
        (x, y),
        52
    )

    pygame.draw.circle(
        surface,
        ACCENT,
        (x, y),
        48,
        3
    )

    pygame.draw.circle(
        surface,
        ACCENT_2,
        (x, y),
        18
    )


# =========================================================
# CENTERED TEXT
# =========================================================

def draw_centered_text(text, font, color, y):

    text_surface = font.render(
        text,
        True,
        color
    )

    text_rect = text_surface.get_rect(
        center=(WIDTH // 2, y)
    )

    screen.blit(
        text_surface,
        text_rect
    )


# =========================================================
# ADD HISTORY
# =========================================================

def add_history(command, result):

    if not command.strip():
        return

    command_history.append(
        (command.strip(), result or "Done.")
    )

    if len(command_history) > MAX_HISTORY:

        command_history.pop(0)


# =========================================================
# CLEAR HISTORY
# =========================================================

def clear_history():

    global response_text

    command_history.clear()

    response_text = "Command history cleared."

    print("History cleared.")


# =========================================================
# PROCESS COMMAND
# =========================================================

def run_command(command):

    global status
    global response_text
    global input_text

    if not command.strip():

        return None

    status = "THINKING..."

    response_text = "Processing..."

    pygame.display.flip()

    try:

        result = process_command(command)

    except Exception as e:

        print("Command Error:", e)

        result = "Sorry, something went wrong."

    if result == "__EXIT__":

        return "__EXIT__"

    response_text = result if result else "Done."

    add_history(
        command,
        response_text
    )

    status = "READY"

    input_text = ""

    return result


# =========================================================
# VOICE COMMAND
# =========================================================

def handle_voice_command():

    global status
    global response_text

    status = "LISTENING..."

    response_text = "Listening..."

    pygame.display.flip()

    try:

        command = take_command()

    except Exception as e:

        print("Voice Error:", e)

        command = None

    if command:

        run_command(command)

    else:

        status = "READY"

        response_text = "I didn't hear anything."


# =========================================================
# TYPED COMMAND
# =========================================================

def handle_typed_command():

    global input_text

    command = input_text.strip()

    if command:

        result = run_command(command)

        if result == "__EXIT__":

            return "__EXIT__"

    return None


# =========================================================
# DRAW HISTORY
# =========================================================

def draw_history():

    history_x = 40
    history_y = 125

    history_width = 270
    history_height = 390

    # Panel
    history_panel = pygame.Rect(
        history_x,
        history_y,
        history_width,
        history_height
    )

    pygame.draw.rect(
        screen,
        PANEL,
        history_panel,
        border_radius=16
    )

    pygame.draw.rect(
        screen,
        ACCENT,
        history_panel,
        1,
        border_radius=16
    )

    # Title
    title = small_font.render(
        "COMMAND HISTORY",
        True,
        TEXT
    )

    screen.blit(
        title,
        (
            history_x + 18,
            history_y + 18
        )
    )

    # Separator
    pygame.draw.line(
        screen,
        MUTED,
        (
            history_x + 18,
            history_y + 50
        ),
        (
            history_x + history_width - 18,
            history_y + 50
        ),
        1
    )

    if not command_history:

        empty = history_font.render(
            "No commands yet",
            True,
            MUTED
        )

        screen.blit(
            empty,
            (
                history_x + 18,
                history_y + 75
            )
        )

        return

    y = history_y + 70

    for index, (command, result) in enumerate(
        reversed(command_history)
    ):

        # Command
        command_display = command

        if len(command_display) > 30:

            command_display = (
                command_display[:27] + "..."
            )

        command_surface = history_font.render(
            "› " + command_display,
            True,
            ACCENT
        )

        screen.blit(
            command_surface,
            (
                history_x + 18,
                y
            )
        )

        y += 24

        # Result
        result_display = result

        if len(result_display) > 32:

            result_display = (
                result_display[:29] + "..."
            )

        result_surface = history_font.render(
            result_display,
            True,
            MUTED
        )

        screen.blit(
            result_surface,
            (
                history_x + 30,
                y
            )
        )

        y += 42


# =========================================================
# MAIN LOOP
# =========================================================

while running:

    current_time = pygame.time.get_ticks()


    # =====================================================
    # EVENTS
    # =====================================================

    for event in pygame.event.get():

        # -------------------------------------------------
        # WINDOW CLOSE
        # -------------------------------------------------

        if event.type == pygame.QUIT:

            running = False


        # -------------------------------------------------
        # MOUSE
        # -------------------------------------------------

        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Microphone
            if mic_button.collidepoint(event.pos):

                handle_voice_command()


            # Send
            elif send_button.collidepoint(event.pos):

                result = handle_typed_command()

                if result == "__EXIT__":

                    running = False


            # Clear
            elif clear_button.collidepoint(event.pos):

                clear_history()


            # Input
            elif input_box.collidepoint(event.pos):

                input_active = True


            else:

                input_active = False


        # -------------------------------------------------
        # KEYBOARD
        # -------------------------------------------------

        elif event.type == pygame.KEYDOWN:

            # ESC
            if event.key == pygame.K_ESCAPE:

                running = False


            # ENTER
            elif (
                event.key == pygame.K_RETURN
                and input_active
            ):

                result = handle_typed_command()

                if result == "__EXIT__":

                    running = False


            # BACKSPACE
            elif (
                event.key == pygame.K_BACKSPACE
                and input_active
            ):

                input_text = input_text[:-1]


            # SPACE = microphone
            elif (
                event.key == pygame.K_SPACE
                and not input_active
            ):

                handle_voice_command()


            # Normal typing
            elif (
                input_active
                and event.unicode
                and event.key != pygame.K_RETURN
            ):

                if len(input_text) < 120:

                    input_text += event.unicode


    # =====================================================
    # BACKGROUND
    # =====================================================

    screen.fill(BG)


    # =====================================================
    # HEADER
    # =====================================================

    draw_centered_text(
        "J A R V I S",
        title_font,
        TEXT,
        50
    )

    draw_centered_text(
        "AI VOICE ASSISTANT",
        subtitle_font,
        MUTED,
        88
    )


    # =====================================================
    # HISTORY PANEL
    # =====================================================

    draw_history()


    # =====================================================
    # AI ORB
    # =====================================================

    draw_orb(
        screen,
        WIDTH // 2 + 130,
        HEIGHT // 2 - 65,
        current_time
    )


    # =====================================================
    # STATUS
    # =====================================================

    draw_centered_text(
        status,
        status_font,
        ACCENT,
        HEIGHT // 2 + 95
    )


    # =====================================================
    # RESPONSE
    # =====================================================

    if response_text:

        display_response = response_text

        if len(display_response) > 65:

            display_response = (
                display_response[:65] + "..."
            )

        draw_centered_text(
            display_response,
            small_font,
            TEXT,
            HEIGHT // 2 + 135
        )


    # =====================================================
    # INPUT BOX
    # =====================================================

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

        input_surface = input_font.render(
            input_text,
            True,
            TEXT
        )

    else:

        input_surface = input_font.render(
            "Type your command...",
            True,
            MUTED
        )


    screen.blit(
        input_surface,
        (
            input_box.x + 15,
            input_box.y + 12
        )
    )


    # =====================================================
    # MIC BUTTON
    # =====================================================

    pygame.draw.rect(
        screen,
        ACCENT,
        mic_button,
        border_radius=14
    )

    mic_text = small_font.render(
        "MIC / SPEAK",
        True,
        BG
    )

    mic_rect = mic_text.get_rect(
        center=mic_button.center
    )

    screen.blit(
        mic_text,
        mic_rect
    )


    # =====================================================
    # SEND BUTTON
    # =====================================================

    pygame.draw.rect(
        screen,
        ACCENT_2,
        send_button,
        border_radius=14
    )

    send_text = small_font.render(
        "SEND",
        True,
        TEXT
    )

    send_rect = send_text.get_rect(
        center=send_button.center
    )

    screen.blit(
        send_text,
        send_rect
    )


    # =====================================================
    # CLEAR BUTTON
    # =====================================================

    pygame.draw.rect(
        screen,
        DANGER,
        clear_button,
        border_radius=14
    )

    clear_text = small_font.render(
        "CLEAR",
        True,
        TEXT
    )

    clear_rect = clear_text.get_rect(
        center=clear_button.center
    )

    screen.blit(
        clear_text,
        clear_rect
    )


    # =====================================================
    # FOOTER
    # =====================================================

    draw_centered_text(
        "Groq AI  •  Python  •  Pygame",
        small_font,
        MUTED,
        HEIGHT - 25
    )


    # =====================================================
    # UPDATE
    # =====================================================

    pygame.display.flip()

    clock.tick(60)


# =========================================================
# EXIT
# =========================================================

pygame.quit()
sys.exit()

