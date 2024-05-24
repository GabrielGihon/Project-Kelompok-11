from tkinter import *
from tkinter import messagebox
import os

def halaman_login():
    filename = "Project-Kelompok-11/database/datauser.csv"

    global user, pw, window
    window = Tk()
    window.title("Welcome")
    window.geometry("1200x675")
    window.configure(bg="White")
    window.resizable(False, False)
    
    img = PhotoImage(file="Project-Kelompok-11/assets/background.png")
    Label(window, image=img, border=0, bg="White").place(x=0, y=0)
    
    frame = Frame(window, width=350, height=400, bg="White")
    frame.place(x=600, y=130)
    
    heading = Label(frame, text="Welcome!", fg="#447082", bg="White", font=("Poppins", 23, "bold"))
    heading.place(x=50, y=50)
    
    # Function to save username and password
    def sign_up():
        global username2
        username2 = user2.get()
        password2 = pw2.get()
        with open(filename, "r") as file1:
            for i in file1:
                z = 0
                a,b = i.split(",")
                b = b.strip()
                
                if username2 == "" or username2 == "Username" or password2 == "" or password2 == "Password":
                    messagebox.showinfo("Error", "Username/Password tidak boleh kosong \nSilahkan isi Username dan Password")
                    break
                elif username2 == a:
                    messagebox.showinfo("Error", "Username sudah digunakan silahkan ganti username")
                    break
                else:
                    z += 1
            if z == len(i[0]):
                with open(filename, "a") as file:
                    file.write(f"{username2},{password2}\n")
                os.makedirs(f"Project-Kelompok-11/database/{username2}", exist_ok=True)
                
                messagebox.showinfo("Berhasil", "Username dan Password telah diregristrasi")
                window2.destroy()
                halaman_login()
        
    # Function to handle login
    def login():
        global username
        username = user.get()
        password = pw.get()
        c = 0
        
        if username == "" or username == "Username" or password == "" or password == "Password":
            messagebox.showinfo("Error", "Username/Password tidak boleh kosong \nSilahkan isi username")
        else:
            with open(filename, "r") as file:
                for i in file:
                    c += 1
                    a,b = i.split(",")
                    b = b.strip()
                    
                    if a == username and b == password:
                        window.destroy()
                        messagebox.showinfo("Berhasil", "Login sukses")
                        # md.program()
                        break
                else:
                    messagebox.showinfo("Error", "Akun tidak ditemukan")
                    
    def on_enter_user(e):
        user.delete(0, "end")
    def on_leave_user(e):
        if user.get() == "":
            user.insert(0, "Username")
    
    user = Entry(frame, width=25, fg="Black", border=0, bg="White", font=("Poppins", 12))
    user.place(x=30, y=150)
    user.insert(0, "Username")
    user.bind("<FocusIn>", on_enter_user)
    user.bind("<FocusOut>", on_leave_user)
    Frame(frame, width=280, height=2, bg="Black").place(x=25, y=171)
    
    def on_enter_pw(e):
        pw.delete(0, "end")
    def on_leave_pw(e):
        if pw.get() == "":
            pw.insert(0, "Password")
    
    pw = Entry(frame, width=25, fg="Black", border=0, bg="White", font=("Poppins", 12))
    pw.place(x=30, y=190)
    pw.insert(0, "Password")
    pw.bind("<FocusIn>", on_enter_pw)
    pw.bind("<FocusOut>", on_leave_pw)
    Frame(frame, width=280, height=2, bg="Black").place(x=25, y=211)
    
    # Function to handle registration page
    def halaman_register():
        global window2, user2, pw2
        
        window.destroy()
        window2 = Tk()
        window2.title("Register")
        window2.geometry("1200x675")
        window2.configure(bg="White")
        window2.resizable(False, False)
        
        img = PhotoImage(file="Project-Kelompok-11/assets/background.png")
        Label(window2, image=img, border=0, bg="White").place(x=0, y=0)
        
        frame = Frame(window2, width=350, height=400, bg="White")
        frame.place(x=600, y=130)
        
        heading = Label(frame, text="Register", fg="#447082", bg="White", font=("Poppins", 23, "bold"))
        heading.place(x=50, y=50)
        
        def on_enter_user2(e):
            user2.delete(0, "end")
        def on_leave_user2(e):
            if user2.get() == "":
                user2.insert(0, "Username")
        
        user2 = Entry(frame, width=25, fg="Black", border=0, bg="White", font=("Poppins", 12))
        user2.place(x=30, y=150)
        user2.insert(0, "Username")
        user2.bind("<FocusIn>", on_enter_user2)
        user2.bind("<FocusOut>", on_leave_user2)
        Frame(frame, width=280, height=2, bg="Black").place(x=25, y=171)
        
        def on_enter_pw2(e):
            pw2.delete(0, "end")
        def on_leave_pw2(e):
            if pw2.get() == "":
                pw2.insert(0, "Password")
        
        pw2 = Entry(frame, width=25, fg="Black", border=0, bg="White", font=("Poppins", 12))
        pw2.place(x=30, y=190)
        pw2.insert(0, "Password")
        pw2.bind("<FocusIn>", on_enter_pw2)
        pw2.bind("<FocusOut>", on_leave_pw2)
        Frame(frame, width=280, height=2, bg="Black").place(x=25, y=211)
        
        Label(frame, height=1, text="Have an account?", fg="Black", bg="White", font=("Poppins", 8)).place(x=35, y=241)
        Button(frame, width=29, pady=7, text="Register", fg="White", bg="#12baff", cursor="hand2", border=0, command=sign_up, font=("Poppins", 8)).place(x=60, y=280)
        Button(frame, width=10, height=1, text="Login", fg="#12baff", bg="White", cursor="hand2", border=0, command=back_login, font=("Poppins", 8)).place(x=150, y=240)
        
        window2.mainloop()
    
    def back_login():
        window2.destroy()
        halaman_login()
        
    Label(frame, height=1, text="Don't have account?", fg="Black", bg="White", font=("Poppins", 8)).place(x=35, y=241)
    Button(frame, width=29, pady=7, text="Login", fg="White", bg="#12baff", cursor="hand2", border=0, command=login, font=("Poppins", 8)).place(x=60, y=280)
    Button(frame, width=10, height=1, text="Register", fg="#12baff", bg="White", cursor="hand2", border=0, command=halaman_register, font=("Poppins", 8)).place(x=150, y=240)
    
    window.mainloop()

if __name__ == "__main__":
    halaman_login()
