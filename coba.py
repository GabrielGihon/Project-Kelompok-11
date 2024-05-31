import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_pie_chart():
        # Data untuk pie chart
        labels = 'A', 'B', 'C', 'D'
        sizes = [15, 30, 45, 10]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
        explode = (0.1, 0, 0, 0)  # memisahkan bagian pertama
        
        # Membuat figure dan axis untuk pie chart
        fig = Figure(figsize=(6, 6))
        ax = fig.add_subplot(111)
        
        # Membuat pie chart
        ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)
        
        ax.axis('equal')  # Equal aspect ratio memastikan pie digambar sebagai lingkaran.
        
        return fig

def main():
        # Membuat jendela utama tkinter
        root = tk.Tk()
        root.title("Pie Chart di Tkinter")
        
        # Membuat canvas untuk menampilkan pie chart
        fig = create_pie_chart()
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        
        # Menempatkan canvas di jendela tkinter
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        # Menambahkan tombol untuk keluar
        exit_button = ttk.Button(root, text="Keluar", command=root.quit)
        exit_button.pack(side=tk.BOTTOM)
        
        # Menjalankan loop utama tkinter
        tk.mainloop()

if __name__ == "__main__":
        main()
