import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from controllers.student_controller import StudentController


controller = StudentController()

selected_student_id = None


# ================= SAVE STUDENT =================

def save_student():

    try:
        controller.add_student(
            name_entry.get(),
            father_entry.get(),
            gender_entry.get(),
            mobile_entry.get(),
            email_entry.get(),
            address_entry.get(),
            course_entry.get(),
            date_entry.get()
        )
    except ValueError as e:
        messagebox.showwarning("Warning", str(e))
        return
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return

    messagebox.showinfo("Success", "Student Added Successfully")
    clear_fields()
    load_students()


# ================= CLEAR FIELDS =================

def clear_fields():

    global selected_student_id
    selected_student_id = None

    name_entry.delete(0, tk.END)
    father_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    mobile_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)


# ================= VIEW STUDENTS =================

def load_students():

    for row in table.get_children():
        table.delete(row)

    students = controller.get_all_students()

    for student in students:
        table.insert(
            "", tk.END,
            values=(student[0], student[1], student[2], student[3], student[4], student[7], student[8])
        )


# ================= SEARCH STUDENT =================

def search_student():

    keyword = search_entry.get().strip()

    if keyword == "":
        messagebox.showwarning("Warning", "Please Enter Name or Mobile")
        load_students()
        return

    for row in table.get_children():
        table.delete(row)

    students = controller.search_student(keyword)

    if not students:
        messagebox.showinfo("Result", "No Student Found")
        return

    for student in students:
        table.insert(
            "", tk.END,
            values=(
                student[0],   # ID
                student[1],   # Name
                student[2],   # Father Name
                student[3],   # Gender
                student[4],   # Mobile
                student[7],   # Course
                student[8]    # Date
            )
        )


# ================= CLEAR SEARCH =================

def clear_search():
    search_entry.delete(0, tk.END)
    load_students()


# ================= SELECT ROW =================

def select_student(event):

    global selected_student_id

    selected = table.focus()
    data = table.item(selected)
    values = data["values"]

    if values:
        selected_student_id = values[0]

        name_entry.delete(0, tk.END)
        name_entry.insert(0, values[1])

        father_entry.delete(0, tk.END)
        father_entry.insert(0, values[2])

        gender_entry.delete(0, tk.END)
        gender_entry.insert(0, values[3])

        mobile_entry.delete(0, tk.END)
        mobile_entry.insert(0, values[4])

        course_entry.delete(0, tk.END)
        course_entry.insert(0, values[5])


# ================= DELETE STUDENT =================

def delete_student():

    selected = table.focus()
    data = table.item(selected)
    values = data["values"]

    if not values:
        messagebox.showwarning("Warning", "Please Select Student")
        return

    try:
        controller.delete_student(values[0])
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return

    messagebox.showinfo("Deleted", "Student Deleted Successfully")
    load_students()


# ================= UPDATE STUDENT =================

def update_student():

    global selected_student_id

    if selected_student_id is None:
        messagebox.showwarning("Warning", "Select Student First")
        return

    try:
        controller.update_student(
            selected_student_id,
            name_entry.get(),
            father_entry.get(),
            gender_entry.get(),
            mobile_entry.get(),
            email_entry.get(),
            address_entry.get(),
            course_entry.get(),
            date_entry.get()
        )
    except ValueError as e:
        messagebox.showwarning("Warning", str(e))
        return
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return

    messagebox.showinfo("Updated", "Student Updated Successfully")
    clear_fields()
    load_students()


# ================= MAIN WINDOW =================

root = tk.Tk()
root.title("Student Management")
root.geometry("900x700")

title = tk.Label(root, text="Student Registration", font=("Arial", 18, "bold"))
title.pack(pady=10)

# ----------- FORM ------------

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Father Name").pack()
father_entry = tk.Entry(root)
father_entry.pack()

tk.Label(root, text="Gender").pack()
gender_entry = tk.Entry(root)
gender_entry.pack()

tk.Label(root, text="Mobile").pack()
mobile_entry = tk.Entry(root)
mobile_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root)
address_entry.pack()

tk.Label(root, text="Course").pack()
course_entry = tk.Entry(root)
course_entry.pack()

tk.Label(root, text="Admission Date (YYYY-MM-DD)").pack()
date_entry = tk.Entry(root)
date_entry.pack()

# -------- BUTTONS --------

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

save_btn = tk.Button(button_frame, text="Save Student", command=save_student)
save_btn.grid(row=0, column=0, padx=5)

update_btn = tk.Button(button_frame, text="Update Student", command=update_student)
update_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(button_frame, text="Delete Student", command=delete_student)
delete_btn.grid(row=0, column=2, padx=5)

view_btn = tk.Button(button_frame, text="View Students", command=load_students)
view_btn.grid(row=0, column=3, padx=5)

# -------- SEARCH BAR --------

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

tk.Label(search_frame, text="Search Student").grid(row=0, column=0, padx=5)

search_entry = tk.Entry(search_frame, width=30)
search_entry.grid(row=0, column=1, padx=5)

search_btn = tk.Button(search_frame, text="Search", command=search_student)
search_btn.grid(row=0, column=2, padx=5)

clear_btn = tk.Button(search_frame, text="Clear", command=clear_search)
clear_btn.grid(row=0, column=3, padx=5)

# -------- TABLE --------

table = ttk.Treeview(
    root,
    columns=("ID", "Name", "Father", "Gender", "Mobile", "Course", "Date"),
    show="headings"
)

for col in table["columns"]:
    table.heading(col, text=col)

table.pack(fill="both", expand=True, pady=20)

table.bind("<ButtonRelease-1>", select_student)

load_students()

root.mainloop()
