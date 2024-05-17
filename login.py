from tkinter import *
import tkinter as tk

def halaman_login():
    window = tk.Tk()
    window.title("Login")
    window.geometry("1200x675")
    window.configure(bg="White")
    window.resizable(True, True)

    frame = Frame(window, width=350, height=300, bg="#0097B2")
    frame.place(x=430,y=250)

    heading = Label(frame, text="Login", fg="White", bg="#0097B2", font=("Montserrat", 23, "bold"))
    heading.place(x=135, y=10)

    text_username = Label(frame, text="Username", fg="Black", border=0, font=(11))
    text_username.place(x=55,y=83)
    username = Entry(frame, width=26, fg="Black", border="2", bg="White", font=(11))
    username.place(x=55,y=105)
    # username.insert(0, "Username")
    
    text_password = Label(frame, text="Password", fg="Black", border=0, font=(11))
    text_password.place(x=55,y=135)
    password = Entry(frame, width=26, fg="Black", border="2", bg="White", font=(11))
    password.place(x=55,y=157)

    # img = PhotoImage(file="assets/Logo PiggyFund.png")
    # Label(window, image=img, bg="White",).place(x=425,y=20)


    def halaman_register():
        global window2
        window.destroy()
        window2 = tk.Tk()
        window2.title("Login")
        window2.geometry("1200x675")
        window2.configure(bg="White")
        window2.resizable(True, True) #mengubah ukuran 

        frame = Frame(window2, width=350, height=300, bg="#0097B2")
        frame.place(x=430,y=250)

        heading = Label(frame, text="Login", fg="White", bg="#0097B2", font=("Montserrat", 23, "bold"))
        heading.place(x=135, y=10)

        text_username = Label(frame, text="Username", fg="Black", border=0, font=(11))
        text_username.place(x=55,y=83)
        username = Entry(frame, width=26, fg="Black", border="2", bg="White", font=(11))
        username.place(x=55,y=105)
        # username.insert(0, "Username")
        
        text_password = Label(frame, text="Password", fg="Black", border=0, font=(11))
        text_password.place(x=55,y=135)
        password = Entry(frame, width=26, fg="Black", border="2", bg="White", font=(11))
        password.place(x=55,y=157)

        # img = PhotoImage(file="assets/Logo PiggyFund.png")
        # Label(window2, image=img, bg="White",).place(x=150,y=125)

        Button(frame, width=35, height=1, text="Sign Up", fg="White", bg="#57a1f8", command=login).place(x=50,y=200)
        Button(frame, width=35, height=1, text="Back", fg="Black", bg="White", command=back_login).place(x=50,y=230)

        window2.mainloop()


    def login():
        window2.destroy()
        halaman_login()

    def back_login():
        window2.destroy()
        halaman_login()


    Button(frame, width=35, height=1, text="Login", fg="White", bg="#57a1f8").place(x=50,y=200)
    Button(frame, width=35, height=1, text="Sign Up", fg="White", bg="#57a1f8", command=halaman_register).place(x=50,y=230)

    window.mainloop()



halaman_login()