from tkinter import messagebox
import string
import customtkinter as ctk
from data.images import eye_icon, eye_off_icon

def create_home_page(parent, router):
#interface--------------------------------------------------------------------
    home_card = ctk.CTkFrame(parent)
    home_card.grid_propagate(False)
    
    home_card.columnconfigure(0, weight=1)
    home_card.rowconfigure(0, weight=1)

    home_container = ctk.CTkFrame(home_card, fg_color="transparent")
    home_container.grid(row=0, column=0)

#home_container-------------------------------------------------------
    create_group = ctk.CTkButton(home_container, text="Create a Group", hover_color="light blue", command=lambda: router("create_group"))
    create_group.grid(row=1, column=0, pady=10)

    join_group = ctk.CTkButton(home_container, text="Join a Group", hover_color="light blue", command=None)
    join_group.grid(row=2, column=0, pady=10)

    return home_card