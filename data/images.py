from PIL import Image
from pathlib import Path
from tkinter import filedialog
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

def create_logo_uploader(parent):
    selected_logo = {"path": None, "image": None}

    logo_preview = ctk.CTkLabel(
        parent,
        text="No logo selected",
        width=150,
        height=150,
    )

    logo_preview.grid(pady=10)

    def upload_logo():
        file_path = filedialog.askopenfilename(
            title="Select a Group Logo",
            filetypes=[
                ("Images", "*.png" "*jpg" "*jpeg"),
                ("PNG Files", "*png"),
                ("JPEG Files", "*jpg" "*jpeg")
            ] 
        )

        if not file_path:
            return

        image = Image.open(file_path)
        image.thumbnail((150, 150))

        logo_image = ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=image.size
        )

        logo_preview.configure(
            image=logo_image,
            text=""
        )

        selected_logo["path"] = file_path
        selected_logo["image"] = file_path

    upload_button = ctk.CTkButton(
        parent,
        text="Upload Logo",
        command=upload_logo
    )

    upload_button.grid(pady=10)

    return selected_logo

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