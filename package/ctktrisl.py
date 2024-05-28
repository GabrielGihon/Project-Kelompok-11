import customtkinter as ctk
from PIL import Image, ImageTk
from tkcalendar import DateEntry

def dashboard():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.geometry('1200x675')
    root.title('DASHBOARD')
    root.resizable(False, False)

    def dashboard_page():
        home_frame = ctk.CTkFrame(main_frame, fg_color='white')

        frame_atas = ctk.CTkFrame(main_frame, width=975, height=60, fg_color='#e8f0fa')
        frame_atas.place(x=10, y=10)

        lb_utama = ctk.CTkLabel(main_frame, text='Selamat Datang, ', font=('Poppins', 20), text_color='black')
        lb_utama.place(x=60, y=20)

        lb_utama = ctk.CTkLabel(main_frame, text='Dashboard ', font=('Poppins', 20), text_color='black')
        lb_utama.place(x=30, y=100)

        frame_totalsaldo = ctk.CTkFrame(main_frame, width=250, height=130, fg_color='#e8f0fa')
        frame_totalsaldo.place(x=100, y=150)

        lb_1 = ctk.CTkLabel(frame_totalsaldo, text='Total Saldo', font=('Poppins', 20), text_color='black')
        lb_1.place(x=50, y=20)

        frame_pemasukan = ctk.CTkFrame(main_frame, width=250, height=130, fg_color='#e8f0fa')
        frame_pemasukan.place(x=400, y=150)

        lb_2 = ctk.CTkLabel(frame_pemasukan, text='Pemasukan', font=('Poppins', 20), text_color='black')
        lb_2.place(x=50, y=20)

        frame_pengeluaran = ctk.CTkFrame(main_frame, width=250, height=130, fg_color='#e8f0fa')
        frame_pengeluaran.place(x=700, y=150)

        lb_3 = ctk.CTkLabel(frame_pengeluaran, text='Pengeluaran', font=('Poppins', 20), text_color='black')
        lb_3.place(x=50, y=20)

        frame_bawah = ctk.CTkFrame(main_frame, width=975, height=300, fg_color='#e8f0fa')
        frame_bawah.place(x=10, y=350)

        home_frame.pack(pady=100)

    def pemasukan_page():
        lb_utama = ctk.CTkLabel(main_frame, text='Pemasukan', font=('Poppins', 20), text_color='black')
        lb_utama.place(x=30, y=100)

        frame_atas = ctk.CTkFrame(main_frame, width=975, height=60, fg_color='#e8f0fa')
        frame_atas.place(x=10, y=10)

        frame_bawah = ctk.CTkFrame(main_frame, width=975, height=500, fg_color='#e8f0fa')
        frame_bawah.place(x=10, y=150)

        lb_3 = ctk.CTkLabel(frame_bawah, text='ISI', font=('Poppins', 20), text_color='black')
        lb_3.place(x=65, y=20)

        lb_utama1 = ctk.CTkLabel(main_frame, text='Total Pemasukan : ', font=('Poppins', 20), text_color='black')
        lb_utama1.place(x=60, y=20)

        ctk.CTkLabel(frame_bawah, text="Masukkan Tanggal Pemasukan:", text_color='black', fg_color='#e8f0fa').place(x=65, y=80)
        date_entry = DateEntry(frame_bawah, date_pattern='dd/MM/yyyy')
        date_entry.place(x=250, y=80)

        ctk.CTkLabel(frame_bawah, text="Masukkan Keterangan Pemasukan:", text_color='black', fg_color='#e8f0fa').place(x=65, y=120)
        description_entry = ctk.CTkEntry(frame_bawah)
        description_entry.place(x=250, y=120)

        ctk.CTkLabel(frame_bawah, text="Masukkan Keperluan Pemasukan:", text_color='black', fg_color='#e8f0fa').place(x=65, y=160)
        purpose_combobox = ctk.CTkComboBox(frame_bawah, values=["Gaji", "Bonus", "Investasi", "Lainnya"])
        purpose_combobox.place(x=250, y=160)
        purpose_combobox.set("Gaji")

        ctk.CTkLabel(frame_bawah, text="Masukkan Jumlah Pemasukan:", text_color='black', fg_color='#e8f0fa').place(x=65, y=200)
        amount_entry = ctk.CTkEntry(frame_bawah)
        amount_entry.place(x=250, y=200)
        
    def pengeluaran_page():
        lb_utama = ctk.CTkLabel(main_frame, text='Pengeluaran', font=('Poppins', 20), text_color='black')
        lb_utama.place(x=30, y=100)

        frame_atas = ctk.CTkFrame(main_frame, width=975, height=60, fg_color='#e8f0fa')
        frame_atas.place(x=10, y=10)

        frame_bawah = ctk.CTkFrame(main_frame, width=975, height=500, fg_color='#e8f0fa')
        frame_bawah.place(x=10, y=150)

        lb_utama1 = ctk.CTkLabel(main_frame, text='Total Pengeluaran :', font=('Poppins', 20), text_color='black')
        lb_utama1.place(x=60, y=20)

        lb_3 = ctk.CTkLabel(frame_bawah, text='Isi', font=('Poppins', 20), text_color='black')
        lb_3.place(x=65, y=20)

        ctk.CTkLabel(frame_bawah, text="Masukkan Tanggal Pengeluaran:", text_color='black', fg_color='#e8f0fa').place(x=65, y=80)
        date_entry = DateEntry(frame_bawah, date_pattern='dd/MM/yyyy')
        date_entry.place(x=250, y=80)

        ctk.CTkLabel(frame_bawah, text="Masukkan Keterangan Pengeluaran:", text_color='black', fg_color='#e8f0fa').place(x=65, y=120)
        description_entry = ctk.CTkEntry(frame_bawah)
        description_entry.place(x=250, y=120)

        ctk.CTkLabel(frame_bawah, text="Masukkan Keperluan Pengeluaran:", text_color='black', fg_color='#e8f0fa').place(x=65, y=160)
        purpose_combobox = ctk.CTkComboBox(frame_bawah, values=["Makan dan Minum", "Transportasi", "Belanja", "Lainnya"])
        purpose_combobox.place(x=250, y=160)
        purpose_combobox.set("Makan dan Minum")

        ctk.CTkLabel(frame_bawah, text="Masukkan Jumlah Pengeluaran:", text_color='black', fg_color='#e8f0fa').place(x=65, y=200)
        amount_entry = ctk.CTkEntry(frame_bawah)
        amount_entry.place(x=250, y=200)

    def tagihan_page():
        tagihan_frame = ctk.CTkFrame(main_frame, fg_color='white')

        lb_utama = ctk.CTkLabel(main_frame, text='Selamat Datang, ', font=('Poppins', 20), text_color='black')
        lb_utama.place(x=60, y=20)

        lb_utama = ctk.CTkLabel(main_frame, text='Tagihan ', font=('Poppins', 20), text_color='black')
        lb_utama.place(x=30, y=100)

        frame_atas = ctk.CTkFrame(main_frame, width=975, height=60, fg_color='#e8f0fa')
        frame_atas.place(x=10, y=10)

        frame_bawah = ctk.CTkFrame(main_frame, width=975, height=500, fg_color='#e8f0fa')
        frame_bawah.place(x=10, y=150)

        tagihan_frame.pack(pady=20)

    def laporan_page():
        laporan_frame = ctk.CTkFrame(main_frame, fg_color='white')

        lb_utama = ctk.CTkLabel(main_frame, text='Selamat Datang, ', font=('Poppins', 20), text_color='black')
        lb_utama.place(x=60, y=20)

        lb_utama = ctk.CTkLabel(main_frame, text='Laporan ', font=('Poppins', 20), text_color='black')
        lb_utama.place(x=30, y=100)

        frame_atas = ctk.CTkFrame(main_frame, width=975, height=60, fg_color='#e8f0fa')
        frame_atas.place(x=10, y=10)

        frame_bawah = ctk.CTkFrame(main_frame, width=975, height=500, fg_color='#e8f0fa')
        frame_bawah.place(x=10, y=150)

        laporan_frame.pack(pady=20)

    def hide_indicators():
        home_indicate.configure(fg_color='#e8f0fa')
        pemasukan_indicate.configure(fg_color='#e8f0fa')
        pengeluaran_indicate.configure(fg_color='#e8f0fa')
        tagihan_indicate.configure(fg_color='#e8f0fa')
        laporan_indicate.configure(fg_color='#e8f0fa')

    def delete_pages():
        for frame in main_frame.winfo_children():
            frame.destroy()

    def indicate(lb, page):
        hide_indicators()
        lb.configure(fg_color='#158aff')
        delete_pages()
        page()

    options_frame = ctk.CTkFrame(root, fg_color='#e8f0fa')

    img = ImageTk.PhotoImage(Image.open("assets/LogoKecil.png").resize((80, 80)))
    ctk.CTkLabel(options_frame, image=img, text='', fg_color='#e8f0fa').place(x=0, y=0)

    img2 = ImageTk.PhotoImage(Image.open("assets/TextAja.png").resize((100, 40)))
    ctk.CTkLabel(options_frame, image=img2, text='', fg_color='#e8f0fa').place(x=90, y=10)

    button_y = 120
    indicate_y = 125

    home_btn = ctk.CTkButton(options_frame, text='Dashboard', font=('Bold', 15), fg_color='#e8f0fa', text_color='#158aff', hover_color='#d4e4fc', command=lambda: indicate(home_indicate, dashboard_page))
    home_btn.place(x=10, y=button_y)

    home_indicate = ctk.CTkLabel(options_frame, text='', fg_color='#e8f0fa', height=2)
    home_indicate.place(x=5, y=indicate_y)

    pemasukan_btn = ctk.CTkButton(options_frame, text='Pemasukan', font=('Bold', 15), fg_color='#e8f0fa', text_color='#158aff', hover_color='#d4e4fc', command=lambda: indicate(pemasukan_indicate, pemasukan_page))
    pemasukan_btn.place(x=10, y=button_y + 40)

    pemasukan_indicate = ctk.CTkLabel(options_frame, text='', fg_color='#e8f0fa', height=2)
    pemasukan_indicate.place(x=5, y=indicate_y + 40)

    pengeluaran_btn = ctk.CTkButton(options_frame, text='Pengeluaran', font=('Bold', 15), fg_color='#e8f0fa', text_color='#158aff', hover_color='#d4e4fc', command=lambda: indicate(pengeluaran_indicate, pengeluaran_page))
    pengeluaran_btn.place(x=10, y=button_y + 80)

    pengeluaran_indicate = ctk.CTkLabel(options_frame, text='', fg_color='#e8f0fa', height=2)
    pengeluaran_indicate.place(x=5, y=indicate_y + 80)

    tagihan_btn = ctk.CTkButton(options_frame, text='Tagihan', font=('Bold', 15), fg_color='#e8f0fa', text_color='#158aff', hover_color='#d4e4fc', command=lambda: indicate(tagihan_indicate, tagihan_page))
    tagihan_btn.place(x=10, y=button_y + 120)

    tagihan_indicate = ctk.CTkLabel(options_frame, text='', fg_color='#e8f0fa', height=2)
    tagihan_indicate.place(x=5, y=indicate_y + 120)

    laporan_btn = ctk.CTkButton(options_frame, text='Laporan', font=('Bold', 15), fg_color='#e8f0fa', text_color='#158aff', hover_color='#d4e4fc', command=lambda: indicate(laporan_indicate, laporan_page))
    laporan_btn.place(x=10, y=button_y + 160)

    laporan_indicate = ctk.CTkLabel(options_frame, text='', fg_color='#e8f0fa', height=2)
    laporan_indicate.place(x=5, y=indicate_y + 160)

    options_frame.pack(side=ctk.LEFT)
    options_frame.pack_propagate(False)
    options_frame.configure(width=200, height=675)

    main_frame = ctk.CTkFrame(root, fg_color='white')
    main_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

    indicate(home_indicate, dashboard_page)

    root.mainloop()

if __name__ == "__main__":
    dashboard()
