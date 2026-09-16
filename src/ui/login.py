from tkinter import messagebox
import string
import customtkinter as ctk
from .firebase_auth import login_user


def create_login_page(parent, router):
#functions--------------------------------------------------------------------
    def handle_login():
        email = login_email_entry.get().strip()
        password = login_password_entry.get().strip()

        if not email or not password:
            messagebox.showerror("Error", "All fields are required to procced")
            return

        result = login_user(email, password)

        if result["success"]:
            messagebox.showinfo("Logged in", "Logged in succesfully")
        else:
            messagebox.showerror("Login failed", result["error"])

#panels-----------------------------------------------------------------------
    login_card = ctk.CTkFrame(parent, width=400, height=500)
    login_card.grid_propagate(False)

    login_card.columnconfigure(0, weight=1)
    login_card.rowconfigure(0, weight=1)

    login_input_container = ctk.CTkFrame(login_card, fg_color="transparent")
    login_input_container.grid(row=0, column=0)

#login_card-------------------------------------------------------------------
    login_email_entry = ctk.CTkEntry(login_input_container, placeholder_text="Please enter your email", width=200)
    login_email_entry.grid(row=0, column=0, pady=10)

    login_password_entry = ctk.CTkEntry(login_input_container, show="*", placeholder_text="Please enter your password", width=200)
    login_password_entry.grid(row=1, column=0, pady=10)

    incorrect_label = ctk.CTkLabel(login_input_container, text="Your password is incorrect",
                            font=("Airial", 10), text_color=("red"))
    incorrect_label.grid(row=2, column=0, pady=5)

    login_user_button = ctk.CTkButton(login_input_container, text="Login", hover_color="light blue", command=handle_login)
    login_user_button.grid(row=3, column=0, pady=10)

    reset_password_button = ctk.CTkButton(login_input_container, text="Forgot your password? Reset it.", fg_color="transparent",  hover_color=("gray85", "gray20"), width=50, command=lambda: router("reset_password"))
    reset_password_button.grid(row=4, column=0, pady=10)

    signup_button = ctk.CTkButton(login_input_container, text="Don't have a account? Sign up.", fg_color="transparent",  hover_color=("gray85", "gray20"), width=50, command=lambda: router("signup"))
    signup_button.grid(row=5, column=0, pady=10)

    return login_card