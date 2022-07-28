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
    {"id": "1024_byte_intros", "label": "1024 Byte intros"},
    {"id": "512_byte_intros", "label": "512 Byte intros"},
    {"id": "256_byte_intros", "label": "256 Byte intros"},
    {"id": "128_byte_intros", "label": "128 Byte intros"},
    {"id": "64_byte_intros", "label": "64 Byte intros"},
    {"id": "32_byte_intros", "label": "32 Byte intros"},
    {"id": "16_byte_intros", "label": "16 Byte intros"},
    {"id": "8_byte_intros", "label": "8 Byte intros"},
    {"id": "tiny_executable_graphics", "label": "Tiny executable graphics"},
]


def get_entry_dir_path(category: str, flavor: str) -> Path:
    return BASE_DATA_PATH / Path(category) / Path(flavor)
