import os
import json
import random
import pygame

pygame.init()

# ==========================================
# BLOCKYRUNNER MOBILE
# ==========================================

W, H = 480, 800
PLAY_H = 580
FPS = 60

display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("BlockyRunner Mobile")

DISPLAY_W, DISPLAY_H = display.get_size()
screen = pygame.Surface((W, H))
clock = pygame.time.Clock()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RECORD_FILE = os.path.join(BASE_DIR, "records.txt")
PROFILE_FILE = os.path.join(BASE_DIR, "player_profile.json")

# ==========================================
# COLORS
# ==========================================

WHITE = (245, 245, 245)
BG = (30, 30, 30)
RED = (225, 36, 0)
GREEN = (68, 148, 74)
YELLOW = (255, 198, 24)
CYAN = (0, 255, 255)
DARK = (60, 60, 60)
BLACK = (0, 0, 0)

# ==========================================
# FONTS
# ==========================================

font_text = pygame.font.Font(None, 30)
font_warn = pygame.font.Font(None, 38)
font_mode = pygame.font.Font(None, 22)
font_menu = pygame.font.Font(None, 22)
font_btn = pygame.font.Font(None, 26)
font_small = pygame.font.Font(None, 19)
font_title = pygame.font.Font(None, 36)

# ==========================================
# DIFFICULTY
# ==========================================

MODE_SPEEDS = {
    "easy": 15,
    "normal": 20,
    "hard": 25,
}

MODE_LABELS = {
    "easy": "Easy Level",
    "normal": "Normal Level",
    "hard": "Hard Level",
}

MODE_ORDER = ["easy", "normal", "hard"]

# ==========================================
# SHOP
# ==========================================

SHOP_ITEMS = {
    # PLAYER COLORS
    "player_white": {
        "name": "White Player", "category": "Player",
        "price": 0, "kind": "player",
        "color": (245, 245, 245)
    },
    "player_cyan": {
        "name": "Cyan Player", "category": "Player",
        "price": 10, "kind": "player",
        "color": (0, 255, 255)
    },
    "player_pink": {
        "name": "Pink Player", "category": "Player",
        "price": 15, "kind": "player",
        "color": (255, 90, 180)
    },
    "player_gold": {
        "name": "Gold Player", "category": "Player",
        "price": 20, "kind": "player",
        "color": (255, 198, 24)
    },
    "player_lime": {
        "name": "Neon Lime Player", "category": "Player",
        "price": 20, "kind": "player",
        "color": (120, 255, 40)
    },
    "player_ice": {
        "name": "Ice Player", "category": "Player",
        "price": 25, "kind": "player",
        "color": (150, 225, 255)
    },
    "player_violet": {
        "name": "Violet Player", "category": "Player",
        "price": 25, "kind": "player",
        "color": (180, 100, 255)
    },
    "player_blue": {
        "name": "Electric Blue Player", "category": "Player",
        "price": 35, "kind": "player",
        "color": (50, 100, 255)
    },

    # ENEMY COLORS
    "enemy_red": {
        "name": "Red Enemy", "category": "Enemies",
        "price": 0, "kind": "enemy",
        "color": (225, 36, 0)
    },
    "enemy_purple": {
        "name": "Purple Enemy", "category": "Enemies",
        "price": 15, "kind": "enemy",
        "color": (160, 70, 230)
    },
    "enemy_orange": {
        "name": "Orange Enemy", "category": "Enemies",
        "price": 15, "kind": "enemy",
        "color": (255, 130, 25)
    },
    "enemy_ice": {
        "name": "Ice Enemies", "category": "Enemies",
        "price": 25, "kind": "enemy",
        "color": (80, 220, 255)
    },
    "enemy_lime": {
        "name": "Toxic Enemies", "category": "Enemies",
        "price": 30, "kind": "enemy",
        "color": (130, 255, 30)
    },
    "enemy_white": {
        "name": "Ghost Enemies", "category": "Enemies",
        "price": 35, "kind": "enemy",
        "color": (235, 235, 255)
    },

    # COINS
    "coin_yellow": {
        "name": "Yellow Coin", "category": "Coin",
        "price": 0, "kind": "coin",
        "color": (255, 198, 24)
    },
    "coin_blue": {
        "name": "Blue Coin", "category": "Coin",
        "price": 10, "kind": "coin",
        "color": (70, 150, 255)
    },
    "coin_pink": {
        "name": "Pink Coin", "category": "Coin",
        "price": 15, "kind": "coin",
        "color": (255, 80, 190)
    },
    "coin_lime": {
        "name": "Toxic Coin", "category": "Coin",
        "price": 20, "kind": "coin",
        "color": (150, 255, 40)
    },
    "coin_ice": {
        "name": "Ice Coin", "category": "Coin",
        "price": 20, "kind": "coin",
        "color": (100, 220, 255)
    },

    # BACKGROUNDS
    "bg_dark": {
        "name": "Dark Background", "category": "Background",
        "price": 0, "kind": "background",
        "color": (30, 30, 30)
    },
    "bg_navy": {
        "name": "Night Blue", "category": "Background",
        "price": 15, "kind": "background",
        "color": (12, 24, 55)
    },
    "bg_forest": {
        "name": "Forest Green", "category": "Background",
        "price": 15, "kind": "background",
        "color": (15, 45, 30)
    },
    "bg_purple": {
        "name": "Deep Purple", "category": "Background",
        "price": 25, "kind": "background",
        "color": (35, 15, 55)
    },
    "bg_crimson": {
        "name": "Crimson Night", "category": "Background",
        "price": 30, "kind": "background",
        "color": (55, 12, 20)
    },
    "bg_ice": {
        "name": "Frozen World", "category": "Background",
        "price": 30, "kind": "background",
        "color": (15, 35, 55)
    },
    "bg_void": {
        "name": "Void Black", "category": "Background",
        "price": 40, "kind": "background",
        "color": (5, 5, 12)
    },

    # TEXT COLORS
    "text_white": {
        "name": "White Text", "category": "Text",
        "price": 0, "kind": "text",
        "color": (245, 245, 245)
    },
    "text_cyan": {
        "name": "Cyan Text", "category": "Text",
        "price": 10, "kind": "text",
        "color": (0, 255, 255)
    },
    "text_pink": {
        "name": "Pink Text", "category": "Text",
        "price": 10, "kind": "text",
        "color": (255, 120, 200)
    },
    "text_gold": {
        "name": "Gold Text", "category": "Text",
        "price": 15, "kind": "text",
        "color": (255, 205, 70)
    },
    "text_lime": {
        "name": "Neon Lime Text", "category": "Text",
        "price": 15, "kind": "text",
        "color": (150, 255, 70)
    },
    "text_violet": {
        "name": "Violet Text", "category": "Text",
        "price": 15, "kind": "text",
        "color": (195, 140, 255)
    },
    "text_ice": {
        "name": "Ice Text", "category": "Text",
        "price": 20, "kind": "text",
        "color": (140, 225, 255)
    },

    # BUTTON COLORS
    "ui_gray": {
        "name": "Gray Buttons", "category": "Buttons",
        "price": 0, "kind": "buttons",
        "color": (60, 60, 60)
    },
    "ui_blue": {
        "name": "Blue Buttons", "category": "Buttons",
        "price": 10, "kind": "buttons",
        "color": (35, 85, 160)
    },
    "ui_purple": {
        "name": "Purple Buttons", "category": "Buttons",
        "price": 10, "kind": "buttons",
        "color": (105, 55, 150)
    },
    "ui_neon": {
        "name": "Neon Buttons", "category": "Buttons",
        "price": 20, "kind": "buttons",
        "color": (20, 100, 65)
    },
    "ui_red": {
        "name": "Red Buttons", "category": "Buttons",
        "price": 20, "kind": "buttons",
        "color": (145, 35, 45)
    },
    "ui_ice": {
        "name": "Ice Buttons", "category": "Buttons",
        "price": 20, "kind": "buttons",
        "color": (35, 85, 115)
    },

    # ACCESSORIES
    "acc_none": {
        "name": "No Accessory", "category": "Accessories",
        "price": 0, "kind": "accessory",
        "accessory": "none"
    },
    "acc_glasses": {
        "name": "Cool Glasses", "category": "Accessories",
        "price": 20, "kind": "accessory",
        "accessory": "glasses"
    },
    "acc_crown": {
        "name": "Crown", "category": "Accessories",
        "price": 30, "kind": "accessory",
        "accessory": "crown"
    },
    "acc_halo": {
        "name": "Halo", "category": "Accessories",
        "price": 25, "kind": "accessory",
        "accessory": "halo"
    },
    "acc_cat": {
        "name": "Cat Ears", "category": "Accessories",
        "price": 20, "kind": "accessory",
        "accessory": "cat"
    },
    "acc_horns": {
        "name": "Demon Horns", "category": "Accessories",
        "price": 30, "kind": "accessory",
        "accessory": "horns"
    },
    "acc_star": {
        "name": "Star", "category": "Accessories",
        "price": 25, "kind": "accessory",
        "accessory": "star"
    },
    "acc_bunny": {
        "name": "Bunny Ears", "category": "Accessories",
        "price": 25, "kind": "accessory",
        "accessory": "bunny"
    },
}

SHOP_CATEGORIES = [
    "Player", "Enemies", "Coin", "Background",
    "Text", "Buttons", "Accessories"
]

# ==========================================
# PLAYER PROFILE
# ==========================================

DEFAULT_PROFILE = {
    "coins": 0,
    "owned": [
        "player_white",
        "enemy_red",
        "coin_yellow",
        "bg_dark",
        "text_white",
        "ui_gray",
        "acc_none",
    ],
    "equipped": {
        "player": "player_white",
        "enemy": "enemy_red",
        "coin": "coin_yellow",
        "background": "bg_dark",
        "text": "text_white",
        "buttons": "ui_gray",
        "accessory": "acc_none",
    },
}


def load_profile():
    profile_data = json.loads(json.dumps(DEFAULT_PROFILE))

    try:
        if os.path.exists(PROFILE_FILE):
            with open(PROFILE_FILE, "r", encoding="utf-8") as file:
                saved = json.load(file)

            if isinstance(saved, dict):
                profile_data["coins"] = max(
                    0, int(saved.get("coins", 0))
                )

                owned = saved.get("owned", [])
                if isinstance(owned, list):
                    valid_owned = [
                        item_id for item_id in owned
                        if item_id in SHOP_ITEMS
                    ]
                    profile_data["owned"] = list(dict.fromkeys(
                        valid_owned + profile_data["owned"]
                    ))

                equipped = saved.get("equipped", {})
                if isinstance(equipped, dict):
                    for slot in profile_data["equipped"]:
                        item_id = equipped.get(slot)

                        if (
                            item_id in profile_data["owned"]
                            and item_id in SHOP_ITEMS
                            and SHOP_ITEMS[item_id]["kind"] == slot
                        ):
                            profile_data["equipped"][slot] = item_id

    except (OSError, ValueError, TypeError):
        pass

    return profile_data


def save_profile():
    try:
        with open(PROFILE_FILE, "w", encoding="utf-8") as file:
            json.dump(
                profile,
                file,
                ensure_ascii=False,
                indent=2
            )
    except OSError:
        pass


def item_color(slot, fallback):
    item_id = profile["equipped"].get(slot)
    item = SHOP_ITEMS.get(item_id, {})
    return item.get("color", fallback)


def text_color():
    return item_color("text", WHITE)


def button_color():
    return item_color("buttons", DARK)


# ==========================================
# RECORDS
# ==========================================

def load_records():
    records_data = {
        "easy": 0,
        "normal": 0,
        "hard": 0,
    }

    try:
        if os.path.exists(RECORD_FILE):
            with open(RECORD_FILE, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(":")

                    if len(parts) == 2 and parts[0] in records_data:
                        try:
                            records_data[parts[0]] = max(
                                0, int(parts[1])
                            )
                        except ValueError:
                            pass

    except OSError:
        pass

    return records_data


def save_record(mode, score):
    current_records = load_records()

    if score <= current_records.get(mode, 0):
        return

    current_records[mode] = score

    try:
        with open(RECORD_FILE, "w", encoding="utf-8") as file:
            for key, value in current_records.items():
                file.write(f"{key}:{value}\n")
    except OSError:
        pass


# ==========================================
# DRAWING HELPERS
# ==========================================

def to_game_coords(pos):
    return (
        int(pos[0] * W / DISPLAY_W),
        int(pos[1] * H / DISPLAY_H)
    )


def draw_text(text, font, color, pos, surface=None):
    if surface is None:
        surface = screen

    surface.blit(
        font.render(str(text), True, color),
        pos
    )


def centered_text(text, font, color, center, surface=None):
    if surface is None:
        surface = screen

    rendered = font.render(str(text), True, color)
    surface.blit(rendered, rendered.get_rect(center=center))


def draw_button(rect, label, color=None, label_color=None, font=None):
    if color is None:
        color = button_color()

    if label_color is None:
        label_color = text_color()

    if font is None:
        font = font_btn

    pygame.draw.rect(screen, color, rect, border_radius=9)
    pygame.draw.rect(
        screen, (125, 125, 125), rect,
        2, border_radius=9
    )
    centered_text(label, font, label_color, rect.center)


def draw_control(rect, label, color=None):
    draw_button(rect, label, color=color, font=font_btn)


# ==========================================
# GAME OBJECTS
# ==========================================

def new_round(mode):
    return {
        "mode": mode,
        "player": pygame.Rect(210, 250, 60, 60),
        "red": pygame.Rect(
            random.randint(0, W - 30), -600, 30, 30
        ),
        "green": pygame.Rect(
            -600, random.randint(0, PLAY_H - 30), 30, 30
        ),
        "coin": pygame.Rect(
            random.randint(0, W - 15),
            random.randint(0, PLAY_H - 15),
            15, 15
        ),
        "score": 0,
        "stamina": 100.0,
        "dead": False,
        "blink": 0,
        "warning_timer": 0,
    }


def start_game(mode):
    global game, scene, last_awarded_game

    game = new_round(mode)
    scene = "game"
    last_awarded_game = False


def change_mode(mode):
    if scene == "game":
        game["mode"] = mode


def award_coins(score):
    global last_awarded_game

    if last_awarded_game:
        return

    reward = max(1, score // 5 + 1)
    profile["coins"] += reward
    save_profile()
    last_awarded_game = True


# ==========================================
# PLAYER ACCESSORIES
# ==========================================

def equipped_accessory(player_rect):
    accessory = SHOP_ITEMS.get(
        profile["equipped"].get("accessory", "acc_none"), {}
    ).get("accessory", "none")

    x = player_rect.x
    y = player_rect.y
    w = player_rect.width
    h = player_rect.height

    if accessory == "glasses":
        pygame.draw.rect(
            screen, (20, 20, 25),
            (x + 7, y + 19, 20, 9),
            border_radius=2
        )
        pygame.draw.rect(
            screen, (20, 20, 25),
            (x + 33, y + 19, 20, 9),
            border_radius=2
        )
        pygame.draw.line(
            screen, (20, 20, 25),
            (x + 27, y + 23), (x + 33, y + 23), 3
        )

    elif accessory == "crown":
        points = [
            (x + 8, y + 8),
            (x + 4, y - 8),
            (x + 20, y + 1),
            (x + 30, y - 12),
            (x + 40, y + 1),
            (x + 56, y - 8),
            (x + 52, y + 8),
        ]
        pygame.draw.polygon(screen, YELLOW, points)
        pygame.draw.rect(
            screen, YELLOW,
            (x + 8, y + 5, 44, 7)
        )

    elif accessory == "halo":
        pygame.draw.ellipse(
            screen, (255, 235, 100),
            (x + 9, y - 13, 42, 12), 3
        )

    elif accessory == "cat":
        pygame.draw.polygon(
            screen, (255, 140, 190),
            [(x + 8, y + 12), (x + 10, y - 12),
             (x + 27, y + 5)]
        )
        pygame.draw.polygon(
            screen, (255, 140, 190),
            [(x + 33, y + 5), (x + 50, y - 12),
             (x + 52, y + 12)]
        )

    elif accessory == "horns":
        pygame.draw.polygon(
            screen, (180, 40, 60),
            [(x + 8, y + 12), (x + 2, y - 10),
             (x + 25, y + 5)]
        )
        pygame.draw.polygon(
            screen, (180, 40, 60),
            [(x + 35, y + 5), (x + 58, y - 10),
             (x + 52, y + 12)]
        )

    elif accessory == "star":
        points = [
            (x + 30, y - 17),
            (x + 35, y - 5),
            (x + 48, y - 4),
            (x + 38, y + 4),
            (x + 42, y + 15),
            (x + 30, y + 8),
            (x + 18, y + 15),
            (x + 22, y + 4),
            (x + 12, y - 4),
            (x + 25, y - 5),
        ]
        pygame.draw.polygon(screen, YELLOW, points)

    elif accessory == "bunny":
        pygame.draw.ellipse(
            screen, (245, 235, 245),
            (x + 8, y - 24, 16, 34)
        )
        pygame.draw.ellipse(
            screen, (245, 235, 245),
            (x + 36, y - 24, 16, 34)
        )
        pygame.draw.ellipse(
            screen, (255, 130, 190),
            (x + 12, y - 20, 8, 25)
        )
        pygame.draw.ellipse(
            screen, (255, 130, 190),
            (x + 40, y - 20, 8, 25)
        )
        # ==========================================
# INITIAL STATE
# ==========================================

profile = load_profile()
records = load_records()

scene = "menu"
game = new_round("easy")
running = True

active_fingers = {}
mouse_is_down = False
mouse_pos = (0, 0)
last_awarded_game = False

# ==========================================
# MAIN MENU BUTTONS
# ==========================================

menu_easy = pygame.Rect(35, 205, 125, 62)
menu_normal = pygame.Rect(177, 205, 125, 62)
menu_hard = pygame.Rect(319, 205, 125, 62)

play_rect = pygame.Rect(70, 305, 160, 65)
shop_rect = pygame.Rect(250, 305, 160, 65)
quit_rect = pygame.Rect(150, 405, 180, 55)

# ==========================================
# PAUSE MENU BUTTONS
# ==========================================

game_menu_rect = pygame.Rect(365, 48, 100, 38)

resume_rect = pygame.Rect(70, 150, 150, 55)
return_menu_rect = pygame.Rect(250, 150, 160, 55)

pause_easy = pygame.Rect(45, 275, 120, 58)
pause_normal = pygame.Rect(180, 275, 120, 58)
pause_hard = pygame.Rect(315, 275, 120, 58)

# ==========================================
# VIRTUAL GAMEPAD
# ==========================================

btn_up = pygame.Rect(90, 600, 100, 50)
btn_down = pygame.Rect(90, 710, 100, 50)
btn_left = pygame.Rect(20, 655, 65, 50)
btn_right = pygame.Rect(195, 655, 65, 50)
btn_sprint = pygame.Rect(300, 630, 150, 90)

# ==========================================
# SHOP BUTTONS
# ==========================================

shop_back_rect = pygame.Rect(20, 20, 105, 42)
shop_prev_rect = pygame.Rect(20, 705, 95, 48)
shop_next_rect = pygame.Rect(365, 705, 95, 48)
shop_buy_rect = pygame.Rect(150, 705, 180, 48)

shop_category_index = 0
shop_item_index = 0

shop_message = ""
shop_message_until = 0


# ==========================================
# MAIN LOOP
# ==========================================

while running:
    clock.tick(FPS)

    just_tapped = False
    tapped_points = []

    # --------------------------------------
    # EVENTS
    # --------------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if scene == "game":
                    scene = "pause"
                elif scene == "pause":
                    scene = "game"
                elif scene == "shop":
                    scene = "menu"
                else:
                    running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_is_down = True
            mouse_pos = to_game_coords(event.pos)
            just_tapped = True
            tapped_points.append(mouse_pos)

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_is_down = False

        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = to_game_coords(event.pos)

        elif event.type == pygame.FINGERDOWN:
            pos = (
                int(event.x * W),
                int(event.y * H)
            )
            active_fingers[event.finger_id] = pos
            just_tapped = True
            tapped_points.append(pos)

        elif event.type == pygame.FINGERMOTION:
            active_fingers[event.finger_id] = (
                int(event.x * W),
                int(event.y * H)
            )

        elif event.type == pygame.FINGERUP:
            active_fingers.pop(event.finger_id, None)

    touch_positions = list(active_fingers.values())

    if mouse_is_down:
        touch_positions.append(mouse_pos)

    def held(rect):
        return any(
            rect.collidepoint(pos)
            for pos in touch_positions
        )

    def tapped(rect):
        return any(
            rect.collidepoint(pos)
            for pos in tapped_points
        )

    keys = pygame.key.get_pressed()

    # Apply equipped background
    screen.fill(item_color("background", BG))
    UI_TEXT = text_color()

    # ======================================
    # MAIN MENU
    # ======================================

    if scene == "menu":

        centered_text(
            "BLOCKYRUNNER",
            font_title, UI_TEXT,
            (W // 2, 95)
        )

        centered_text(
            "MOBILE",
            font_text, UI_TEXT,
            (W // 2, 132)
        )

        centered_text(
            f"Coins: {profile['coins']}",
            font_text, YELLOW,
            (W // 2, 168)
        )

        centered_text(
            "Choose difficulty",
            font_menu, UI_TEXT,
            (W // 2, 190)
        )

        difficulty_buttons = [
            ("easy", menu_easy, "EASY", GREEN, BLACK),
            ("normal", menu_normal, "NORMAL",
             (254, 254, 34), BLACK),
            ("hard", menu_hard, "HARD", RED, WHITE),
        ]

        for mode, rect, label, color, label_color in difficulty_buttons:
            draw_button(
                rect, label,
                color, label_color
            )

            centered_text(
                f"Best: {records[mode]}",
                font_small, UI_TEXT,
                (rect.centerx, rect.bottom + 16)
            )

        draw_button(play_rect, "PLAY", GREEN, BLACK)
        draw_button(shop_rect, "SHOP")
        draw_button(quit_rect, "EXIT", (90, 45, 45), WHITE)

        if just_tapped:

            selected_mode = None

            if tapped(menu_easy):
                selected_mode = "easy"

            elif tapped(menu_normal):
                selected_mode = "normal"

            elif tapped(menu_hard):
                selected_mode = "hard"

            if selected_mode:
                start_game(selected_mode)

            elif tapped(play_rect):
                start_game(game["mode"])

            elif tapped(shop_rect):
                scene = "shop"

            elif tapped(quit_rect):
                running = False

    # ======================================
    # PAUSE / GAME MENU
    # ======================================

    elif scene == "pause":

        centered_text(
            "GAME MENU",
            font_title, UI_TEXT,
            (W // 2, 85)
        )

        centered_text(
            f"Current difficulty: {MODE_LABELS[game['mode']]}",
            font_menu, UI_TEXT,
            (W // 2, 120)
        )

        draw_button(resume_rect, "RESUME", GREEN, BLACK)
        draw_button(return_menu_rect, "MAIN MENU")

        centered_text(
            "Change difficulty",
            font_menu, UI_TEXT,
            (W // 2, 240)
        )

        draw_button(pause_easy, "EASY", GREEN, BLACK)
        draw_button(
            pause_normal, "NORMAL",
            (254, 254, 34), BLACK
        )
        draw_button(pause_hard, "HARD", RED, WHITE)

        centered_text(
            "Your current run is kept.",
            font_small, UI_TEXT,
            (W // 2, 365)
        )

        centered_text(
            f"Score: {game['score']}",
            font_text, UI_TEXT,
            (W // 2, 410)
        )

        if just_tapped:

            if tapped(resume_rect):
                scene = "game"

            elif tapped(return_menu_rect):
                scene = "menu"

            elif tapped(pause_easy):
                change_mode("easy")

            elif tapped(pause_normal):
                change_mode("normal")

            elif tapped(pause_hard):
                change_mode("hard")

    # ======================================
    # SHOP
    # ======================================

    elif scene == "shop":

        screen.fill(item_color("background", BG))
        UI_TEXT = text_color()

        centered_text(
            "SHOP",
            font_title, UI_TEXT,
            (W // 2, 65)
        )

        centered_text(
            f"Coins: {profile['coins']}",
            font_text, YELLOW,
            (W // 2, 105)
        )

        draw_button(shop_back_rect, "BACK")

        category = SHOP_CATEGORIES[shop_category_index]

        # Category navigation hints
        centered_text(
            "<",
            font_title, UI_TEXT,
            (75, 155)
        )

        centered_text(
            category,
            font_menu, UI_TEXT,
            (W // 2, 155)
        )

        centered_text(
            ">",
            font_title, UI_TEXT,
            (405, 155)
        )

        category_items = [
            (item_id, item)
            for item_id, item in SHOP_ITEMS.items()
            if item["category"] == category
        ]

        if category_items:

            shop_item_index %= len(category_items)

            item_id, item = category_items[shop_item_index]

            panel = pygame.Rect(45, 190, 390, 440)

            pygame.draw.rect(
                screen, (42, 42, 48),
                panel, border_radius=14
            )

            pygame.draw.rect(
                screen, (110, 110, 120),
                panel, 2, border_radius=14
            )

            centered_text(
                item["name"],
                font_title, UI_TEXT,
                (W // 2, 230)
            )

            # Item preview
            if item["kind"] == "accessory":

                preview_rect = pygame.Rect(200, 300, 80, 80)

                pygame.draw.rect(
                    screen,
                    item_color("player", WHITE),
                    preview_rect
                )

                equipped_accessory(preview_rect)

            elif item["kind"] == "background":

                pygame.draw.rect(
                    screen, item["color"],
                    (75, 275, 330, 155)
                )

                pygame.draw.rect(
                    screen, UI_TEXT,
                    (75, 275, 330, 155), 2
                )

                centered_text(
                    "Background preview",
                    font_small,
                    WHITE,
                    (W // 2, 410)
                )

            elif item["kind"] == "text":

                pygame.draw.rect(
                    screen, (25, 25, 25),
                    (90, 290, 300, 110),
                    border_radius=8
                )

                centered_text(
                    "Sample Text",
                    font_text, item["color"],
                    (W // 2, 345)
                )

            elif item["kind"] == "buttons":

                pygame.draw.rect(
                    screen, item["color"],
                    (135, 315, 210, 55),
                    border_radius=8
                )

                centered_text(
                    "Button preview",
                    font_small, WHITE,
                    (W // 2, 342)
                )

            elif item["kind"] == "coin":

                pygame.draw.ellipse(
                    screen, item["color"],
                    (205, 305, 70, 70)
                )

            elif item["kind"] == "enemy":

                pygame.draw.rect(
                    screen, item["color"],
                    (205, 300, 65, 65)
                )

            else:

                pygame.draw.rect(
                    screen, item["color"],
                    (195, 295, 90, 90),
                    border_radius=8
                )

                if item["kind"] == "player":
                    equipped_accessory(
                        pygame.Rect(195, 295, 90, 90)
                    )

            owned = item_id in profile["owned"]

            equipped = (
                item_id
                == profile["equipped"].get(item["kind"])
            )

            if owned:
                status = "EQUIPPED" if equipped else "OWNED"
                status_color = GREEN
            else:
                status = f"Price: {item['price']} coins"
                status_color = YELLOW

            centered_text(
                status,
                font_text, status_color,
                (W // 2, 475)
            )

            centered_text(
                f"Item {shop_item_index + 1} / {len(category_items)}",
                font_small, UI_TEXT,
                (W // 2, 515)
            )

            centered_text(
                "Tap < or > to change category",
                font_small, UI_TEXT,
                (W // 2, 555)
            )

            centered_text(
                "PREV / NEXT to browse items",
                font_small, UI_TEXT,
                (W // 2, 580)
            )

            draw_button(shop_prev_rect, "PREV")
            draw_button(shop_next_rect, "NEXT")
            draw_button(shop_buy_rect, "BUY / USE", GREEN, BLACK)

            # Handle shop controls
            if just_tapped:

                if tapped(shop_back_rect):
                    scene = "menu"

                elif tapped(shop_prev_rect):
                    shop_item_index = (
                        shop_item_index - 1
                    ) % len(category_items)

                elif tapped(shop_next_rect):
                    shop_item_index = (
                        shop_item_index + 1
                    ) % len(category_items)

                elif tapped(shop_buy_rect):

                    if item_id in profile["owned"]:

                        profile["equipped"][item["kind"]] = item_id
                        save_profile()

                        shop_message = "Equipped!"
                        shop_message_until = (
                            pygame.time.get_ticks() + 1400
                        )

                    elif profile["coins"] >= item["price"]:

                        profile["coins"] -= item["price"]
                        profile["owned"].append(item_id)
                        profile["equipped"][item["kind"]] = item_id

                        save_profile()

                        shop_message = "Purchased and equipped!"
                        shop_message_until = (
                            pygame.time.get_ticks() + 1400
                        )

                    else:

                        shop_message = "Not enough coins!"
                        shop_message_until = (
                            pygame.time.get_ticks() + 1400
                        )

        # Category navigation works by tapping either side
        if just_tapped and tapped_points:

            px, py = tapped_points[0]

            if 125 <= py <= 180 and px < 120:
                shop_category_index = (
                    shop_category_index - 1
                ) % len(SHOP_CATEGORIES)

                shop_item_index = 0

            elif 125 <= py <= 180 and px > 360:
                shop_category_index = (
                    shop_category_index + 1
                ) % len(SHOP_CATEGORIES)

                shop_item_index = 0

        if pygame.time.get_ticks() < shop_message_until:
            centered_text(
                shop_message,
                font_menu, YELLOW,
                (W // 2, 675)
            )

    # ======================================
    # GAMEPLAY CONTINUES IN PART 3
    # ======================================
    elif scene == "game":

        player = game["player"]
        red = game["red"]
        green = game["green"]
        coin = game["coin"]

        # Open the in-game menu
        if just_tapped and tapped(game_menu_rect):
            scene = "pause"

        # ----------------------------------
        # GAME UPDATE
        # ----------------------------------

        if scene == "game" and not game["dead"]:

            left = (
                keys[pygame.K_a]
                or keys[pygame.K_LEFT]
                or held(btn_left)
            )

            right = (
                keys[pygame.K_d]
                or keys[pygame.K_RIGHT]
                or held(btn_right)
            )

            up = (
                keys[pygame.K_w]
                or keys[pygame.K_UP]
                or held(btn_up)
            )

            down = (
                keys[pygame.K_s]
                or keys[pygame.K_DOWN]
                or held(btn_down)
            )

            sprint = (
                keys[pygame.K_LSHIFT]
                or keys[pygame.K_RSHIFT]
                or held(btn_sprint)
            )

            # Movement and stamina
            speed = 5

            if sprint and game["stamina"] > 0:
                speed = 9
                game["stamina"] = max(
                    0, game["stamina"] - 1.5
                )
            else:
                game["stamina"] = min(
                    100, game["stamina"] + 0.5
                )

            dx = (int(right) - int(left)) * speed
            dy = (int(down) - int(up)) * speed

            player.x = max(
                0, min(W - player.width, player.x + dx)
            )

            player.y = max(
                0, min(PLAY_H - player.height, player.y + dy)
            )

            # Move enemies
            enemy_speed = MODE_SPEEDS[game["mode"]]

            red.y += enemy_speed
            green.x += enemy_speed

            # Reset red enemy after it leaves the screen
            if red.top > PLAY_H:
                red.y = -random.randint(120, 650)
                red.x = random.randint(0, W - red.width)

            # Reset green enemy after it leaves the screen
            if green.left > W:
                green.x = -random.randint(120, 650)
                green.y = random.randint(
                    0, PLAY_H - green.height
                )

            # Collect coin
            if player.colliderect(coin):
                game["score"] += 1

                coin.x = random.randint(
                    0, W - coin.width
                )

                coin.y = random.randint(
                    0, PLAY_H - coin.height
                )

            # Collision with enemies
            if (
                player.colliderect(red)
                or player.colliderect(green)
            ):
                game["dead"] = True

                save_record(
                    game["mode"],
                    game["score"]
                )

                records = load_records()
                award_coins(game["score"])

        # ----------------------------------
        # RESTART AFTER GAME OVER
        # ----------------------------------

        elif (
            scene == "game"
            and game["dead"]
            and just_tapped
            and not tapped(game_menu_rect)
        ):
            start_game(game["mode"])

        # ----------------------------------
        # HUD
        # ----------------------------------

        # Stamina bar
        pygame.draw.rect(
            screen, (50, 50, 50),
            (10, 10, 200, 15)
        )

        bar_width = int(
            game["stamina"] / 100 * 200
        )

        pygame.draw.rect(
            screen, CYAN,
            (10, 10, bar_width, 15)
        )

        pygame.draw.rect(
            screen, WHITE,
            (10, 10, 200, 15), 2
        )

        draw_text(
            MODE_LABELS[game["mode"]],
            font_mode, UI_TEXT,
            (10, 35)
        )

        draw_text(
            f"Score: {game['score']}",
            font_text, UI_TEXT,
            (W - 150, 10)
        )

        draw_button(
            game_menu_rect,
            "MENU",
            color=button_color(),
            label_color=UI_TEXT,
            font=font_small
        )

        # ----------------------------------
        # ENEMY WARNING SYSTEM
        # ----------------------------------

        if not game["dead"]:

            warning_color = (255, 65, 65)

            # Red enemy approaching from above
            if -320 < red.y < 0:

                centered_text(
                    "! ENEMY ABOVE !",
                    font_warn,
                    warning_color,
                    (W // 2, 82)
                )

                pygame.draw.polygon(
                    screen,
                    warning_color,
                    [
                        (W // 2, 108),
                        (W // 2 - 13, 88),
                        (W // 2 + 13, 88)
                    ]
                )

            # Green enemy approaching from the left
            if -320 < green.x < 0:

                centered_text(
                    "! ENEMY LEFT !",
                    font_warn,
                    warning_color,
                    (W // 2, 130)
                )

                pygame.draw.polygon(
                    screen,
                    warning_color,
                    [
                        (18, PLAY_H // 2),
                        (38, PLAY_H // 2 - 13),
                        (38, PLAY_H // 2 + 13)
                    ]
                )

        # ----------------------------------
        # GAME OBJECTS
        # ----------------------------------

        enemy_color = item_color("enemy", RED)
        coin_color = item_color("coin", YELLOW)
        player_color = item_color("player", WHITE)

        pygame.draw.rect(
            screen, enemy_color, red
        )

        pygame.draw.rect(
            screen, enemy_color, green
        )

        pygame.draw.ellipse(
            screen, coin_color, coin
        )

        # Player blinking animation after losing
        if (
            not game["dead"]
            or (game["blink"] // 8) % 2 == 0
        ):
            pygame.draw.rect(
                screen, player_color, player
            )

            equipped_accessory(player)

        # ----------------------------------
        # GAME OVER SCREEN
        # ----------------------------------

        if game["dead"]:

            game["blink"] += 1

            overlay = pygame.Surface(
                (W, 130),
                pygame.SRCALPHA
            )

            overlay.fill((0, 0, 0, 210))
            screen.blit(overlay, (0, 210))

            centered_text(
                "YOU LOST!",
                font_warn,
                UI_TEXT,
                (W // 2, 240)
            )

            centered_text(
                f"Score: {game['score']}",
                font_text,
                UI_TEXT,
                (W // 2, 275)
            )

            centered_text(
                "Tap anywhere to restart",
                font_menu,
                UI_TEXT,
                (W // 2, 310)
            )

        # ----------------------------------
        # VIRTUAL GAMEPAD
        # ----------------------------------

        draw_control(btn_up, "UP")
        draw_control(btn_down, "DN")
        draw_control(btn_left, "LT")
        draw_control(btn_right, "RT")

        draw_control(
            btn_sprint,
            "SPRINT",
            (150, 50, 50)
        )

    # ======================================
    # DISPLAY
    # ======================================

    scaled = pygame.transform.scale(
        screen,
        (DISPLAY_W, DISPLAY_H)
    )

    display.blit(scaled, (0, 0))
    pygame.display.flip()

# ==========================================
# EXIT
# ==========================================

pygame.quit()