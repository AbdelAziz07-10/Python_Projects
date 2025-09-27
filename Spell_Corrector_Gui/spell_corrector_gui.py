from tkinter import *
from textblob import TextBlob

def clear():
    input_field.delete(0, END)
    output_field.delete(0, END)

def check_spelling():
    text = input_field.get()
    blob = TextBlob(text)
    corrected = str(blob.correct())
    output_field.delete(0, END)
    output_field.insert(0, corrected)

if __name__ == "__main__":
    root = Tk()
    root.configure(bg='#2c3e50')
    root.geometry("450x180")
    root.title("Spell Checker")
    
    title = Label(root, text='Spell Checker Application',
                  fg='#ecf0f1', bg='#3498db', font=('Arial', 14, 'bold'))
    
    input_label = Label(root, text="Enter Word:", 
                       fg='#ecf0f1', bg='#34495e', font=('Arial', 10))
    
    output_label = Label(root, text="Corrected Word:", 
                        fg='#ecf0f1', bg='#34495e', font=('Arial', 10))
    
    title.grid(row=0, column=0, columnspan=2, pady=10, padx=20, sticky='ew')
    input_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
    output_label.grid(row=3, column=0, padx=10, pady=5, sticky='e')
    
    input_field = Entry(root, font=('Arial', 11), width=25, relief='solid', bd=1)
    output_field = Entry(root, font=('Arial', 11), width=25, relief='solid', bd=1)
    
    input_field.grid(row=1, column=1, padx=10, pady=5)
    output_field.grid(row=3, column=1, padx=10, pady=5)
    
    check_btn = Button(root, text="Check Spelling", bg="#27ae60", fg="white",
                       font=('Arial', 10, 'bold'), command=check_spelling, 
                       relief='flat', padx=20)
    check_btn.grid(row=2, column=1, pady=10)
    
    clear_btn = Button(root, text="Clear All", bg="#e74c3c", fg="white",
                       font=('Arial', 10, 'bold'), command=clear, 
                       relief='flat', padx=20)
    clear_btn.grid(row=4, column=1, pady=5)
    
    root.mainloop()