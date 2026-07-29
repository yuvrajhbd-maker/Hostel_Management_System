# 🏨 Hostel Management System

A desktop-based **Hostel Management System** developed using **Python Tkinter** and **MySQL**.
This application helps hostel administrators manage students, rooms, room allocation, fee collection, and reports efficiently.

---

## 📌 Project Overview

The Hostel Management System is designed to automate daily hostel operations.
It provides an easy-to-use graphical interface for managing student records, room details, allocations, and fee payments.

The project follows an **MVC (Model-View-Controller)** structure:

- **Model** (`models/`) — plain data classes (Student, Room, Allocation, Fee)
- **View** (`view/`) — Tkinter GUI screens; contain layout/widgets only
- **Controller** (`controllers/`) — validation and business logic; the only layer views are allowed to call
- **DAO** (`dao/`) — raw SQL / data access, called only by controllers

---

## 🚀 Features

### 🔐 Admin Login
- Admin login system (against the `admin` table in MySQL)
- Professional login interface

---

### 👨‍🎓 Student Management
- Add new students
- View all students
- Update student details
- Delete student records
- Search students by name/mobile

Student details include: Name, Father Name, Gender, Mobile, Email, Address, Course, Admission Date.

---

### 🏠 Room Management
- Add hostel rooms
- View all rooms
- Search / delete rooms
- Track capacity, occupancy, and status

---

### 🛏️ Room Allocation
- Assign rooms to students
- Automatically updates room occupancy/status
- View all allocations

---

### 💰 Fee Collection
- Add student fee records (auto-calculates due amount)
- View all fee records
- Delete fee records

---

### 📊 Dashboard
Shows Total Students, Total Rooms, Available Rooms, Total Fee Collection, and Due Fee, and links to every module (Student Management, Room Management, Room Allocation, Fee Collection, Reports).

---

### 📄 Reports
Generate and export (Excel/PDF) reports for Students, Rooms, and Fees.

---

## 🛠️ Technologies Used

- **Frontend:** Python Tkinter
- **Backend:** Python
- **Database:** MySQL
- **Libraries:** mysql-connector-python, openpyxl, reportlab

---

## 📂 Project Structure

```
Hostel_Management_System/
│
├── main.py                     # entry point (python main.py)
├── database.py                 # single DB connection helper (env-var driven)
├── requirements.txt
├── hostel_db.sql                # schema + seed data to import into MySQL
│
├── view/                        # GUI screens (Tkinter) — layout only
│   ├── login.py
│   ├── dashboard.py
│   ├── student_gui.py
│   ├── room_gui.py
│   ├── allocation_gui.py
│   ├── fee_gui.py
│   └── report_gui.py
│
├── controllers/                 # business logic / validation
│   ├── auth_controller.py
│   ├── student_controller.py
│   ├── room_controller.py
│   ├── allocation_controller.py
│   ├── fee_controller.py
│   ├── report_controller.py
│   └── dashboard_controller.py
│
├── dao/                          # raw data access (SQL only)
│   ├── studentdao.py
│   ├── roomdao.py
│   ├── allocationdao.py
│   ├── feedao.py
│   ├── reportdao.py
│   └── dashboarddao.py
│
├── models/                       # plain data classes
│   ├── student.py
│   ├── room.py
│   ├── allocation.py
│   └── fee.py
│
├── utils/
│   └── export.py                 # Excel/PDF export helpers
│
└── reports/                       # generated Excel/PDF reports land here
```

---

## ⚙️ Installation & Setup

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Database Setup

1. Open MySQL and create the database:

```sql
CREATE DATABASE hostel_db;
```

2. Import the schema and seed data:

```
mysql -u root -p hostel_db < hostel_db.sql
```

### 3. Configure the database connection

`database.py` reads credentials from environment variables (with local-dev
defaults as a fallback), so no password needs to be hardcoded in source:

```
export HOSTEL_DB_HOST=localhost
export HOSTEL_DB_USER=root
export HOSTEL_DB_PASSWORD=your_password
export HOSTEL_DB_NAME=hostel_db
```

On Windows (PowerShell):

```
$env:HOSTEL_DB_HOST="localhost"
$env:HOSTEL_DB_USER="root"
$env:HOSTEL_DB_PASSWORD="your_password"
$env:HOSTEL_DB_NAME="hostel_db"
```

### 4. Run the project

```
python main.py
```

This opens the login screen, which then launches the dashboard and other
modules as separate windows.

---

## 🎯 Future Enhancements

- Attendance Management
- Visitor Management
- Complaint Management
- Email Notifications
- Role Based Access
- Online Fee Payment
- Password hashing for admin login (currently plaintext, matching the seed data in `hostel_db.sql`)

---

## 👨‍💻 Developer

**Yuvraj Singh Tanwar**

Python Developer | Data Analyst

---

## ⭐ Project Status

Completed ✅
