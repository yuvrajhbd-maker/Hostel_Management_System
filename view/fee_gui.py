import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from controllers.fee_controller import FeeController


controller = FeeController()


# ================= SAVE FEE =================

def save_fee():

    if student_combo.get() == "" or total_entry.get() == "" or paid_entry.get() == "":
        messagebox.showwarning("Warning", "Fill All Fields")
        return

    student_id = student_dict[student_combo.get()]

    try:
        controller.add_fee(
            student_id,
            total_entry.get(),
            paid_entry.get(),
            date_entry.get(),
            mode_combo.get()
        )
    except ValueError as e:
        messagebox.showwarning("Warning", str(e))
        return
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return

    messagebox.showinfo("Success", "Fee Added Successfully")
    clear_fields()
    load_fee()


# ================= AUTO DUE =================

def calculate_due(event=None):

    try:
        total = float(total_entry.get())
        paid = float(paid_entry.get())

        due_entry.delete(0, tk.END)
        due_entry.insert(0, total - paid)
    except ValueError:
        pass


# ================= CLEAR =================

def clear_fields():
    total_entry.delete(0, tk.END)
    paid_entry.delete(0, tk.END)
    due_entry.delete(0, tk.END)


# ================= VIEW FEE =================

def load_fee():

    for row in table.get_children():
        table.delete(row)

    fees = controller.get_all_fee()

    for fee in fees:
        table.insert("", tk.END, values=fee)


# ================= DELETE FEE =================

def delete_fee():

    selected = table.focus()
    data = table.item(selected)
    values = data["values"]

    if not values:
        messagebox.showwarning("Warning", "Select Fee Record")
        return

    try:
        controller.delete_fee(values[0])
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return

    messagebox.showinfo("Deleted", "Fee Deleted")
    load_fee()


# ================= WINDOW =================

root = tk.Tk()
root.title("Fee Collection System")
root.geometry("900x650")

title = tk.Label(root, text="Fee Collection", font=("Arial", 22, "bold"))
title.pack(pady=15)

# ================= FORM =================

form = tk.Frame(root)
form.pack()

# Student

tk.Label(form, text="Student").grid(row=0, column=0)

students = controller.get_students()

student_dict = {}
student_list = []

for s in students:
    student_dict[s[1]] = s[0]
    student_list.append(s[1])

student_combo = ttk.Combobox(form, values=student_list)
student_combo.grid(row=0, column=1, padx=10, pady=5)

# Total Fee

tk.Label(form, text="Total Fee").grid(row=1, column=0)
total_entry = tk.Entry(form)
total_entry.grid(row=1, column=1)

# Paid

tk.Label(form, text="Paid Amount").grid(row=2, column=0)
paid_entry = tk.Entry(form)
paid_entry.grid(row=2, column=1)

paid_entry.bind("<KeyRelease>", calculate_due)

# Due

tk.Label(form, text="Due Amount").grid(row=3, column=0)
due_entry = tk.Entry(form)
due_entry.grid(row=3, column=1)

# Date

tk.Label(form, text="Payment Date").grid(row=4, column=0)
date_entry = tk.Entry(form)
date_entry.insert(0, str(date.today()))
date_entry.grid(row=4, column=1)

# Mode

tk.Label(form, text="Payment Mode").grid(row=5, column=0)
mode_combo = ttk.Combobox(form, values=["Cash", "UPI", "Card"])
mode_combo.grid(row=5, column=1)

# Buttons

btn = tk.Frame(root)
btn.pack(pady=15)

tk.Button(btn, text="Save Fee", command=save_fee).grid(row=0, column=0, padx=10)
tk.Button(btn, text="View Fee", command=load_fee).grid(row=0, column=1, padx=10)
tk.Button(btn, text="Delete", command=delete_fee).grid(row=0, column=2, padx=10)

# TABLE

table = ttk.Treeview(
    root,
    columns=("ID", "Student", "Total", "Paid", "Due", "Date", "Mode"),
    show="headings"
)

for col in table["columns"]:
    table.heading(col, text=col)

table.pack(fill="both", expand=True, pady=20)

load_fee()

root.mainloop()
