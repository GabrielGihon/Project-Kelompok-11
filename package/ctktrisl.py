import customtkinter as ctk
from PIL import Image, ImageTk
from tkcalendar import DateEntry

def dashboard():
    ctk.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    root = ctk.CTk()
    root.geometry('1200x675')
    root.title('DASHBOARD')
    root.resizable(False, False)

    img = Image.open("assets/Text Aja.png")
    img = img.resize((150, 75), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    label_img = ctk.CTkLabel(root, image=img, text="")
    label_img.place(x=10, y=10)

    img2 = Image.open("assets/Logo Only.png")
    img2 = img2.resize((100, 75), Image.Resampling.LANCZOS)
    img2 = ImageTk.PhotoImage(img2)
    label_img2 = ctk.CTkLabel(root, image=img2, text="")
    label_img2.place(x=10, y=90)

    def dashboard_page():
        home_frame = ctk.CTkFrame(main_frame)
        
        bg_image = Image.open("assets/bg dashboard.png")
        bg_image = bg_image.resize((1200, 675), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(bg_image)
        
        bg_label = ctk.CTkLabel(main_frame, image=bg_image, text="")
        bg_label.image = bg_image  
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        frame_totalsaldo = ctk.CTkFrame(main_frame, width= 250, height=130, fg_color='blue')
        frame_totalsaldo.place(x=100, y=150)
        
        lb_1 = ctk.CTkLabel(frame_totalsaldo, text='Total Saldo', font=('Poppins', 16), text_color='white')
        lb_1.place(x=80, y=20)
        
        frame_pemasukan = ctk.CTkFrame(main_frame, width=250, height=130, fg_color='green')
        frame_pemasukan.place(x=400, y=150)
        
        lb_2 = ctk.CTkLabel(frame_pemasukan, text='Pemasukan', font=('Poppins', 16), text_color='white')
        lb_2.place(x=80, y=20)
        
        frame_pengeluaran = ctk.CTkFrame(main_frame, width=250, height=130, fg_color='red')
        frame_pengeluaran.place(x=700, y=150)
        
        lb_3 = ctk.CTkLabel(frame_pengeluaran, text='Pengeluaran', font=('Poppins', 16), text_color='white')
        lb_3.place(x=80, y=20)
        
        lb = ctk.CTkLabel(home_frame, text='', font=('Poppins', 50))
        lb.pack()
        
        pengeluaran_lb = ctk.CTkLabel(home_frame, text='Dashboard', font=('Bold', 34))
        pengeluaran_lb.place(x=10, y=80)
        
        frame_bawah = ctk.CTkFrame(main_frame, width=975, height=300, fg_color='#c3c3c3')
        frame_bawah.place(x=10, y=350)
        
        lb.pack()
        
        home_frame.pack(pady=20)

    def pemasukan_page():
        frame_bawah = ctk.CTkFrame(main_frame, width=975, height=500, fg_color='#c3c3c3')
        frame_bawah.place(x=10, y=150)
        
        lb_3 = ctk.CTkLabel(frame_bawah, text='Pemasukan', font=('Poppins',20), text_color='Black', fg_color='#c3c3c3')
        lb_3.place(x=65, y=20)

    def pengeluaran_page():
        frame_atas = ctk.CTkFrame(main_frame, width=975, height=40, fg_color='#c3c3c3')
        frame_atas.place(x=10, y=10)

        frame_bawah = ctk.CTkFrame(main_frame, width=975, height=500, fg_color='#c3c3c3')
        frame_bawah.place(x=10, y=150)
        
        lb_3 = ctk.CTkLabel(frame_bawah, text='Pengeluaran', font=('Poppins',20), text_color='Black', fg_color='#c3c3c3')
        lb_3.place(x=65, y=20)

        ctk.CTkLabel(frame_bawah, text="Masukkan Tanggal Pengeluaran:").place(x=65, y=80)
        date_entry = DateEntry(frame_bawah, date_pattern='dd/MM/yyyy')
        date_entry.place(x=250, y=80)

        ctk.CTkLabel(frame_bawah, text="Masukkan Keterangan Pengeluaran:").place(x=65, y=120)
        description_entry = ctk.CTkEntry(frame_bawah)
        description_entry.place(x=250, y=120)

        ctk.CTkLabel(frame_bawah, text="Masukkan Keperluan Pengeluaran:").place(x=65, y=160)
        purpose_combobox = ctk.CTkComboBox(frame_bawah, values=["Makan dan Minum", "Transportasi", "Belanja", "Lainnya"])
        purpose_combobox.place(x=250, y=160)
        purpose_combobox.set("Makan dan Minum")

        ctk.CTkLabel(frame_bawah, text="Masukkan Jumlah Pengeluaran:").place(x=65, y=200)
        amount_entry = ctk.CTkEntry(frame_bawah)
        amount_entry.place(x=250, y=200)

    def tagihan_page():
        tagihan_frame = ctk.CTkFrame(main_frame)
        lb = ctk.CTkLabel(tagihan_frame, text='TAGIHAN\n\nPage: 4', font=('Bold', 50))
        lb.pack()
        tagihan_frame.pack(pady=20)

    def laporan_page():
        laporan_frame = ctk.CTkFrame(main_frame)
        lb = ctk.CTkLabel(laporan_frame, text='LAPORAN\n\nPage: 5', font=('Bold', 50))
        lb.pack()
        laporan_frame.pack(pady=20)

    def hide_indicators():
        home_indicate.configure(fg_color='#c3c3c3')
        pemasukan_indicate.configure(fg_color='#c3c3c3')
        pengeluaran_indicate.configure(fg_color='#c3c3c3')
        tagihan_indicate.configure(fg_color='#c3c3c3')
        laporan_indicate.configure(fg_color='#c3c3c3')

    def delete_pages():
        for frame in main_frame.winfo_children():
            frame.destroy()

    def indicate(lb, page):
        hide_indicators()
        lb.configure(fg_color='#158aff')
        delete_pages()
        page()

    options_frame = ctk.CTkFrame(root, fg_color='#c3c3c3')

    img = Image.open("assets/LogoKecil.png")
    img = ImageTk.PhotoImage(img)
    ctk.CTkLabel(options_frame, image=img, text="", fg_color="#c3c3c3").place(x=0, y=0)

    img2 = Image.open("assets/TextAja.png")
    img2 = ImageTk.PhotoImage(img2)
    ctk.CTkLabel(options_frame, image=img2, text="", fg_color="#c3c3c3").place(x=90, y=10)

    # Sesuaikan posisi tombol dan indikator agar berada di bawah gambar
    button_y = 120
    indicate_y = 125

    home_btn = ctk.CTkButton(options_frame, text='DASHBOARD', font=('Bold', 15), text_color='#158aff', command=lambda: indicate(home_indicate, dashboard_page), fg_color='#c3c3c3', hover_color='#c3c3c3')
    home_btn.place(x=10, y=button_y)

    home_indicate = ctk.CTkLabel(options_frame, text='', fg_color='#c3c3c3')
    home_indicate.place(x=5, y=indicate_y)

    pemasukan_btn = ctk.CTkButton(options_frame, text='Pemasukan', font=('Bold', 15), text_color='#158aff', command=lambda: indicate(pemasukan_indicate, pemasukan_page), fg_color='#c3c3c3', hover_color='#c3c3c3')
    pemasukan_btn.place(x=10, y=button_y + 40)

    pemasukan_indicate = ctk.CTkLabel(options_frame, text='', fg_color='#c3c3c3', height=2)
    pemasukan_indicate.place(x=5, y=indicate_y + 40)

    pengeluaran_btn = ctk.CTkButton(options_frame, text='Pengeluaran', font=('Bold', 15), text_color='#158aff', command=lambda: indicate(pengeluaran_indicate, pengeluaran_page), fg_color='#c3c3c3', hover_color='#c3c3c3')
    pengeluaran_btn.place(x=10, y=button_y + 80)

    pengeluaran_indicate = ctk.CTkLabel(options_frame, text='', fg_color='#c3c3c3')
    pengeluaran_indicate.place(x=5, y=indicate_y + 80)

    tagihan_btn = ctk.CTkButton(options_frame, text='Tagihan', font=('Bold', 15), text_color='#158aff', command=lambda: indicate(tagihan_indicate, tagihan_page), fg_color='#c3c3c3', hover_color='#c3c3c3')
    tagihan_btn.place(x=10, y=button_y + 120)

    tagihan_indicate = ctk.CTkLabel(options_frame, text='', fg_color='#c3c3c3')
    tagihan_indicate.place(x=5, y=indicate_y + 120)

    laporan_btn = ctk.CTkButton(options_frame, text='Laporan', font=('Bold', 15), text_color='#158aff', command=lambda: indicate(laporan_indicate, laporan_page), fg_color='#c3c3c3', hover_color='#c3c3c3')
    laporan_btn.place(x=10, y=button_y + 160)

    laporan_indicate = ctk.CTkLabel(options_frame, text='', fg_color='#c3c3c3')
    laporan_indicate.place(x=5, y=indicate_y + 160)
    options_frame.pack(side=ctk.LEFT)
    options_frame.pack_propagate(False)
    options_frame.configure(width=200, height=675)

    main_frame = ctk.CTkFrame(root, fg_color="white", corner_radius=15)
    main_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

    indicate(home_indicate, dashboard_page)

    root.mainloop()
    
if __name__ == "__main__":
    dashboard()
