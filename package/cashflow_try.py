import csv
import tkinter as tk
from tkinter import messagebox
import os

# Nama file CSV
EXPENSES_FILE = 'expenses.csv'
INCOME_FILE = 'income.csv'

# Fungsi untuk membuat file CSV dan menambahkan header jika belum ada
def initialize_csv(file_name, headers):
    if not os.path.exists(file_name):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)

# Fungsi untuk menambahkan pengeluaran
def add_expense():
    date = date_entry.get()
    category = expense_category_var.get()
    amount = amount_entry.get()
    description = description_entry.get()

    if not date or not category or not amount:
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid amount")
        return

    with open(EXPENSES_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    
    messagebox.showinfo("Success", "Expense added successfully")
    clear_entries()

# Fungsi untuk menambahkan pemasukan
def add_income():
    date = date_entry.get()
    category = income_category_var.get()
    amount = amount_entry.get()
    description = description_entry.get()

    if not date or not category or not amount:
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid amount")
        return

    with open(INCOME_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    
    messagebox.showinfo("Success", "Income added successfully")
    clear_entries()

# Fungsi untuk menghapus entri setelah menambahkan data
def clear_entries():
    date_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

# Fungsi untuk menghitung total pengeluaran
def calculate_total_expenses():
    total = 0.0
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                total += float(row[2])
    return total

# Fungsi untuk menghitung total pemasukan
def calculate_total_income():
    total = 0.0
    if os.path.exists(INCOME_FILE):
        with open(INCOME_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                total += float(row[2])
    return total

# Fungsi untuk menghitung sisa uang (saldo)
def calculate_balance():
    total_income = calculate_total_income()
    total_expenses = calculate_total_expenses()
    balance = total_income - total_expenses
    return balance

# Inisialisasi file CSV
initialize_csv(EXPENSES_FILE, ['Date', 'Category', 'Amount', 'Description'])
initialize_csv(INCOME_FILE, ['Date', 'Category', 'Amount', 'Description'])

# Membuat antarmuka pengguna
root = tk.Tk()
root.title("Financial Tracker")

# Frame untuk Pengeluaran
expense_frame = tk.LabelFrame(root, text="Add Expense", padx=10, pady=10)
expense_frame.grid(row=0, column=0, padx=10, pady=10)

tk.Label(expense_frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=5)
tk.Label(expense_frame, text="Category:").grid(row=1, column=0, padx=10, pady=5)
tk.Label(expense_frame, text="Amount:").grid(row=2, column=0, padx=10, pady=5)
tk.Label(expense_frame, text="Description:").grid(row=3, column=0, padx=10, pady=5)

date_entry = tk.Entry(expense_frame)
date_entry.grid(row=0, column=1, padx=10, pady=5)

expense_category_var = tk.StringVar(expense_frame)
expense_category_var.set("Makanan")  # default value
expense_category_options = ["Makanan", "Keperluan Rumah", "Transportasi", "Keperluan Komunikasi"]
expense_category_menu = tk.OptionMenu(expense_frame, expense_category_var, *expense_category_options)
expense_category_menu.grid(row=1, column=1, padx=10, pady=5)

amount_entry = tk.Entry(expense_frame)
amount_entry.grid(row=2, column=1, padx=10, pady=5)

description_entry = tk.Entry(expense_frame)
description_entry.grid(row=3, column=1, padx=10, pady=5)

add_expense_button = tk.Button(expense_frame, text="Add Expense", command=add_expense)
add_expense_button.grid(row=4, column=0, columnspan=2, pady=10)

# Frame untuk Pemasukan
income_frame = tk.LabelFrame(root, text="Add Income", padx=10, pady=10)
income_frame.grid(row=0, column=1, padx=10, pady=10)

tk.Label(income_frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=5)
tk.Label(income_frame, text="Category:").grid(row=1, column=0, padx=10, pady=5)
tk.Label(income_frame, text="Amount:").grid(row=2, column=0, padx=10, pady=5)
tk.Label(income_frame, text="Description:").grid(row=3, column=0, padx=10, pady=5)

income_category_var = tk.StringVar(income_frame)
income_category_var.set("Orang Tua")  # default value
income_category_options = ["Orang Tua", "Gaji", "Bonus"]
income_category_menu = tk.OptionMenu(income_frame, income_category_var, *income_category_options)
income_category_menu.grid(row=1, column=1, padx=10, pady=5)

amount_entry = tk.Entry(income_frame)
amount_entry.grid(row=2, column=1, padx=10, pady=5)

description_entry = tk.Entry(income_frame)
description_entry.grid(row=3, column=1, padx=10, pady=5)

add_income_button = tk.Button(income_frame, text="Add Income", command=add_income)
add_income_button.grid(row=4, column=0, columnspan=2, pady=10)

# Frame untuk Menampilkan Total
total_frame = tk.LabelFrame(root, text="Totals", padx=10, pady=10)
total_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

tk.Label(total_frame, text="Total Expenses:").grid(row=0, column=0, padx=10, pady=5)
total_expenses_label = tk.Label(total_frame, text="0.0")
total_expenses_label.grid(row=0, column=1, padx=10, pady=5)

tk.Label(total_frame, text="Total Income:").grid(row=1, column=0, padx=10, pady=5)
total_income_label = tk.Label(total_frame, text="0.0")
total_income_label.grid(row=1, column=1, padx=10, pady=5)

tk.Label(total_frame, text="Balance:").grid(row=2, column=0, padx=10, pady=5)
balance_label = tk.Label(total_frame, text="0.0")
balance_label.grid(row=2, column=1, padx=10, pady=5)

def update_totals():
    total_expenses_label.config(text=str(calculate_total_expenses()))
    total_income_label.config(text=str(calculate_total_income()))
    balance_label.config(text=str(calculate_balance()))

update_totals_button = tk.Button(total_frame, text="Update Totals", command=update_totals)
update_totals_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()