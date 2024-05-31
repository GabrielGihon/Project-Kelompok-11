import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import csv
import package.login
import pandas as pd
from tkinter import filedialog

def dashboard(username):
    root = tk.Tk()
    root.geometry('1200x675')
    root.title('DASHBOARD')
    root.resizable(False, False)
    
    def dashboard_page():
        def update_data():
            filename1 = f"database/{username}/pemasukan.csv"
            filename2 = f"database/{username}/pengeluaran.csv"

            data = pd.read_csv(filename1)
            total1 = data['jumlah'].sum()
            lb_2.config(text=f"Pemasukan \n\n{total1}")
            
            data = pd.read_csv(filename2)
            total2 = data['jumlah'].sum()
            lb_3.config(text=f"Pengeluaran \n\n{total2}")
            
            total_uang = total1 - total2
            lb_1.config(text=f"Total Saldo \n\n{total_uang}")
        
        home_frame = tk.Frame(main_frame, bg = 'White')
        
        frame_atas = tk.Frame(main_frame, width=975, height=60, bg='#e8f0fa')
        frame_atas.place(x=10, y=10)
        
        lb_utama = tk.Label(main_frame, text=f'Selamat Datang, {username}', font=('Poppins', 20), fg='Black', bg='#e8f0fa')
        lb_utama.place(x=60, y=20)
        
        lb_utama = tk.Label(main_frame, text='Dashboard ', font=('Poppins', 20), fg='Black', bg='White')
        lb_utama.place(x=30, y=100)
        
        frame_totalsaldo = tk.Frame(main_frame, width=250, height=130, bg='#e8f0fa')
        frame_totalsaldo.place(x=100, y=150)
        
        ttl_indicate = tk.Label(frame_totalsaldo, text='', bg='blue', height=10)
        ttl_indicate.place(x=0, y=0)

        saldo_image = tk.PhotoImage(file='assets/ttldn.png')
        logo_saldo = tk.Label(frame_totalsaldo, image=saldo_image, border=0, bg="#e8f0fa")
        logo_saldo.image = saldo_image 
        logo_saldo.place(x=14, y=30)

        lb_1 = tk.Label(frame_totalsaldo, text='Total Saldo  \n\n0', font='Poppins', bg='#e8f0fa', fg='Black')
        lb_1.place(x=100, y=20)
        
        frame_pemasukan = tk.Frame(main_frame, width=250, height=130, bg='#e8f0fa')
        frame_pemasukan.place(x=400, y=150)

        
        lb_2 = tk.Label(frame_pemasukan, text="Pemasukan \n\n0", font='Poppins', bg='#e8f0fa', fg='Black')
        lb_2.place(x=100, y=20)
        
        msk_indicate = tk.Label(frame_pemasukan, text='', bg='#03fc7b', height=10)
        msk_indicate.place(x=0, y=0)

        pemasukan_image = tk.PhotoImage(file='assets/up2.png')
        logo_masuk = tk.Label(frame_pemasukan, image=pemasukan_image, border=0, bg="#e8f0fa")
        logo_masuk.image = pemasukan_image 
        logo_masuk.place(x=14, y=30)

        frame_pengeluaran = tk.Frame(main_frame, width=250, height=130, bg='#e8f0fa')
        frame_pengeluaran.place(x=700, y=150)

        
        lb_3 = tk.Label(frame_pengeluaran, text='Pengeluaran \n\n0', font='Poppins', bg='#e8f0fa', fg='Black')
        lb_3.place(x=100, y=20)
        
        pengeluaran_lb = tk.Label(home_frame, text='Dashboard', font=('Bold', 34))
        pengeluaran_lb.place(x=10, y=80)

        lr_indicate = tk.Label(frame_pengeluaran, text='', bg='#fa2f69', height=10)
        lr_indicate.place(x=0, y=0)

        pengeluaran_image = tk.PhotoImage(file='assets/loss2.png')
        logo_keluar = tk.Label(frame_pengeluaran, image=pengeluaran_image, border=0, bg="#e8f0fa")
        logo_keluar.image = pengeluaran_image 
        logo_keluar.place(x=14, y=30)
        
        frame_bawah = tk.Frame(main_frame, width=975, height=300, bg='#e8f0fa')
        frame_bawah.place(x=10, y=350)

    
        
       
            
    
        button_image_1 = PhotoImage(file='assets/updt.png')
        logo_update = tk.Label(frame_totalsaldo, image=saldo_image )
        logo_update.image = button_image_1
        button_1 = Button(
            root , border=0, bg="white",
            image=button_image_1, command=update_data
        )
        button_1.place(x=1100, y=80)

        

        home_frame.pack(pady=100)
        
    def pemasukan_page():
        def simpan_pemasukan():
            global filename
            
            date_value = date_entry.get()
            description_value = description_entry.get()
            purpose_value = purpose_combobox.get()
            amount_value = amount_entry.get()
            
            filename = f"database/{username}/pemasukan.csv"
            
            with open(filename, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([date_value, description_value, purpose_value, amount_value])
            
            messagebox.showinfo("Success", "Data saved successfully!")
            
            date_entry.delete(0, tk.END)
            description_entry.delete(0, tk.END)
            purpose_combobox.set('')
            amount_entry.delete(0, tk.END)
            total_pemasukan()
            
        def total_pemasukan():
            try:
                data = pd.read_csv(filename)
                total = data['jumlah'].sum()
                lb_utama1.config(text=f"Total Pemasukan : {total}")
            except FileNotFoundError:
                lb_utama1.config(text="Total Pemasukan : 0")
            except KeyError:
                lb_utama1.config(text="Total Pemasukan : 0")
        
        frame_atas = tk.Frame(main_frame, width=975, height=60, bg='#e8f0fa')
        frame_atas.place(x=10, y=10)

        ttl_indicate = tk.Label(frame_atas, text='', bg='green', height=60)
        ttl_indicate.place(x=0, y=0)

        frame_bawah = tk.Frame(main_frame, width=975, height=500, bg='#e8f0fa')
        frame_bawah.place(x=10, y=150)
        
        lb_3 = tk.Label(frame_bawah, text='Pemasukan', font=('Poppins',20), fg='Black', bg='#e8f0fa')
        lb_3.place(x=65, y=20)
        
        lb_utama1 = tk.Label(main_frame, text="Total Pemasukan : 0", font=('Poppins', 20), fg='Black', bg='#e8f0fa')
        lb_utama1.place(x=60, y=20)
        
        tk.Label(frame_bawah, text="Masukkan Tanggal Pemasukan:", bg='#e8f0fa').place(x=65, y=80)
        date_entry = DateEntry(frame_bawah, date_pattern='dd/MM/yyyy')
        date_entry.place(x=250, y=80)
        
        tk.Label(frame_bawah, text="Masukkan Keterangan Pemasukan:", bg='#e8f0fa').place(x=65, y=120)
        description_entry = tk.Entry(frame_bawah)
        description_entry.place(x=250, y=120)
        
        tk.Label(frame_bawah, text="Masukkan Sumber Pemasukan:", bg='#e8f0fa').place(x=65, y=160)
        purpose_combobox = ttk.Combobox(frame_bawah, values=["Gaji", "Investasi", "Part time", "Lainnya"])
        purpose_combobox.place(x=250, y=160)
        purpose_combobox.current(0)
        
        tk.Label(frame_bawah, text="Masukkan Jumlah Pemasukan:", bg='#e8f0fa').place(x=65, y=200)
        amount_entry = tk.Entry(frame_bawah)
        amount_entry.place(x=250, y=200)
        
        save_btn = tk.Button(frame_bawah, text='Save', font=('Bold', 15), fg='#158aff', bd=0, bg='White', command=simpan_pemasukan)
        save_btn.place(x=200, y=250)
        
    def pengeluaran_page():
        global simpan_pengeluaran, total_pengeluaran
        
        def simpan_pengeluaran():
            global filename
            
            date_value = date_entry.get()
            description_value = description_entry.get()
            purpose_value = purpose_combobox.get()
            amount_value = amount_entry.get()
            
            filename = f"database/{username}/pengeluaran.csv"
            
            with open(filename, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([date_value, description_value, purpose_value, amount_value])
            
            messagebox.showinfo("Success", "Data saved successfully!")
            
            date_entry.delete(0, tk.END)
            description_entry.delete(0, tk.END)
            purpose_combobox.set('')
            amount_entry.delete(0, tk.END)
            total_pengeluaran()
        
        def total_pengeluaran():
            try:
                data = pd.read_csv(filename)
                total = data['jumlah'].sum()
                lb_utama1.config(text=f"Total Pengeluaran: {total}")
            except FileNotFoundError:
                lb_utama1.config(text="Total Pengeluaran: 0")
            except KeyError:
                lb_utama1.config(text="Total Pengeluaran: 0")
        
        frame_atas = tk.Frame(main_frame, width=975, height=40, bg='#e8f0fa')
        lb_utama = tk.Label(main_frame, text='Pengeluaran', font=('Poppins', 20), fg='Black', bg='White')
        lb_utama.place(x=30, y=100)

        frame_atas = tk.Frame(main_frame, width=975, height=60, bg='#e8f0fa')
        frame_atas.place(x=10, y=10)

        ttl_indicate = tk.Label(frame_atas, text='', bg='red', height=60)
        ttl_indicate.place(x=0, y=0)

        frame_bawah = tk.Frame(main_frame, width=975, height=500, bg='#e8f0fa')
        frame_bawah.place(x=10, y=150)

        lb_3 = tk.Label(frame_bawah, text='ISI', font=('Poppins', 20), fg='Black', bg='#e8f0fa')
        lb_3.place(x=65, y=20)

        lb_utama1 = tk.Label(main_frame, text="Total Pengeluaran: 0", font=('Poppins', 20), fg='Black', bg='#e8f0fa')
        lb_utama1.place(x=60, y=20)
        
        tk.Label(frame_bawah, text="Masukkan Tanggal Pengeluaran:", bg='#e8f0fa').place(x=65, y=80)
        date_entry = DateEntry(frame_bawah, date_pattern='dd/MM/yyyy')
        date_entry.place(x=250, y=80)

        tk.Label(frame_bawah, text="Masukkan Keterangan Pengeluaran:", bg='#e8f0fa').place(x=65, y=120)
        description_entry = tk.Entry(frame_bawah)
        description_entry.place(x=250, y=120)

        tk.Label(frame_bawah, text="Masukkan Keperluan Pengeluaran:", bg='#e8f0fa').place(x=65, y=160)
        purpose_combobox = ttk.Combobox(frame_bawah, values=["Makan dan Minum", "Transportasi", "Belanja", "Lainnya"])
        purpose_combobox.place(x=250, y=160)
        purpose_combobox.current(0)

        tk.Label(frame_bawah, text="Masukkan Jumlah Pengeluaran:", bg='#e8f0fa').place(x=65, y=200)
        amount_entry = tk.Entry(frame_bawah)
        amount_entry.place(x=250, y=200)
        
        save_btn = tk.Button(frame_bawah, text='Save', font=('Bold', 15), fg='#158aff', bd=0, bg='White', command=simpan_pengeluaran)
        save_btn.place(x=200, y=250)

    def tagihan_page():
        def simpan_tagihan():
            global filename
            
            date_value = date_entry.get()
            description_value = description_entry.get()
            purpose_value = purpose_combobox.get()
            amount_value = amount_entry.get()
            
            filename = f"database/{username}/tagihan.csv"
            
            with open(filename, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([date_value, description_value, purpose_value, amount_value])
            
            messagebox.showinfo("Success", "Data saved successfully!")
            
            date_entry.delete(0, tk.END)
            description_entry.delete(0, tk.END)
            purpose_combobox.set('')
            amount_entry.delete(0, tk.END)
            
        tagihan_frame = tk.Frame(main_frame, bg='White')

        lb_utama = tk.Label(main_frame, text='Selamat Datang, ', font=('Poppins', 20), fg='Black', bg='#e8f0fa')
        lb_utama.place(x=60, y=20)

        lb_utama = tk.Label(main_frame, text='Tagihan ', font=('Poppins', 20), fg='Black', bg='White')
        lb_utama.place(x=30, y=100)

        frame_atas = tk.Frame(main_frame, width=975, height=60, bg='#e8f0fa')
        frame_atas.place(x=10, y=10)

        frame_bawah = tk.Frame(main_frame, width=975, height=500, bg='#e8f0fa')
        frame_bawah.place(x=10, y=150)

        lb_3 = tk.Label(frame_bawah, text='ISI', font=('Poppins', 20), fg='Black', bg='#e8f0fa')
        lb_3.place(x=65, y=20)

        lb_utama1 = tk.Label(main_frame, text="Total Tagihan: 0", font=('Poppins', 20), fg='Black', bg='#e8f0fa')
        lb_utama1.place(x=60, y=20)
        
        tk.Label(frame_bawah, text="Masukkan Tanggal Tagihan:", bg='#e8f0fa').place(x=65, y=80)
        date_entry = DateEntry(frame_bawah, date_pattern='dd/MM/yyyy')
        date_entry.place(x=250, y=80)

        tk.Label(frame_bawah, text="Masukkan Keterangan Tagihan:", bg='#e8f0fa').place(x=65, y=120)
        description_entry = tk.Entry(frame_bawah)
        description_entry.place(x=250, y=120)

        tk.Label(frame_bawah, text="Masukkan Keperluan Tagihan:", bg='#e8f0fa').place(x=65, y=160)
        purpose_combobox = ttk.Combobox(frame_bawah, values=["Makan dan Minum", "Transportasi", "Belanja", "Lainnya"])
        purpose_combobox.place(x=250, y=160)
        purpose_combobox.current(0)

        tk.Label(frame_bawah, text="Masukkan Jumlah Tagihan:", bg='#e8f0fa').place(x=65, y=200)
        amount_entry = tk.Entry(frame_bawah)
        amount_entry.place(x=250, y=200)

        save_btn = tk.Button(frame_bawah, text='Save', font=('Bold', 15), fg='#158aff', bd=0, bg='White', command=simpan_tagihan)
        save_btn.place(x=200, y=250)

        tagihan_frame.pack(pady=20)

    def laporan_page():
        pemasukan_filename = f"database/{username}/pemasukan.csv"
        pengeluaran_filename = f"database/{username}/pengeluaran.csv"
        
        try:
            pemasukan_data = pd.read_csv(pemasukan_filename)
            pengeluaran_data = pd.read_csv(pengeluaran_filename)
        except FileNotFoundError:
            messagebox.showinfo("Error", "File pemasukan/pengeluaran tidak ditemukan.")
            return
        
        laporan_frame = tk.Frame(main_frame, bg='White')
        laporan_frame.pack(fill="both", expand=True)
        
        lb_utama = tk.Label(laporan_frame, text=f'Selamat Datang, {username}', font=('Poppins', 20), fg='Black', bg='#e8f0fa')
        lb_utama.place(x=60, y=20)

        lb_laporan = tk.Label(laporan_frame, text='Laporan', font=('Poppins', 20), fg='Black', bg='White')
        lb_laporan.pack(pady=10)

        frame_atas = tk.Frame(laporan_frame, bg='#e8f0fa')
        frame_atas.pack(fill='x', padx=10, pady=10)

        frame_bawah = tk.Frame(laporan_frame, bg='#e8f0fa')
        frame_bawah.pack(fill="both", expand=True, padx=10, pady=10)
        
        def display_csv_data(dataframe):
            tree.delete(*tree.get_children())  # Clear the current data

            tree["columns"] = list(dataframe.columns)
            tree["show"] = "headings"
            
            for col in dataframe.columns:
                tree.heading(col, text=col)
                tree.column(col, width=100)
            
            for index, row in dataframe.iterrows():
                tree.insert("", "end", values=list(row))

            status_label.config(text="data loaded")

        def open_pemasukan():
            display_csv_data(pemasukan_data)

        def open_pengeluaran():
            display_csv_data(pengeluaran_data)
        
        open_pemasukan_button = tk.Button(frame_atas, text="Open Pemasukan CSV", command=open_pemasukan)
        open_pemasukan_button.pack(side=tk.LEFT, padx=20, pady=10)
        
        open_pengeluaran_button = tk.Button(frame_atas, text="Open Pengeluaran CSV", command=open_pengeluaran)
        open_pengeluaran_button.pack(side=tk.LEFT, padx=20, pady=10)
        
        tree = ttk.Treeview(frame_bawah, show="headings")
        tree.pack(padx=20, pady=20, fill="both", expand=True)
        
        status_label = tk.Label(frame_bawah, text="", padx=20, pady=10, bg='#e8f0fa')
        status_label.pack()
    
    def hide_indicators():
        home_indicate.config(bg='#e8f0fa')
        pemasukan_indicate.config(bg='#e8f0fa')
        pengeluaran_indicate.config(bg='#e8f0fa')
        tagihan_indicate.config(bg='#e8f0fa')
        laporan_indicate.config(bg='#e8f0fa')

    def delete_pages():
        for frame in main_frame.winfo_children():
            frame.destroy()

    def indicate(lb, page):
        hide_indicators()
        lb.config(bg='#158aff')
        delete_pages()
        page()

    options_frame = tk.Frame(root, bg='#e8f0fa')

    img = PhotoImage(file="assets/LogoKecil.png")
    Label(options_frame, image=img, border=0, bg="#e8f0fa").place(x=20, y=0)

    img2 = PhotoImage(file="assets/TextAja.png")
    Label(options_frame, image=img2, border=0, bg="#e8f0fa").place(x=90, y=10)

    
    button_y = 120
    indicate_y = 125

    home_btn = tk.Button(options_frame, text='Dashboard', font=('century gothic', 15), fg='#0097B2', bd=0, bg='#e8f0fa', command=lambda: indicate(home_indicate, dashboard_page))
    home_btn.place(x=60, y=button_y +3 )

    home_icon = tk.PhotoImage(file="assets/dashboard.png")
    Label(options_frame, image=home_icon, border=0, bg="#e8f0fa").place(x=25, y=button_y + 8)

    home_indicate = tk.Label(options_frame, text='', bg='#e8f0fa', height=2)
    home_indicate.place(x=5, y=indicate_y)
    
    pemasukan_btn = tk.Button(options_frame, text='Pemasukan', font=('century gothic', 15), fg='#0097B2', bd=0, bg='#e8f0fa', command=lambda: indicate(pemasukan_indicate, pemasukan_page))
    pemasukan_btn.place(x=60, y=button_y + 40)

    pemasukan_icon = tk.PhotoImage(file="assets/profit.png")
    Label(options_frame, image=pemasukan_icon, border=0, bg="#e8f0fa").place(x=25, y=button_y + 48)

    pemasukan_indicate = tk.Label(options_frame, text='', bg='#e8f0fa', height=2)
    pemasukan_indicate.place(x=5, y=indicate_y + 40)

    pengeluaran_btn = tk.Button(options_frame, text='Pengeluaran', font=('century gothic', 15), fg='#0097B2', bd=0, bg='#e8f0fa', command=lambda: indicate(pengeluaran_indicate, pengeluaran_page))
    pengeluaran_btn.place(x=60, y=button_y + 80)

    pengeluaran_icon = tk.PhotoImage(file="assets/donation.png")
    Label(options_frame, image=pengeluaran_icon, border=0, bg="#e8f0fa").place(x=25, y=button_y + 88)

    pengeluaran_indicate = tk.Label(options_frame, text='', bg='#e8f0fa',height=2)
    pengeluaran_indicate.place(x=5, y=indicate_y + 80)

    tagihan_btn = tk.Button(options_frame, text='Tagihan', font=('century gothic', 15), fg='#0097B2', bd=0, bg='#e8f0fa', command=lambda: indicate(tagihan_indicate, tagihan_page))
    tagihan_btn.place(x=60, y=button_y + 120)

    tagihan_icon = tk.PhotoImage(file="assets/bill.png")
    Label(options_frame, image=tagihan_icon, border=0, bg="#e8f0fa").place(x=25, y=button_y + 128)

    tagihan_indicate = tk.Label(options_frame, text='', bg='#e8f0fa',height=2)
    tagihan_indicate.place(x=5, y=indicate_y + 120)

    laporan_btn = tk.Button(options_frame, text='Laporan', font=('century gothic', 15), fg='#0097B2', bd=0, bg='#e8f0fa', command=lambda: indicate(laporan_indicate, laporan_page))
    laporan_btn.place(x=60, y=button_y + 160)

    laporan_icon = tk.PhotoImage(file="assets/prescription.png")
    Label(options_frame, image=laporan_icon, border=0, bg="#e8f0fa").place(x=25, y=button_y + 168)

    laporan_indicate = tk.Label(options_frame, text='', bg='#e8f0fa',height=2)
    laporan_indicate.place(x=5, y=indicate_y + 160)

    logout_btn = tk.Button(options_frame, text='Logout', font=('century gothic', 15), fg='#0097B2', bd=0, bg='#e8f0fa', command=lambda: indicate(laporan_indicate, laporan_page))
    laporan_btn.place(x=60, y=button_y + 160)

    logout_icon = tk.PhotoImage(file="assets/prescription.png")
    Label(options_frame, image=laporan_icon, border=0, bg="#e8f0fa").place(x=25, y=button_y + 208)

    options_frame.pack(side=tk.LEFT)
    options_frame.pack_propagate(False)
    options_frame.configure(width=200, height=675)

    main_frame = tk.Frame(root, bg='white')
    main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    indicate(home_indicate, dashboard_page)

    
    root.mainloop()

def main_program():
    global username
    package.login.halaman_login()
    username = package.login.username

if __name__ == "__main__":
    main_program()