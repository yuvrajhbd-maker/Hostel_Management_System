import tkinter as tk
from tkinter import ttk, messagebox

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from controllers.report_controller import ReportController


controller = ReportController()

REPORTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

current_data = []
current_headers = []


# ================= TABLE HEADING =================

def set_heading():
    for col in table["columns"]:
        table.heading(col, text=col)


# ================= CLEAR TABLE =================

def clear_table():
    for row in table.get_children():
        table.delete(row)


def _render_report(headers, data):
    global current_data, current_headers

    clear_table()

    current_headers = headers
    current_data = data

    table["columns"] = tuple(headers)
    set_heading()

    for row in data:
        table.insert("", tk.END, values=row)


# ================= LOAD STUDENT REPORT =================

def student_report():
    headers, data = controller.student_report()
    _render_report(headers, data)


# ================= LOAD ROOM REPORT =================

def room_report():
    headers, data = controller.room_report()
    _render_report(headers, data)


# ================= LOAD FEE REPORT =================

def fee_report():
    headers, data = controller.fee_report()
    _render_report(headers, data)


# ================= EXPORT EXCEL =================

def export_excel_file():
    try:
        controller.export_excel(
            os.path.join(REPORTS_DIR, "report.xlsx"),
            current_headers,
            current_data
        )
    except ValueError as e:
        messagebox.showwarning("Warning", str(e))
        return
    except Exception as e:
        messagebox.showerror("Export Error", str(e))
        return

    messagebox.showinfo("Success", "Excel Exported Successfully")


# ================= EXPORT PDF =================

def export_pdf_file():
    try:
        controller.export_pdf(
            os.path.join(REPORTS_DIR, "report.pdf"),
            current_headers,
            current_data
        )
    except ValueError as e:
        messagebox.showwarning("Warning", str(e))
        return
    except Exception as e:
        messagebox.showerror("Export Error", str(e))
        return

    messagebox.showinfo("Success", "PDF Exported Successfully")


# ================= WINDOW =================

root = tk.Tk()
root.title("Hostel Management Reports")
root.geometry("900x600")

title = tk.Label(root, text="Reports Dashboard", font=("Arial", 22, "bold"))
title.pack(pady=20)

# ================= BUTTONS =================

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Student Report", width=20, command=student_report).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Room Report", width=20, command=room_report).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Fee Report", width=20, command=fee_report).grid(row=0, column=2, padx=10)

tk.Button(btn_frame, text="Export Excel", width=20, command=export_excel_file).grid(row=1, column=0, padx=10, pady=10)
tk.Button(btn_frame, text="Export PDF", width=20, command=export_pdf_file).grid(row=1, column=1, padx=10, pady=10)

# ================= TABLE =================

table = ttk.Treeview(root, show="headings")
table.pack(fill="both", expand=True, pady=20)

root.mainloop()
