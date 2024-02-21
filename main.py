import tkinter as tk
from tkinter import ttk
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    url = entry.get()
    
    if url:
        # Generate QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Display QR Code in Tkinter window
        img = ImageTk.PhotoImage(img)
        qr_code_label.config(image=img)
        qr_code_label.image = img
    else:
        tk.messagebox.showinfo("Error", "Please enter a URL.")

# Create main window
root = tk.Tk()
root.title("QR Code Generator")

# Create and place widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label = ttk.Label(frame, text="Enter URL:")
label.grid(row=0, column=0, sticky=tk.W)

entry = ttk.Entry(frame, width=40)
entry.grid(row=0, column=1, columnspan=2, sticky=(tk.W, tk.E))

generate_button = ttk.Button(frame, text="Generate QR Code", command=generate_qr_code)
generate_button.grid(row=1, column=0, columnspan=3)

qr_code_label = ttk.Label(frame)
qr_code_label.grid(row=2, column=0, columnspan=3)

# Start Tkinter event loop
root.mainloop()
