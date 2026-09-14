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
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    confirm_password = confirm_password_entry.get().strip()

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if signup_user_button:
        if has_upper and has_lower and has_digit and has_special:
            if len(password) >= min_legnth:
                if password == confirm_password:
                    match_label.grid_remove()
                    result = signup_user(email, password)
                    
                    if result["success"]:
                        messagebox.showinfo("Account Created", "Account Created succesfully")
                    else:
                        messagebox.showerror("Signup failed", result["error"])
                elif password != confirm_password:
                    match_label.grid(column=0, row=7)
    
        elif not email or not password:
            messagebox.showerror("Error", "All fields are required to procced")
            return
    else:
        if not has_upper and not has_lower and not has_digit and has_special: 
            upper_label.grid(column=0, row=3),
            lower_label.grid(column=0, row=4),
            digit_label.grid(column=0, row=5),
            special_label.grid(column=0, row=6)
            signup_user_button.grid(column=0, row=8)
        else:
            upper_label.grid_remove()
            lower_label.grid_remove()
            digit_label.grid_remove()
            special_label.grid_remove()
            signup_user_button.grid(column=0, row=3)


#interface--------------------------------------------------------------------
root = ttk.Window(title="PortalOne SignUp", themename="lumen")
root.attributes('-fullscreen', True)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#panels-----------------------------------------------------------------------
main_panel = ttk.Frame(root)
main_panel.grid(column=0, row=0)

#main_panel-------------------------------------------------------------------
email_label = ttk.Label(main_panel, text="Email:")
email_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

email_entry = ttk.Entry(main_panel)
email_entry.grid(column=1, row=0, padx=5, pady=5)

password_label = ttk.Label(main_panel, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

password_entry = ttk.Entry(main_panel, show="*")
password_entry.grid(column=1, row=1, padx=5, pady=5)

confirm_password_label = ttk.Label(main_panel, text="Confirm Password:")
confirm_password_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

confirm_password_entry = ttk.Entry(main_panel, show="*")
confirm_password_entry.grid(column=1, row=2, padx=5, pady=5)

upper_label = ttk.Label(main_panel, text="The password must have a uppercase character", font=("Airal", 10))
upper_label.grid(column=0, row=3)

lower_label = ttk.Label(main_panel, text="The password must have a lowercase character", font=("Airal", 10))
lower_label.grid(column=0, row=4)

digit_label = ttk.Label(main_panel, text="The password must have a digit", font=("Airal", 10))
digit_label.grid(column=0, row=5)

special_label = ttk.Label(main_panel, text="The password must have a uppercase", font=("Airal", 10))
special_label.grid(column=0, row=6)

match_label = ttk.Label(main_panel, text="Passwords don't match", font=("Arial", 10))
match_label.grid(column=0, row=7)

signup_user_button = ttk.Button(main_panel, text="Create account", command=handle_signup)
signup_user_button.grid(column=0, row=8)

handle_signup()

root.mainloop()
