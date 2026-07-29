import tkinter as tk
from tkinter import ttk, messagebox

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from controllers.room_controller import RoomController


controller = RoomController()


# ================= ADD ROOM =================

def add_room():

    try:
        controller.add_room(
            room_no_entry.get(),
            room_type_entry.get(),
            capacity_entry.get()
        )
    except ValueError as e:
        messagebox.showwarning("Warning", str(e))
        return
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return

    messagebox.showinfo("Success", "Room Added Successfully")
    clear_fields()
    view_rooms()


# ================= VIEW ROOMS =================

def view_rooms():

    for row in table.get_children():
        table.delete(row)

    rooms = controller.get_all_rooms()

    for room in rooms:
        table.insert("", tk.END, values=room)


# ================= SEARCH ROOM =================

def search_room():

    keyword = search_entry.get()

    for row in table.get_children():
        table.delete(row)

    rooms = controller.search_room(keyword)

    for room in rooms:
        table.insert("", tk.END, values=room)


# ================= DELETE ROOM =================

def delete_room():

    selected = table.focus()
    data = table.item(selected)
    values = data["values"]

    if not values:
        messagebox.showwarning("Warning", "Select Room First")
        return

    room_no = values[0]

    try:
        result = controller.delete_room(room_no)
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return

    messagebox.showinfo("Message", result)
    view_rooms()


# ================= CLEAR =================

def clear_fields():
    room_no_entry.delete(0, tk.END)
    room_type_entry.delete(0, tk.END)
    capacity_entry.delete(0, tk.END)


# ================= WINDOW =================

root = tk.Tk()
root.title("Room Management System")
root.geometry("900x650")

title = tk.Label(root, text="Room Management", font=("Arial", 22, "bold"))
title.pack(pady=15)

# ================= FORM =================

form = tk.Frame(root)
form.pack()

tk.Label(form, text="Room Number").grid(row=0, column=0, padx=5, pady=5)
room_no_entry = tk.Entry(form)
room_no_entry.grid(row=0, column=1)

tk.Label(form, text="Room Type").grid(row=1, column=0, padx=5, pady=5)
room_type_entry = tk.Entry(form)
room_type_entry.grid(row=1, column=1)

tk.Label(form, text="Capacity").grid(row=2, column=0, padx=5, pady=5)
capacity_entry = tk.Entry(form)
capacity_entry.grid(row=2, column=1)

# ================= BUTTONS =================

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

tk.Button(button_frame, text="Add Room", command=add_room).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="View Rooms", command=view_rooms).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Delete Room", command=delete_room).grid(row=0, column=2, padx=10)

# ================= SEARCH =================

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

tk.Label(search_frame, text="Search Room").grid(row=0, column=0, padx=5)

search_entry = tk.Entry(search_frame, width=25)
search_entry.grid(row=0, column=1, padx=5)

tk.Button(search_frame, text="Search", command=search_room).grid(row=0, column=2, padx=5)
tk.Button(search_frame, text="Clear", command=view_rooms).grid(row=0, column=3, padx=5)

# ================= TABLE =================

table = ttk.Treeview(
    root,
    columns=("Room No", "Room Type", "Capacity", "Occupied", "Status"),
    show="headings"
)

for col in table["columns"]:
    table.heading(col, text=col)

table.pack(fill="both", expand=True, pady=20)

view_rooms()

root.mainloop()
