import tkinter as tk
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    text = text_entry.get()
    if text:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qrcode.png")

        img = Image.open("qrcode.png")
        photo = ImageTk.PhotoImage(img)

        qr_code_label.config(image=photo)
        qr_code_label.photo = photo

root = tk.Tk()
root.title("Prescribe Medicine")
root.geometry("600x400")
root.configure(bg="#222")

title_label = tk.Label(root, text="Prescribe Medicine", font=("Helvetica", 20), bg="#222", fg="white")
title_label.pack(pady=20)

text_entry = tk.Entry(root, font=("Helvetica", 16), justify="center")
text_entry.insert(0, "")
text_entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code, font=("Helvetica", 16), bg="#007BFF", fg="white")
generate_button.pack()

qr_code_label = tk.Label(root, bg="#222")
qr_code_label.pack(pady=20)

root.mainloop()
