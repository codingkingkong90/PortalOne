from tkinter import messagebox
import string
import customtkinter as ctk
from services.firestore import create_group_documents
from data.images import eye_icon, eye_off_icon

def create_group_page(parent, router):
#interface--------------------------------------------------------------------
    create_card = ctk.CTkFrame(parent, width=400, height=500)
    create_card.grid_propagate(False)
    
    create_card.columnconfigure(0, weight=1)
    create_card.rowconfigure(0, weight=1)

    create_input_container = ctk.CTkFrame(create_card, fg_color="transparent")
    create_input_container.grid(row=0, column=0)

#create_card------------------------------------------------------------------
    group_name_entry = ctk.CTkEntry(create_input_container, placeholder_text="Please enter a group name", width=280)
    group_name_entry.grid(row=0, column=0, pady=10)

    group_type_entry = ctk.CTkEntry(create_input_container, placeholder_text="Please enter a group type or make a custom group type", width=280)
    group_type_entry.grid(row=1, column=0, pady=10)

    group_description_entry = ctk.CTkEntry(create_input_container, placeholder_text="Please add a group description", width=280)
    group_description_entry.grid(row=0, column=0, pady=10)

    group_logo_entry = ctk.CTkEntry

    group_create_button = ctk.CTkButton(create_input_container, text="Create Group", hover_color="light blue", command=None)
    group_create_button.grid(row=5, column=0, pady=10)