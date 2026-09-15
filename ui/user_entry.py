import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import messagebox
import string
import customtkinter as ctk
from firebase_auth import login_user, signup_user

import warnings
import requests
from urllib3.exceptions import InsecureRequestWarning

# 1. Hide the insecure request warning messages
warnings.simplefilter("ignore", InsecureRequestWarning)

# 2. Force every single web request in the app to use verify=False
original_request = requests.Session.request


def patched_request(self, *args, **kwargs):
    kwargs["verify"] = False  # Tells the library to ignore the school certificate
    return original_request(self, *args, **kwargs)


requests.Session.request = patched_request

#interface--------------------------------------------------------------------
root = ctk.CTk()
root.title("PortalOne SignUp")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root.attributes('-fullscreen', True)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#global variables-------------------------------------------------------------
password = ctk.StringVar()
min_legnth = 8

#functions--------------------------------------------------------------------
'''
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
'''
def handle_signup():
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if signup_user_button:
        result = signup_user(email, password)
        
        if result["success"]:
            messagebox.showinfo("Account Created", "Account Created succesfully")
        else:
            messagebox.showerror("Signup failed", result["error"])
    

    elif not email or not password:
        messagebox.showerror("Error", "All fields are required to procced")
        return

def check_requirement(condition, label):
    if condition:
        label.grid_remove()
    else:
        label.grid()


def check_password(*args):
    global password, confirm_password

    password = password_entry.get().strip()
    confirm_password = confirm_password_entry.get().strip()

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    has_legnth = len(password) >= min_legnth
    has_match = password == confirm_password
    

    check_requirement(has_upper, upper_label)
    check_requirement(has_lower, lower_label)
    check_requirement(has_digit, digit_label)
    check_requirement(has_special, special_label)
    check_requirement(has_legnth, legnth_label)
    check_requirement(has_match, match_label)

    if(
        has_upper
        and has_lower
        and has_digit
        and has_special
        and has_legnth
        and has_match
    ):
        handle_signup()

password.trace_add("write", check_password)

def show_login():
    if login_button:
        signup_card.grid_remove()
        login_card.grid()



#panels-----------------------------------------------------------------------
signup_card = ctk.CTkFrame(root, width=400, height=500)
signup_card.grid(column=0, row=0, sticky="")
signup_card.grid_propagate(False)

signup_card.columnconfigure(0, weight=1)
signup_card.rowconfigure(0, weight=1)

signup_input_container = ctk.CTkFrame(signup_card, fg_color="transparent")
signup_input_container.grid(row=0, column=0)

login_card = ctk.CTkFrame(root, width=400, height=500)
login_card.grid(column=0, row=0, sticky="")
login_card.grid_propagate(False)

login_card.columnconfigure(0, weight=1)
login_card.rowconfigure(0, weight=1)


#main_panel-------------------------------------------------------------------

email_entry = ctk.CTkEntry(signup_input_container, placeholder_text="Please enter your email", width=200)
email_entry.grid(row=0, column=0, pady=10)

password_entry = ctk.CTkEntry(signup_input_container, show="*", placeholder_text="Please enter a password", textvariable=password, width=200)
password_entry.grid(row=1, column=0, pady=10)

confirm_password_entry = ctk.CTkEntry(signup_input_container, show="*", placeholder_text="Please re-enter your password", width=200)
confirm_password_entry.grid(row=2, column=0, pady=10)

upper_label = ctk.CTkLabel(signup_input_container, text="Your password must have atleast one capital letter",
                           font=("Airial", 10), text_color=("red"))
upper_label.grid(row=3, column=0, pady=5)

lower_label = ctk.CTkLabel(signup_input_container, text="Your password must have atleast one lowercase letter",
                           font=("Airial", 10), text_color=("red"))
lower_label.grid(row=4, column=0, pady=5)

digit_label = ctk.CTkLabel(signup_input_container, text="Your password must have atleast one digit",
                           font=("Airial", 10), text_color=("red"))
digit_label.grid(row=5, column=0, pady=5)

special_label = ctk.CTkLabel(signup_input_container, text="Your password must have atleast one special character",
                           font=("Airial", 10), text_color=("red"))
special_label.grid(row=6, column=0, pady=5)

legnth_label = ctk.CTkLabel(signup_input_container, text="Your password must be atleast 8 characters",
                           font=("Airial", 10), text_color=("red"))
legnth_label.grid(row=7, column=0, pady=5)

match_label = ctk.CTkLabel(signup_input_container, text="Your password must match",
                           font=("Airial", 10), text_color=("red"))
match_label.grid(row=8, column=0, pady=5)

signup_user_button = ctk.CTkButton(signup_input_container, text="Create Account", hover_color="light blue", command=check_password)
signup_user_button.grid(row=9, column=0, pady=10)

login_button = ctk.CTkButton(signup_input_container, text="Already have a account? Log in.", fg_color="transparent",  hover_color=("gray85", "gray20"), width=50, command=check_password)
login_button.grid(row=9, column=0, pady=10)

#login_card-------------------------------------------------------------------

root.mainloop()
