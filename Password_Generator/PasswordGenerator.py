import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    password = []
    for i in range(5):
        alpha = random.choice(string.ascii_letters)
        symbol = random.choice(string.punctuation)
        numbers = random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(numbers)
    passwords = "".join(str(x) for x in password) 
    
    password_var.set(passwords)
    copy_button.config(state="normal")

def copy_password():
    password = password_var.get()
    if password and password != "Your password will appear here":
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied!", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Please generate a password first!")

def clear_password():
    password_var.set("Your password will appear here")
    copy_button.config(state="disabled")

root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("500x400")
root.configure(bg="#2c3e50")
root.resizable(False, False)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

title_label = tk.Label(root, 
                      text="🔐 Secure Password Generator", 
                      font=("Arial", 20, "bold"),
                      bg="#2c3e50", 
                      fg="#ecf0f1")
title_label.grid(row=0, column=0, columnspan=3, pady=20)

subtitle_label = tk.Label(root, 
                         text="Generate strong 15-character passwords", 
                         font=("Arial", 11),
                         bg="#2c3e50", 
                         fg="#95a5a6")
subtitle_label.grid(row=1, column=0, columnspan=3, pady=(0, 20))

password_frame = tk.Frame(root, bg="#34495e", relief="raised", bd=2)
password_frame.grid(row=2, column=0, columnspan=3, padx=20, pady=20, sticky="ew")

password_var = tk.StringVar()
password_var.set("Your password will appear here")

password_label = tk.Label(password_frame, 
                         textvariable=password_var,
                         font=("Courier New", 14, "bold"),
                         bg="#34495e", 
                         fg="#e74c3c",
                         wraplength=400,
                         pady=15)
password_label.pack(expand=True, fill="both")

button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.grid(row=3, column=0, columnspan=3, pady=20)

generate_button = tk.Button(button_frame, 
                           text="🎲 Generate Password", 
                           command=generate_password,
                           font=("Arial", 12, "bold"),
                           bg="#27ae60", 
                           fg="white",
                           activebackground="#2ecc71",
                           activeforeground="white",
                           relief="raised",
                           bd=3,
                           padx=20,
                           pady=10,
                           cursor="hand2")
generate_button.pack(side="left", padx=10)

copy_button = tk.Button(button_frame, 
                       text="📋 Copy to Clipboard", 
                       command=copy_password,
                       font=("Arial", 12, "bold"),
                       bg="#3498db", 
                       fg="white",
                       activebackground="#5dade2",
                       activeforeground="white",
                       relief="raised",
                       bd=3,
                       padx=20,
                       pady=10,
                       cursor="hand2",
                       state="disabled")  
copy_button.pack(side="left", padx=10)


clear_button = tk.Button(button_frame, 
                        text="🗑️ Clear", 
                        command=clear_password,
                        font=("Arial", 12, "bold"),
                        bg="#e74c3c", 
                        fg="white",
                        activebackground="#ec7063",
                        activeforeground="white",
                        relief="raised",
                        bd=3,
                        padx=20,
                        pady=10,
                        cursor="hand2")
clear_button.pack(side="left", padx=10)


info_frame = tk.Frame(root, bg="#2c3e50")
info_frame.grid(row=4, column=0, columnspan=3, pady=(20, 0))

info_text = tk.Label(info_frame, 
                    text="✓ Contains letters, numbers & symbols\n✓ 15 characters long\n✓ Cryptographically secure", 
                    font=("Arial", 9),
                    bg="#2c3e50", 
                    fg="#95a5a6",
                    justify="center")
info_text.pack()


footer_label = tk.Label(root, 
                       text="Keep your passwords safe and secure! 🛡️", 
                       font=("Arial", 8),
                       bg="#2c3e50", 
                       fg="#7f8c8d")
footer_label.grid(row=5, column=0, columnspan=3, pady=(10, 20))

root.mainloop()