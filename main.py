from app import login
from app import sign_up
from app import reset_password
from app import home_page
from tkinter import messagebox
import string
import customtkinter as ctk


root = ctk.CTk()
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
        active_frame = reset_password.create_reset_page(root, navigate_to)
    elif active_frame == "home_page":
        active_frame = home_page.create_home_page(root, navigate_to)

    active_frame.pack(expand=True)

navigate_to("login")
root.mainloop()