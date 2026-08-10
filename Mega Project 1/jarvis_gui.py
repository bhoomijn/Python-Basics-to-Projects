
import pygame
import math
import sys

from main import take_command, process_command


# =========================================================
# INITIALIZE PYGAME
# =========================================================

pygame.init()

WIDTH = 1000
HEIGHT = 650

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JARVIS AI Assistant")

clock = pygame.time.Clock()


# =========================================================
# FONTS
# =========================================================

title_font = pygame.font.Font(None, 64)
subtitle_font = pygame.font.Font(None, 30)
status_font = pygame.font.Font(None, 34)
small_font = pygame.font.Font(None, 24)
input_font = pygame.font.Font(None, 30)


# =========================================================
# COLORS
# =========================================================

BG = (8, 12, 22)
PANEL = (15, 22, 38)
TEXT = (235, 245, 255)
MUTED = (145, 160, 180)
ACCENT = (0, 210, 255)
ACCENT_2 = (80, 120, 255)


# =========================================================
# STATE
# =========================================================

status = "READY"
running = True

input_text = ""
response_text = ""

input_active = True


# =========================================================
# BUTTONS
# =========================================================

mic_button = pygame.Rect(
    WIDTH // 2 - 190,
    HEIGHT - 105,
    170,
    55
)

send_button = pygame.Rect(
    WIDTH // 2 + 20,
    HEIGHT - 105,
    170,
    55
)

input_box = pygame.Rect(
    120,
    HEIGHT - 175,
    WIDTH - 240,
    55
)


# =========================================================
# DRAW AI ORB
# =========================================================

def draw_orb(surface, x, y, time):

    pulse = math.sin(time * 0.004) * 8

    # Outer rings
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

    # Main orb
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

    # Inner orb
    pygame.draw.circle(
        surface,
        ACCENT_2,
        (x, y),
        18
    )


# =========================================================
# DRAW CENTERED TEXT
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
# PROCESS COMMAND
# =========================================================

def run_command(command):

    global status
    global response_text
    global input_text

    if not command.strip():
        return

    status = "THINKING..."
    response_text = "Processing..."

    pygame.display.flip()

    result = process_command(command)

    if result == "__EXIT__":

        return "__EXIT__"

    response_text = result if result else "Done."

    status = "READY"

    input_text = ""

    return result


# =========================================================
# PROCESS VOICE COMMAND
# =========================================================

def handle_voice_command():

    global status
    global response_text

    status = "LISTENING..."
    response_text = "Listening..."

    pygame.display.flip()

    command = take_command()

    if command:

        run_command(command)

    else:

        status = "READY"
        response_text = "I didn't hear anything."


# =========================================================
# PROCESS TYPED COMMAND
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
        # MOUSE CLICK
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

            # Input box
            elif input_box.collidepoint(event.pos):

                input_active = True

            else:

                input_active = False


        # -------------------------------------------------
        # KEYBOARD
        # -------------------------------------------------

        elif event.type == pygame.KEYDOWN:

            # ESC = EXIT
            if event.key == pygame.K_ESCAPE:

                running = False

            # SPACE = MICROPHONE
            elif (
                event.key == pygame.K_SPACE
                and not input_active
            ):

                handle_voice_command()

            # ENTER = SEND
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

            # Normal typing
            elif (
                input_active
                and event.unicode
                and event.key != pygame.K_RETURN
            ):

                # Keep input reasonably sized
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
        55
    )

    draw_centered_text(
        "AI VOICE ASSISTANT",
        subtitle_font,
        MUTED,
        95
    )


    # =====================================================
    # AI ORB
    # =====================================================

    draw_orb(
        screen,
        WIDTH // 2,
        HEIGHT // 2 - 25,
        current_time
    )


    # =====================================================
    # STATUS
    # =====================================================

    draw_centered_text(
        status,
        status_font,
        ACCENT,
        HEIGHT // 2 + 120
    )


    # =====================================================
    # RESPONSE
    # =====================================================

    if response_text:

        display_response = response_text

        if len(display_response) > 75:

            display_response = (
                display_response[:75] + "..."
            )

        draw_centered_text(
            display_response,
            small_font,
            TEXT,
            HEIGHT // 2 + 160
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


    # Input placeholder
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
            input_box.y + 13
        )
    )


    # =====================================================
    # MICROPHONE BUTTON
    # =====================================================

    pygame.draw.rect(
        screen,
        ACCENT,
        mic_button,
        border_radius=15
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
        border_radius=15
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
