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

    img = Image.open("assets/Text Aja.png")
    img = img.resize((150, 75), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    label_img = tk.Label(root, image=img, border=0, bg="white")
    label_img.place(x=10, y=10)

    img2 = Image.open("assets/Logo Only.png")
    img2 = img2.resize((100, 75), Image.Resampling.LANCZOS)
    img2 = ImageTk.PhotoImage(img2)
    label_img2 = tk.Label(root, image=img2, border=0, bg="white")
    label_img2.place(x=10, y=90)


    def dashboard_page():
        home_frame = tk.Frame(main_frame)

        bg_image = Image.open("assets/bg dashboard.png")
        bg_image = bg_image.resize((1200, 675), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(main_frame, image=bg_image)
        bg_label.image = bg_image  
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame_totalsaldo = tk.Frame(main_frame, width= 250, height=130, bg='blue')
        frame_totalsaldo.place(x=100, y=150)

        lb_1 = tk.Label(frame_totalsaldo, text='Total Saldo', font='Poppins', bg='blue', fg='white')
        lb_1.place(x=100, y=20)

        frame_pemasukan = tk.Frame(main_frame, width=250, height=130, bg='green')
        frame_pemasukan.place(x=400, y=150)

        lb_2 = tk.Label(frame_pemasukan, text='Pemasukan', font='Poppins', bg='green', fg='white')
        lb_2.place(x=100, y=20)

        frame_pengeluaran = tk.Frame(main_frame, width=250, height=130, bg='red')
        frame_pengeluaran.place(x=700, y=150)

        lb_3 = tk.Label(frame_pengeluaran, text='Pengeluaran', font='Poppins', bg='red', fg='white')
        lb_3.place(x=100, y=20)

        lb = tk.Label(home_frame, text='', font=('Poppins', 50))
        lb.pack()
        
        pengeluaran_lb = tk.Label(home_frame, text='Dashboard', font=('Bold', 34))
        pengeluaran_lb.place(x=10, y=80)

        frame_bawah = tk.Frame(main_frame, width=975, height=300, bg='#c3c3c3')
        frame_bawah.place(x=10, y=350)

        lb.pack()
        
        frame_bawah = tk.Frame(main_frame)
        home_frame.pack(pady=20)

    def pemasukan_page():
        frame_bawah = tk.Frame(main_frame, width=975, height=500, bg='#c3c3c3')
        frame_bawah.place(x=10, y=150)
        
        lb_3 = tk.Label(frame_bawah, text='Pemasukan', font=('Poppins',20), fg='Black', bg='#c3c3c3')
        lb_3.place(x=65, y=20)

        
    def pengeluaran_page():

        frame_atas = tk.Frame(main_frame, width=975, height=40, bg='#c3c3c3')
        frame_atas.place(x=10, y=10)

        frame_bawah = tk.Frame(main_frame, width=975, height=500, bg='#c3c3c3')
        frame_bawah.place(x=10, y=150)
        
        lb_3 = tk.Label(frame_bawah, text='Pengeluaran', font=('Poppins',20), fg='Black', bg='#c3c3c3')
        lb_3.place(x=65, y=20)

        tk.Label(frame_bawah, text="Masukkan Tanggal Pengeluaran:").place(x=65, y=80)
        date_entry = DateEntry(frame_bawah, date_pattern='dd/MM/yyyy')
        date_entry.place(x=250, y=80)

        tk.Label(frame_bawah, text="Masukkan Keterangan Pengeluaran:").place(x=65, y=120)
        description_entry = tk.Entry(frame_bawah)
        description_entry.place(x=250, y=120)

        tk.Label(frame_bawah, text="Masukkan Keperluan Pengeluaran:").place(x=65, y=160)
        purpose_combobox = ttk.Combobox(frame_bawah, values=["Makan dan Minum", "Transportasi", "Belanja", "Lainnya"])
        purpose_combobox.place(x=250, y=160)
        purpose_combobox.current(0)

        tk.Label(frame_bawah, text="Masukkan Jumlah Pengeluaran:").place(x=65, y=200)
        amount_entry = tk.Entry(frame_bawah)
        amount_entry.place(x=250, y=200)

    def tagihan_page():
        tagihan_frame = tk.Frame(main_frame)
        lb = tk.Label(tagihan_frame, text='TAGIHAN\n\nPage: 4', font=('Bold', 50))
        lb.pack()
        tagihan_frame.pack(pady=20)

    def laporan_page():
        laporan_frame = tk.Frame(main_frame)
        lb = tk.Label(laporan_frame, text='LAPORAN\n\nPage: 5', font=('Bold', 50))
        lb.pack()
        laporan_frame.pack(pady=20)

    def hide_indicators():
        home_indicate.config(bg='#c3c3c3')
        pemasukan_indicate.config(bg='#c3c3c3')
        pengeluaran_indicate.config(bg='#c3c3c3')
        tagihan_indicate.config(bg='#c3c3c3')
        laporan_indicate.config(bg='#c3c3c3')

    def delete_pages():
        for frame in main_frame.winfo_children():
            frame.destroy()

    def indicate(lb, page):
        hide_indicators()
        lb.config(bg='#158aff')
        delete_pages()
        page()

    options_frame = tk.Frame(root, bg='#c3c3c3')

    img = PhotoImage(file="assets/LogoKecil.png")
    Label(options_frame, image=img, border=0, bg="White").place(x=0, y=0)

    img2 = PhotoImage(file="assets/TextAja.png")
    Label(options_frame, image=img2, border=0, bg="#c3c3c3").place(x=90, y=10)

    # Sesuaikan posisi tombol dan indikator agar berada di bawah gambar
    button_y = 120
    indicate_y = 125

    home_btn = tk.Button(options_frame, text='DASHBOARD', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(home_indicate, dashboard_page))
    home_btn.place(x=10, y=button_y)

    home_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
    home_indicate.place(x=5, y=indicate_y)

    pemasukan_btn = tk.Button(options_frame, text='Pemasukan', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(pemasukan_indicate, pemasukan_page))
    pemasukan_btn.place(x=10, y=button_y + 40)

    pemasukan_indicate = tk.Label(options_frame, text='', bg='#c3c3c3', height=2)
    pemasukan_indicate.place(x=5, y=indicate_y + 40)

    pengeluaran_btn = tk.Button(options_frame, text='Pengeluaran', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(pengeluaran_indicate, pengeluaran_page))
    pengeluaran_btn.place(x=10, y=button_y + 80)

    pengeluaran_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
    pengeluaran_indicate.place(x=5, y=indicate_y + 80)

    tagihan_btn = tk.Button(options_frame, text='Tagihan', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(tagihan_indicate, tagihan_page))
    tagihan_btn.place(x=10, y=button_y + 120)

    tagihan_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
    tagihan_indicate.place(x=5, y=indicate_y + 120)

    laporan_btn = tk.Button(options_frame, text='Laporan', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(laporan_indicate, laporan_page))
    laporan_btn.place(x=10, y=button_y + 160)

    laporan_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
    laporan_indicate.place(x=5, y=indicate_y + 160)
    options_frame.pack(side=tk.LEFT)
    options_frame.pack_propagate(False)
    options_frame.configure(width=200, height=675)

    main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)
    main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    indicate(home_indicate, dashboard_page)

    root.mainloop()
    
if __name__ == "__main__":
    dashboard()
