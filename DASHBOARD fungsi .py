import tkinter as tk

root = tk.Tk()
root.geometry('1200x675')
root.title('DASHBOARD')

def dashboard_page():
    home_frame = tk.Frame(main_frame)
    lb = tk.Label(home_frame, text='DASHBOARD\n\nPage: 1', font=('Bold', 50))
    lb.pack()
    home_frame.pack(pady=20)

def pemasukan_page():
    pemasukan_frame = tk.Frame(main_frame)
    lb = tk.Label(pemasukan_frame, text='PEMASUKAN\n\nPage: 2', font=('Bold', 50))
    lb.pack()
    pemasukan_frame.pack(pady=20)

def pengeluaran_page():
    pengeluaran_frame = tk.Frame(main_frame)
    lb = tk.Label(pengeluaran_frame, text='PENGELUARAN\n\nPage: 3', font=('Bold', 50))
    lb.pack()
    pengeluaran_frame.pack(pady=20)

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

home_btn = tk.Button(options_frame, text='DASHBOARD', font=('Bold', 15),
                     fg='#158aff', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(home_indicate, dashboard_page))
home_btn.place(x=30, y=40)

home_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
home_indicate.place(x=5, y=45)

pemasukan_btn = tk.Button(options_frame, text='Pemasukan', font=('Bold', 15),
                          fg='#158aff', bd=0, bg='#c3c3c3',
                          command=lambda: indicate(pemasukan_indicate, pemasukan_page))
pemasukan_btn.place(x=30, y=80)

pemasukan_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
pemasukan_indicate.place(x=5, y=85)

pengeluaran_btn = tk.Button(options_frame, text='Pengeluaran', font=('Bold', 15),
                            fg='#158aff', bd=0, bg='#c3c3c3',
                            command=lambda: indicate(pengeluaran_indicate, pengeluaran_page))
pengeluaran_btn.place(x=30, y=120)

pengeluaran_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
pengeluaran_indicate.place(x=5, y=125)

tagihan_btn = tk.Button(options_frame, text='Tagihan', font=('Bold', 15),
                        fg='#158aff', bd=0, bg='#c3c3c3',
                        command=lambda: indicate(tagihan_indicate, tagihan_page))
tagihan_btn.place(x=30, y=160)

tagihan_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
tagihan_indicate.place(x=5, y=165)

laporan_btn = tk.Button(options_frame, text='Laporan', font=('Bold', 15),
                        fg='#158aff', bd=0, bg='#c3c3c3',
                        command=lambda: indicate(laporan_indicate, laporan_page))
laporan_btn.place(x=30, y=200)

laporan_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
laporan_indicate.place(x=5, y=205)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=200, height=675)

main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)
main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Load the initial page
indicate(home_indicate, dashboard_page)

root.mainloop()
