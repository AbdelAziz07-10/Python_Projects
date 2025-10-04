from tkinter import *
import os

def shutdown():
    return os.system("shutdown /s /t 1")

def restart():
    return os.system("shutdown /r /t 1")

def logout():
    return os.system("shutdown -l")

master = Tk()
master.title("System Control")
master.geometry("300x200")
master.resizable(False, False)

master.configure(bg='#2b2b2b')

frame = Frame(master, bg='#2b2b2b')
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

title = Label(frame, text="System Control Panel", font=("Arial", 14, "bold"), 
              bg='#2b2b2b', fg='white')
title.pack(pady=20)

button_style = {
    'font': ('Arial', 11),
    'width': 15,
    'height': 2,
    'bd': 0,
    'cursor': 'hand2'
}

Button(frame, text="Shutdown", command=shutdown, bg='#e74c3c', fg='white', 
       activebackground='#c0392b', **button_style).pack(pady=5)

Button(frame, text="Restart", command=restart, bg='#f39c12', fg='white', 
       activebackground='#e67e22', **button_style).pack(pady=5)

Button(frame, text="Log Out", command=logout, bg='#3498db', fg='white', 
       activebackground='#2980b9', **button_style).pack(pady=5)

mainloop()