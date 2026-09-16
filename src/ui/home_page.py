from tkinter import messagebox
import string
import customtkinter as ctk
from src.data.images import eye_icon, eye_off_icon

def create_home_page(parent, router):
    home_card = ctk.CTkFrame(parent)
    home_card.grid_propagate(False)
    
    home_card.columnconfigure(0, weight=1)
    home_card.rowconfigure(0, weight=1)

    home_container = ctk.CTkFrame(home_card, fg_color="transparent")
    home_container.grid(row=0, column=0)