import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
root.title("PNG to JPG Converter")
root.geometry("300x250+500+200")
canvas1 = tk.Canvas(root, width=300, height=250, bg='azure3', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text="Image Converter", bg='azure3')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def getPNG():
    global im1
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)

browse_png = tk.Button(text="Select PNG file", command=getPNG, bg="royalblue", fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browse_png)

def convert():
    global im1, message_label
    
    if 'message_label' in globals():
        message_label.destroy()
    
    if 'im1' not in globals() or im1 is None:
        message_label = tk.Label(root, text="❌ Please select an image first!", bg='azure3', fg='red', font=('helvetica', 10, 'bold'))
        canvas1.create_window(150, 220, window=message_label)
        return
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    
    if not export_file_path:
        message_label = tk.Label(root, text="❌ Please choose where to save!", bg='azure3', fg='red', font=('helvetica', 10, 'bold'))
        canvas1.create_window(150, 220, window=message_label)
        return
    
    rgb_im = im1.convert('RGB')
    rgb_im.save(export_file_path)
    
    message_label = tk.Label(root, text="✅ Conversion Done!", bg='azure3', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 220, window=message_label)

saveasbutton = tk.Button(text="Convert PNG to JPG", command=convert, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveasbutton)

root.mainloop()