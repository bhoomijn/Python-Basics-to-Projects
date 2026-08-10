
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
response_font = pygame.font.Font(None, 26)


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
# DRAW CENTERED TEXT
# =========================================================

def draw_centered_text(text, font, color, y):

    text_surface = font.render(
        str(text),
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
# DRAW RESPONSE
# =========================================================

def draw_response(text):

    if not text:
        return

    # Response panel
    response_box = pygame.Rect(
        100,
        395,
        800,
        105
    )

    pygame.draw.rect(
        screen,
        PANEL,
        response_box,
        border_radius=15
    )

    pygame.draw.rect(
        screen,
        ACCENT_2,
        response_box,
        1,
        border_radius=15
    )

    # Break response into lines
    words = str(text).split()

    lines = []
    current_line = ""

    for word in words:

        test_line = (
            current_line + " " + word
        ).strip()

        if response_font.size(test_line)[0] < 750:

            current_line = test_line

        else:

            if current_line:
                lines.append(current_line)

            current_line = word

    if current_line:
        lines.append(current_line)

    # Maximum 3 lines
    lines = lines[:3]

    y = response_box.y + 20

    for line in lines:

        text_surface = response_font.render(
            line,
            True,
            TEXT
        )

        text_rect = text_surface.get_rect(
            center=(WIDTH // 2, y)
        )

        screen.blit(
            text_surface,
            text_rect
        )

        y += 27


# =========================================================
# PROCESS COMMAND
# =========================================================

def run_command(command):

    global status
    global response_text
    global input_text

    command = command.strip()

    if not command:
        return None

    status = "THINKING..."

    response_text = "Processing..."

    # Show Processing immediately
    draw_screen()
    pygame.display.flip()

    try:

        result = process_command(command)

    except Exception as e:

        print("Command Error:", e)

        result = (
            "Sorry, something went wrong."
        )

    if result == "__EXIT__":

        return "__EXIT__"

    if result:

        response_text = str(result)

    else:

        response_text = "Done."

    status = "READY"

    input_text = ""

    # IMPORTANT:
    # Immediately redraw final answer
    draw_screen()
    pygame.display.flip()

    return result


# =========================================================
# PROCESS VOICE COMMAND
# =========================================================

def handle_voice_command():

    global status
    global response_text

    status = "LISTENING..."

    response_text = "Listening..."

    draw_screen()
    pygame.display.flip()

    command = take_command()

    if command:

        result = run_command(command)

        if result == "__EXIT__":

            return "__EXIT__"

    else:

        status = "READY"

        response_text = (
            "I didn't hear anything."
        )

        draw_screen()
        pygame.display.flip()

    return None


# =========================================================
# PROCESS TYPED COMMAND
# =========================================================

def handle_typed_command():

    global input_text

    command = input_text.strip()

    if not command:
        return None

    result = run_command(command)

    if result == "__EXIT__":

        return "__EXIT__"

    return result


# =========================================================
# DRAW COMPLETE SCREEN
# =========================================================

def draw_screen():

    current_time = pygame.time.get_ticks()

    # -----------------------------------------------------
    # BACKGROUND
    # -----------------------------------------------------

    screen.fill(BG)

    # -----------------------------------------------------
    # HEADER
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # ORB
    # -----------------------------------------------------

    draw_orb(
        screen,
        WIDTH // 2,
        HEIGHT // 2 - 35,
        current_time
    )

    # -----------------------------------------------------
    # STATUS
    # -----------------------------------------------------

    draw_centered_text(
        status,
        status_font,
        ACCENT,
        335
    )

    # -----------------------------------------------------
    # RESPONSE
    # -----------------------------------------------------

    draw_response(response_text)

    # -----------------------------------------------------
    # INPUT BOX
    # -----------------------------------------------------

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
            input_box.y + 13
        )
    )

    # -----------------------------------------------------
    # MICROPHONE BUTTON
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # SEND BUTTON
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # FOOTER
    # -----------------------------------------------------

    draw_centered_text(
        "Groq AI  •  Python  •  Pygame",
        small_font,
        MUTED,
        HEIGHT - 25
    )


# =========================================================
# MAIN LOOP
# =========================================================

while running:

    for event in pygame.event.get():

        # -------------------------------------------------
        # CLOSE WINDOW
        # -------------------------------------------------

        if event.type == pygame.QUIT:

            running = False

        # -------------------------------------------------
        # MOUSE
        # -------------------------------------------------

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if mic_button.collidepoint(event.pos):

                result = handle_voice_command()

                if result == "__EXIT__":

                    running = False

            elif send_button.collidepoint(event.pos):

                result = handle_typed_command()

                if result == "__EXIT__":

                    running = False

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

                result = handle_voice_command()

                if result == "__EXIT__":

                    running = False

            # NORMAL TYPING
            elif (
                input_active
                and event.unicode
                and event.key != pygame.K_RETURN
            ):

                if len(input_text) < 120:

                    input_text += event.unicode

    # -----------------------------------------------------
    # DRAW
    # -----------------------------------------------------

    draw_screen()

    pygame.display.flip()

    clock.tick(60)


# =========================================================
# EXIT
# =========================================================

pygame.quit()
sys.exit()
