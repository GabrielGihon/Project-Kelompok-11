import tkinter as tk
from tkinter import ttk

# Data contoh untuk tabel
data_tagihan = [
    ("2024-05-20", "Tagihan Listrik", 500000, "Belum Dibayar"),
    ("2024-05-22", "Tagihan Air", 150000, "Sudah Dibayar"),
    ("2024-05-25", "Tagihan Internet", 300000, "Belum Dibayar"),
    ("2024-06-01", "Tagihan Telepon", 100000, "Sudah Dibayar")
]

# Fungsi untuk mengubah status pembayaran
def ubah_status():
    selected_item = tree.selection()[0]
    current_status = tree.item(selected_item, "values")[3]
    new_status = "Sudah Dibayar" if current_status == "Belum Dibayar" else "Belum Dibayar"
    tree.item(selected_item, values=(tree.item(selected_item, "values")[0],
                                     tree.item(selected_item, "values")[1],
                                     tree.item(selected_item, "values")[2],
                                     new_status))

# Membuat jendela utama
root = tk.Tk()
root.title("Tabel Tagihan Jatuh Tempo")

# Membuat tabel menggunakan Treeview
tree = ttk.Treeview(root, columns=("Tanggal", "Nama", "Jumlah", "Status"), show="headings")
tree.heading("Tanggal", text="Tanggal")
tree.heading("Nama", text="Nama")
tree.heading("Jumlah", text="Jumlah")
tree.heading("Status", text="Status")

# Menambahkan data ke tabel
for item in data_tagihan:
    tree.insert("", tk.END, values=item)

tree.pack()

# Tombol untuk mengubah status pembayaran
button = tk.Button(root, text="Ubah Status Pembayaran", command=ubah_status)
button.pack()

# Menjalankan aplikasi
root.mainloop()
