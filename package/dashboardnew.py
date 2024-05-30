import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry

def dashboard():
    root = tk.Tk()
    root.geometry('1200x675')
    root.title('DASHBOARD')
    root.resizable(False, False)

    def dashboard_page():
        home_frame = tk.Frame(main_frame, bg = 'White')

        img2 = PhotoImage(file="assets/wl.png")
        Label(home_frame, image=img2, border=0, ).place(x=0, y=300)
        
        frame_atas = tk.Frame(main_frame, width=975, height=60, bg='#e8f0fa')
        frame_atas.place(x=10, y=10)

        lb_utama = tk.Label(main_frame, text='Selamat Datang, ', font=('Poppins', 20), fg='Black', bg='#e8f0fa')
        lb_utama.place(x=60, y=20)

        lb_utama = tk.Label(main_frame, text='Dashboard ', font=('Poppins', 20), fg='Black', bg='White')
        lb_utama.place(x=30, y=100)


        frame_totalsaldo = tk.Frame(main_frame, width=250, height=130, bg='#e8f0fa')
        frame_totalsaldo.place(x=100, y=150)

        ttl_indicate = tk.Label(frame_totalsaldo, text='', bg='blue', height=10)
        ttl_indicate.place(x=0, y=0)

        lb_1 = tk.Label(frame_totalsaldo, text='Total Saldo', font='Poppins', bg='#e8f0fa', fg='#0097B2')
        lb_1.place(x=100, y=20)


        frame_pemasukan = tk.Frame(main_frame, width=250, height=130, bg='#e8f0fa')
        frame_pemasukan.place(x=400, y=150)


        msk_indicate = tk.Label(frame_pemasukan, text='', bg='green', height=10)
        msk_indicate.place(x=0, y=0)

        lb_2 = tk.Label(frame_pemasukan, text='Pemasukan', font='Poppins', bg='#e8f0fa', fg='#0097B2')
        lb_2.place(x=100, y=20)

        frame_pengeluaran = tk.Frame(main_frame, width=250, height=130, bg='#e8f0fa')
        frame_pengeluaran.place(x=700, y=150)

        lr_indicate = tk.Label(frame_pengeluaran, text='', bg='red', height=10)
        lr_indicate.place(x=0, y=0)

        lb_3 = tk.Label(frame_pengeluaran, text='Pengeluaran', font='Poppins', bg='#e8f0fa', fg='#0097B2')
        lb_3.place(x=100, y=20)


        pengeluaran_lb = tk.Label(home_frame, text='Dashboard', font=('Bold', 34))
        pengeluaran_lb.place(x=10, y=80)

        frame_bawah = tk.Frame(main_frame, width=975, height=300, bg='#e8f0fa')
        frame_bawah.place(x=10, y=350)


        home_frame.pack(pady=100)

    def pemasukan_page():
        lb_utama = tk.Label(main_frame, text='Pemasukan', font=('Poppins', 20), fg='Black', bg='White')
        lb_utama.place(x=30, y=100)

        frame_atas = tk.Frame(main_frame, width=975, height=60, bg='#e8f0fa')
        frame_atas.place(x=10, y=10)

        frame_bawah = tk.Frame(main_frame, width=975, height=500, bg='#e8f0fa')
        frame_bawah.place(x=10, y=150)

        lb_3 = tk.Label(frame_bawah, text='ISI', font=('Poppins', 20), fg='Black', bg='#e8f0fa')
        lb_3.place(x=65, y=20)

        lb_utama1 = tk.Label(main_frame, text='Total Pemasukan : ', font=('Poppins', 20), fg='Black', bg='#e8f0fa')
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
        
        save_btn = tk.Button(frame_bawah, text='Save', font=('Bold', 15), fg='#158aff', bd=0, bg='White')
        save_btn.place(x=200, y=250)

    def pengeluaran_page():
        lb_utama = tk.Label(main_frame, text='Pengeluaran', font=('Poppins', 20), fg='Black', bg='White')
        lb_utama.place(x=30, y=100)

        frame_atas = tk.Frame(main_frame, width=975, height=60, bg='#e8f0fa')
        frame_atas.place(x=10, y=10)

        frame_bawah = tk.Frame(main_frame, width=975, height=500, bg='#e8f0fa')
        frame_bawah.place(x=10, y=150)

        lb_utama1 = tk.Label(main_frame, text='Total Pengeluaran :', font=('Poppins', 20), fg='Black', bg='#e8f0fa')
        lb_utama1.place(x=60, y=20)

        lb_3 = tk.Label(frame_bawah, text='Isi', font=('Poppins', 20), fg='Black', bg='#e8f0fa')
        lb_3.place(x=65, y=20)

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

        save_btn = tk.Button(frame_bawah, text='Save', font=('Bold', 15), fg='#158aff', bd=0, bg='White')
        save_btn.place(x=200, y=250)

    def tagihan_page():
        tagihan_frame = tk.Frame(main_frame, bg='White')

        lb_utama = tk.Label(main_frame, text='Selamat Datang, ', font=('Poppins', 20), fg='Black', bg='#e8f0fa')
        lb_utama.place(x=60, y=20)

        lb_utama = tk.Label(main_frame, text='Tagihan ', font=('Poppins', 20), fg='Black', bg='White')
        lb_utama.place(x=30, y=100)

        frame_atas = tk.Frame(main_frame, width=975, height=60, bg='#e8f0fa')
        frame_atas.place(x=10, y=10)

        frame_bawah = tk.Frame(main_frame, width=975, height=500, bg='#e8f0fa')
        frame_bawah.place(x=10, y=150)

        tagihan_frame.pack(pady=20)

    def laporan_page():
        laporan_frame = tk.Frame(main_frame,bg='White')

        lb_utama = tk.Label(main_frame, text='Selamat Datang, ', font=('Poppins', 20), fg='Black', bg='#e8f0fa')
        lb_utama.place(x=60, y=20)

        lb_utama = tk.Label(main_frame, text='Laporan ', font=('Poppins', 20), fg='Black', bg='White')
        lb_utama.place(x=30, y=100)

        frame_atas = tk.Frame(main_frame, width=975, height=60, bg='#e8f0fa')
        frame_atas.place(x=10, y=10)

        frame_bawah = tk.Frame(main_frame, width=975, height=500, bg='#e8f0fa')
        frame_bawah.place(x=10, y=150)

        laporan_frame.pack(pady=20)

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
    Label(options_frame, image=img, border=0, bg="#e8f0fa").place(x=10, y=0)

    img2 = PhotoImage(file="assets/TextAja.png")
    Label(options_frame, image=img2, border=0, bg="#e8f0fa").place(x=90, y=20)

    
    button_y = 120
    indicate_y = 125

    home_btn = tk.Button(options_frame, text='Dashboard', font=('Poppins', 15), fg='#0097B2', bd=0, bg='#e8f0fa', command=lambda: indicate(home_indicate, dashboard_page))
    home_btn.place(x=60, y=button_y +3 )

    home_icon = tk.PhotoImage(file="assets/dashboard.png")
    Label(options_frame, image=home_icon, border=0, bg="#e8f0fa").place(x=25, y=button_y + 8)

    home_indicate = tk.Label(options_frame, text='', bg='#e8f0fa', height=2)
    home_indicate.place(x=5, y=indicate_y)
    
    pemasukan_btn = tk.Button(options_frame, text='Pemasukan', font=('Bold', 15), fg='#0097B2', bd=0, bg='#e8f0fa', command=lambda: indicate(pemasukan_indicate, pemasukan_page))
    pemasukan_btn.place(x=60, y=button_y + 40)

    pemasukan_icon = tk.PhotoImage(file="assets/profit.png")
    Label(options_frame, image=pemasukan_icon, border=0, bg="#e8f0fa").place(x=25, y=button_y + 48)

    pemasukan_indicate = tk.Label(options_frame, text='', bg='#e8f0fa', height=2)
    pemasukan_indicate.place(x=5, y=indicate_y + 40)

    pengeluaran_btn = tk.Button(options_frame, text='Pengeluaran', font=('Bold', 15), fg='#0097B2', bd=0, bg='#e8f0fa', command=lambda: indicate(pengeluaran_indicate, pengeluaran_page))
    pengeluaran_btn.place(x=60, y=button_y + 80)

    pengeluaran_icon = tk.PhotoImage(file="assets/donation.png")
    Label(options_frame, image=pengeluaran_icon, border=0, bg="#e8f0fa").place(x=25, y=button_y + 88)

    pengeluaran_indicate = tk.Label(options_frame, text='', bg='#e8f0fa',height=2)
    pengeluaran_indicate.place(x=5, y=indicate_y + 80)

    tagihan_btn = tk.Button(options_frame, text='Tagihan', font=('Bold', 15), fg='#0097B2', bd=0, bg='#e8f0fa', command=lambda: indicate(tagihan_indicate, tagihan_page))
    tagihan_btn.place(x=60, y=button_y + 120)

    tagihan_icon = tk.PhotoImage(file="assets/bill.png")
    Label(options_frame, image=tagihan_icon, border=0, bg="#e8f0fa").place(x=25, y=button_y + 128)

    tagihan_indicate = tk.Label(options_frame, text='', bg='#e8f0fa',height=2)
    tagihan_indicate.place(x=5, y=indicate_y + 120)

    laporan_btn = tk.Button(options_frame, text='Laporan', font=('Bold', 15), fg='#0097B2', bd=0, bg='#e8f0fa', command=lambda: indicate(laporan_indicate, laporan_page))
    laporan_btn.place(x=60, y=button_y + 160)

    laporan_icon = tk.PhotoImage(file="assets/prescription.png")
    Label(options_frame, image=laporan_icon, border=0, bg="#e8f0fa").place(x=25, y=button_y + 168)

    laporan_indicate = tk.Label(options_frame, text='', bg='#e8f0fa',height=2)
    laporan_indicate.place(x=5, y=indicate_y + 160)

    options_frame.pack(side=tk.LEFT)
    options_frame.pack_propagate(False)
    options_frame.configure(width=200, height=675)

    main_frame = tk.Frame(root, bg='white')
    main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    indicate(home_indicate, dashboard_page)

    root.mainloop()

if __name__ == "__main__":
    dashboard()