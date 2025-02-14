import cv2
import tkinter as tk
from tkinter import filedialog, messagebox

# Character encoding dictionary
d = {chr(i): i for i in range(255)}

# Encrypt Function
def encrypt_message():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return
    
    img = cv2.imread(file_path)
    msg = text_entry.get("1.0", tk.END).strip()
    password = password_entry.get()
    
    if not msg or not password:
        messagebox.showerror("Error", "Message and Password cannot be empty!")
        return

    n, m, z = 0, 0, 0
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Images", "*.png")])
    if save_path:
        cv2.imwrite(save_path, img)
        messagebox.showinfo("Success", "Message encrypted and saved successfully!")

# GUI Setup
root = tk.Tk()
root.title("Image Steganography - Encryption")
root.geometry("400x300")

# Labels
tk.Label(root, text="Enter Secret Message:").pack(pady=5)
text_entry = tk.Text(root, height=3, width=40)
text_entry.pack(pady=5)

tk.Label(root, text="Enter Passcode:").pack(pady=5)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

# Encrypt Button
encrypt_button = tk.Button(root, text="Select Image & Encrypt", command=encrypt_message)
encrypt_button.pack(pady=10)

root.mainloop()
