import tkinter as tk
from tkinter import messagebox

import subprocess
import sys
import os

# Make project root importable regardless of the current working directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from controllers.auth_controller import AuthController


auth_controller = AuthController()


# ================= SHOW PASSWORD =================

def show_password():

    if show_pass_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


# ================= LOGIN =================

def login(event=None):

    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning(
            "Warning",
            "Please Enter Username and Password"
        )
        return

    try:
        success = auth_controller.login(username, password)

        if success:
            messagebox.showinfo("Success", "Login Successful")
            root.destroy()

            dashboard_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dashboard.py")
            subprocess.Popen([sys.executable, dashboard_path])
        else:
            messagebox.showerror("Failed", "Invalid Username or Password")

    except Exception as e:
        messagebox.showerror("Database Error", str(e))


# ================= MAIN WINDOW =================

root = tk.Tk()
root.title("Hostel Management System Login")
root.geometry("500x450")
root.resizable(False, False)

# Background
root.configure(bg="#1e3c72")

# ================= LOGIN CARD =================

login_frame = tk.Frame(root, bg="white", width=350, height=330)
login_frame.place(relx=0.5, rely=0.5, anchor="center")
login_frame.pack_propagate(False)

# Heading

title = tk.Label(login_frame, text="Hostel Management", font=("Arial", 18, "bold"), bg="white")
title.pack(pady=20)

subtitle = tk.Label(login_frame, text="Admin Login", font=("Arial", 13), bg="white")
subtitle.pack()

# Username

tk.Label(login_frame, text="Username", bg="white", font=("Arial", 11)).pack(pady=5)

username_entry = tk.Entry(login_frame, width=30, font=("Arial", 11))
username_entry.pack()

# Password

tk.Label(login_frame, text="Password", bg="white", font=("Arial", 11)).pack(pady=5)

password_entry = tk.Entry(login_frame, width=30, show="*", font=("Arial", 11))
password_entry.pack()

# Show Password

show_pass_var = tk.BooleanVar()

show_check = tk.Checkbutton(
    login_frame,
    text="Show Password",
    variable=show_pass_var,
    command=show_password,
    bg="white"
)
show_check.pack(pady=10)

# Login Button

login_btn = tk.Button(
    login_frame,
    text="Login",
    width=20,
    height=2,
    bg="#2196F3",
    fg="white",
    font=("Arial", 11, "bold"),
    command=login
)
login_btn.pack(pady=10)

# Enter Key Login
root.bind("<Return>", login)

username_entry.focus()

root.mainloop()
