import cv2
import tkinter as tk
from tkinter import filedialog, messagebox

# Character decoding dictionary
c = {i: chr(i) for i in range(255)}

# Decrypt Function
def decrypt_message():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return
    
    img = cv2.imread(file_path)
    pas = password_entry.get()

    if not pas:
        messagebox.showerror("Error", "Enter the password for decryption!")
        return

    n, m, z = 0, 0, 0
    message = ""
    try:
        for _ in range(1000):  # Arbitrary limit to avoid infinite loops
            message += c[img[n, m, z]]
            n = (n + 1) % img.shape[0]
            m = (m + 1) % img.shape[1]
            z = (z + 1) % 3
    except KeyError:
        pass

    messagebox.showinfo("Decryption", f"Decrypted Message:\n{message}")

# GUI Setup
root = tk.Tk()
root.title("Image Steganography - Decryption")
root.geometry("400x200")

# Labels
tk.Label(root, text="Enter Passcode:").pack(pady=5)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

# Decrypt Button
decrypt_button = tk.Button(root, text="Select Image & Decrypt", command=decrypt_message)
decrypt_button.pack(pady=10)

root.mainloop()
