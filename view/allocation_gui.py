import tkinter as tk
from tkinter import ttk, messagebox

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from controllers.allocation_controller import AllocationController


controller = AllocationController()

# Store name -> id lookups for the dropdowns
student_data = {}
room_data = {}


# ================= LOAD STUDENTS =================

def load_students():

    students = controller.get_students()

    for student in students:
        student_data[student[1]] = student[0]

    student_combo["values"] = list(student_data.keys())


# ================= LOAD ROOMS =================

def load_rooms():

    rooms = controller.get_available_rooms()

    for room in rooms:
        room_data[str(room[0])] = room[0]

    room_combo["values"] = list(room_data.keys())


# ================= ALLOCATE ROOM =================

def allocate():

    student_name = student_combo.get()
    room_no = room_combo.get()
    date = date_entry.get()

    if student_name == "" or room_no == "" or date == "":
        messagebox.showwarning("Warning", "Fill All Details")
        return

    try:
        result = controller.allocate_room(
            student_data[student_name],
            room_data[room_no],
            date
        )
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return

    messagebox.showinfo("Result", result)

    view_allocations()
    load_rooms()


# ================= VIEW ALLOCATION =================

def view_allocations():

    for row in table.get_children():
        table.delete(row)

    data = controller.get_all_allocations()

    for row in data:
        table.insert("", tk.END, values=row)


# ================= WINDOW =================

root = tk.Tk()
root.title("Room Allocation")
root.geometry("700x600")

title = tk.Label(root, text="Room Allocation", font=("Arial", 20, "bold"))
title.pack(pady=20)

# Student Dropdown

tk.Label(root, text="Select Student").pack()

student_combo = ttk.Combobox(root, state="readonly")
student_combo.pack()

# Room Dropdown

tk.Label(root, text="Select Room").pack()

room_combo = ttk.Combobox(root, state="readonly")
room_combo.pack()

# Date

tk.Label(root, text="Allocation Date (YYYY-MM-DD)").pack()

date_entry = tk.Entry(root)
date_entry.pack()

# Button

allocate_btn = tk.Button(root, text="Allocate Room", command=allocate)
allocate_btn.pack(pady=15)

# Table

table = ttk.Treeview(
    root,
    columns=("ID", "Student", "Room", "Date"),
    show="headings"
)

for col in table["columns"]:
    table.heading(col, text=col)

table.pack(fill="both", expand=True)

# Load Data

load_students()
load_rooms()
view_allocations()

root.mainloop()
