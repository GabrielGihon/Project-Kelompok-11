from tkinter import *
from tkinter import messagebox
import tkinter as tk
import csv
import os 

def input_data_user(data, filename="assets/datauser.csv"):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["username", "password"])
        writer.writerow(data)
        
def read_data_user(filename="assets/datauser.csv"):
    if not os.path.isfile(filename):
        return []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def login_user(username, password):
    username = input_username.get()
    password = input_password.get()

    users = read_data_user()
    for user in users:
        if user['username'] == username and user['password'] == password:
            messagebox.showinfo("Success", "Login successful!")
            return
    messagebox.showerror("Error", "Invalid username or password.")

def register_user(username, password):
    username = input_username.get()
    password = input_password.get()

    if username and password:
        users = read_data_user()
        for user in users:
            if user['username'] == username:
                messagebox.showerror("Error", "Username already exists!")
                return
        input_data_user([username, password])
        messagebox.showinfo("Success", "Registration successful!")
    else:
        messagebox.showerror("Error", "Please enter both username and password.")


def halaman_login():
    global input_username, input_password
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
    input_username = Entry(frame, width=26, fg="Black", border="2", bg="White", font=(11))
    input_username.place(x=55,y=105)
    
    text_password = Label(frame, text="Password", fg="Black", border=0, font=(11))
    text_password.place(x=55,y=135)
    input_password = Entry(frame, width=26, fg="Black", border="2", bg="White", font=(11))
    input_password.place(x=55,y=157)

    def halaman_register():
        global window2
        window.destroy()
        window2 = tk.Tk()
        window2.title("Login")
        window2.geometry("1200x675")
        window2.configure(bg="White")
        window2.resizable(True, True) 

        frame = Frame(window2, width=350, height=300, bg="#0097B2")
        frame.place(x=430,y=250)

        heading = Label(frame, text="Login", fg="White", bg="#0097B2", font=("Montserrat", 23, "bold"))
        heading.place(x=135, y=10)

        text_username = Label(frame, text="Username", fg="Black", border=0, font=(11))
        text_username.place(x=55,y=83)
        input_username = Entry(frame, width=26, fg="Black", border="2", bg="White", font=(11))
        input_username.place(x=55,y=105)

        text_password = Label(frame, text="Password", fg="Black", border=0, font=(11))
        text_password.place(x=55,y=135)
        input_password = Entry(frame, width=26, fg="Black", border="2", bg="White", font=(11))
        input_password.place(x=55,y=157)


        Button(frame, width=35, height=1, text="Sign Up", fg="White", bg="#57a1f8", command=register_user).place(x=50,y=200)
        Button(frame, width=35, height=1, text="Back", fg="Black",bg="White",command=back_login).place(x=50,y=230)

        input_data_user(input_username, input_password)
        window2.mainloop()


    # def login_page():
    #     window2.destroy()
    #     halaman_login()

    def back_login():
        window2.destroy()
        halaman_login()

    Button(frame, width=35, height=1, text="Login", fg="White", bg="#57a1f8", command=login_user).place(x=50,y=200)
    Button(frame, width=35, height=1, text="Sign Up", fg="White", bg="#57a1f8", command=halaman_register).place(x=50,y=230)

    window.mainloop()
    
halaman_login()