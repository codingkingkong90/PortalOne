from ui import login, sign_up, reset_passwrod
from tkinter import messagebox
import string
import customtkinter as ctk

root = ctk.CTK()
root.title("PortalOne")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
root.attributes('-fullscreen', True)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

active_frame = None

def navigate_to(page_name):
    global active_frame

    if active_frame is not None:
        active_frame.grid_forget()
        active_frame.destroy()

    if page_name == "signup":
        active_frame = sign_up.create_signup_page(root, navigate_to)
    elif page_name == "login":
        active_frame = login.create_login_page(root, navigate_to)
    elif page_name == "reset_password":
        active_frame = reset_passwrod.create_reset_page(root, navigate_to)