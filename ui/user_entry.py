import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import messagebox
import string
from firebase_auth import login_user, signup_user

#functions--------------------------------------------------------------------
def handle_login():
    email = email_entry.get().strip
    password = password_entry.get().strip

    if not email or not password:
        messagebox.showerror("Error", "All fields are required to procced")
        return

    result = login_user(email, password)

    if result["success"]:
        messagebox.showinfo("Logged in", "Logged in succesfully")
    else:
        messagebox.showerror("Login failed", result["error"])

def handle_signup():
    min_legnth = 8
    while True:
        email = email_entry.get().strip
        password = password_entry.get().strip

        if not email or not password:
            messagebox.showerror("Error", "All fields are required to procced")
            return

        if len(password) >= min_legnth:
            result = signup_user(email, password)
            
            if result["success"]:
                messagebox.showinfo("Account Created", "Account Created succesfully")
            else:
                messagebox.showerror("Signup failed", result["error"])    
    
def check_password(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    

#interface--------------------------------------------------------------------
root = ttk.Window(title="PortalOne SignUp", themename="lumen")
root.attributes('-fullscreen', True)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#panels-----------------------------------------------------------------------
main_panel = ttk.Frame(root)
main_panel.grid(column=0, row=0)

error_panel = ttk.Frame(root)

#main_panel-------------------------------------------------------------------
email_label = ttk.Label(main_panel, text="Email:")
email_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

email_entry = ttk.Entry(main_panel)
email_entry.grid(column=1, row=0, padx=5, pady=5)

password_label = ttk.Label(main_panel, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

password_entry = ttk.Entry(main_panel, show="*")
password_entry.grid(column=1, row=1, padx=5, pady=5)

#error_panel------------------------------------------------------------------



root.mainloop()
