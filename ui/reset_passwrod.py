import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import messagebox
import string
import customtkinter as ctk

#interface--------------------------------------------------------------------
root = ctk.CTk()
root.title("PortalOne Reset Password")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root.attributes('-fullscreen', True)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)