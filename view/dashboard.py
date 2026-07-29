import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

# Project root path add
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

VIEW_DIR = os.path.dirname(os.path.abspath(__file__))

from controllers.dashboard_controller import DashboardController


# ================= OPEN MODULES =================

def _open(script_name):
    subprocess.Popen([sys.executable, os.path.join(VIEW_DIR, script_name)])


def open_student():
    _open("student_gui.py")


def open_room_management():
    _open("room_gui.py")


def open_allocation():
    _open("allocation_gui.py")


def open_fee():
    _open("fee_gui.py")


def open_report():
    _open("report_gui.py")


# ================= LOGOUT =================

def logout():
    result = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if result:
        root.destroy()


# ================= DASHBOARD DATA =================

dashboard_controller = DashboardController()
summary = dashboard_controller.get_summary()

students = summary["total_students"]
rooms = summary["total_rooms"]
available = summary["available_rooms"]
collection = summary["total_collection"]
due_fee = summary["total_due_fee"]


# ================= MAIN WINDOW =================

root = tk.Tk()
root.configure(bg="#f2f2f2")
root.title("Hostel Management System Dashboard")
root.geometry("1150x650")

# Heading

title = tk.Label(root, text="Hostel Management System", font=("Arial", 25, "bold"), bg="#f2f2f2")
title.pack(pady=20)

welcome = tk.Label(root, text="Welcome Admin", font=("Arial", 14))
welcome.pack()

# ================= CARDS FRAME =================

card_frame = tk.Frame(root)
card_frame.pack(pady=30)


# Card Function

def create_card(parent, title, value, column):
    frame = tk.Frame(parent, width=200, height=130, bg="white", relief="raised", borderwidth=2)
    frame.grid(row=0, column=column, padx=15)
    frame.pack_propagate(False)

    tk.Label(frame, text=title, font=("Arial", 12, "bold"), bg="white").pack(pady=15)
    tk.Label(frame, text=value, font=("Arial", 22, "bold"), bg="white").pack()


# Cards

create_card(card_frame, "Total Students", students, 0)
create_card(card_frame, "Total Rooms", rooms, 1)
create_card(card_frame, "Available Rooms", available, 2)
create_card(card_frame, "Collection", collection, 3)
create_card(card_frame, "Due Fee", due_fee, 4)


# ================= BUTTONS =================

btn_frame = tk.Frame(root)
btn_frame.pack(pady=30)

student_btn = tk.Button(
    btn_frame, text="Student Management", width=25, height=2,
    bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), command=open_student
)
student_btn.grid(row=0, column=0, padx=10, pady=10)

room_mgmt_btn = tk.Button(
    btn_frame, text="Room Management", width=25, height=2,
    bg="#9C27B0", fg="white", font=("Arial", 11, "bold"), command=open_room_management
)
room_mgmt_btn.grid(row=0, column=1, padx=10, pady=10)

allocation_btn = tk.Button(
    btn_frame, text="Room Allocation", width=25, height=2,
    bg="#2196F3", fg="white", font=("Arial", 11, "bold"), command=open_allocation
)
allocation_btn.grid(row=0, column=2, padx=10, pady=10)

fee_btn = tk.Button(
    btn_frame, text="Fee Collection", width=25, height=2,
    bg="#FF9800", fg="white", font=("Arial", 11, "bold"), command=open_fee
)
fee_btn.grid(row=1, column=0, padx=10, pady=10)

report_btn = tk.Button(
    btn_frame, text="Reports", width=25, height=2,
    bg="#009688", fg="white", font=("Arial", 11, "bold"), command=open_report
)
report_btn.grid(row=1, column=1, padx=10, pady=10)

logout_btn = tk.Button(
    btn_frame, text="Logout", width=25, height=2,
    bg="#F44336", fg="white", font=("Arial", 11, "bold"), command=logout
)
logout_btn.grid(row=1, column=2, padx=10, pady=10)

root.mainloop()
