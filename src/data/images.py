from PIL import Image
from pathlib import Path
import customtkinter as ctk

def make_icon_white(path):
    image = Image.open(path).convert("RGBA")

    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            if a > 0:
                pixels[x, y] = (255, 255, 255, a)

    return image

BASE_DIR = Path(__file__).resolve().parent.parent

eye_icon = ctk.CTkImage(
    light_image=make_icon_white(BASE_DIR / "assests" / "icons" / "visibility.png"),
    dark_image=make_icon_white(BASE_DIR / "assests" / "icons" / "visibility.png"),
    size=(20,20)
)

eye_off_icon = ctk.CTkImage(
    light_image=make_icon_white(BASE_DIR / "assests" / "icons" / "visibility_off.png"),
    dark_image=make_icon_white(BASE_DIR / "assests" / "icons" / "visibility_off.png"),
    size=(20,20)
)