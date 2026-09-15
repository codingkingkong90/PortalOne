from tkinter import messagebox
import string
import customtkinter as ctk

def create_reset_page(parent, router):
#interface--------------------------------------------------------------------
    reset_password_card = ctk.CTkFrame(parent, width=400, height=500)
    reset_password_card.grid_propagate(False)

    reset_password_card.columnconfigure(0, weight=1)
    reset_password_card.rowconfigure(0, weight=1)

    reset_input_container = ctk.CTkFrame(reset_password_card, fg_color="transparent")
    reset_input_container.grid(row=0, column=0)

#reset_input_container--------------------------------------------------------
    login_email_entry = ctk.CTkEntry(login_input_container, placeholder_text="Please enter your email", width=200)
    login_email_entry.grid(row=0, column=0, pady=10)