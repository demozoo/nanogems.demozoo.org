from pathlib import Path
import os

BASE_PUBLIC_PATH = "./public/data"

BASE_PUBLIC_ROOT_PATH = Path("./public")
os.makedirs(BASE_PUBLIC_ROOT_PATH, exist_ok=True)

BASE_DATA_PATH = BASE_PUBLIC_ROOT_PATH / Path("data")
os.makedirs(BASE_DATA_PATH, exist_ok=True)

BASE_THUMBNAIL_PATH = BASE_PUBLIC_ROOT_PATH / Path("img/thumbnails")
os.makedirs(BASE_THUMBNAIL_PATH, exist_ok=True)

DEFAULT_THUMBNAIL = "default.png"

# Order in list is Order displayed (left to right)
FLAVORS = [
    {"id": "highend", "label": "Highend"},
    {"id": "oldschool", "label": "Oldschool"},
    {"id": "fantasy", "label": "Fantasy Consoles / VM"},
]

# Order in list is Order displayed (top to bottom)
CATEGORIES = [
    {"id": "1024_byte_intros", "label": "1024B intros"},
    {"id": "512_byte_intros", "label": "512B intros"},
    {"id": "256_byte_intros", "label": "256B intros"},
    {"id": "128_byte_intros", "label": "128B intros"},
    {"id": "64_byte_intros", "label": "64B intros"},
    {"id": "32_byte_intros", "label": "32B intros"},
    {"id": "16_byte_intros", "label": "16B intros"},
    {"id": "8_byte_intros", "label": "8B intros"},
    {"id": "tiny_executable_graphics", "label": "Tiny executable graphics"},
]

DISPLAY_TAGS = [
    "textmode",
    "header-excluded",
    "tiny-intro-with-sound",
    "code-challenge",
    "chessboard",
    "glitch",
    "xor-pattern",
    "fractal",
    "floorcasting",
    "tunnel",
    "raycasting",
    "raymarching",
    "raytracing",
    "checkerboard",
    "sierpinski",
    "automata",
    "fire-effect",
    "matrix-effect",
    "xor-pattern",
    "twister",
    "noise",
    "rotozoomer",
    "vectors",
    "midi",
    "bytebeat",
    "plasma",
    "sine-dots",
    "metaballs"
]


def get_entry_dir_path(category: str, flavor: str) -> Path:
    return BASE_DATA_PATH / Path(category) / Path(flavor)
