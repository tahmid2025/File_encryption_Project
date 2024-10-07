# All the libaries that will be used
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os
import random
import string

# This is a function to generate my Encryption key
def encryption_key(length=6):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


#This is used to encrypt a file
def encrypt_file(file_path):
    key = encryption_key()  # Generates a random encryption key
    with open(file_path, 'rb') as file:
        file_data = file.read()  # Reads the file content
    encrypted_data = bytearray(file_data)
    for i in range(len(encrypted_data)):
        encrypted_data[i] ^= ord(key[i % len(key)])  # XOR operation is perofromed for each byte with the key
    enc_file_path = os.path.join(os.path.dirname(file_path), f"enc_{os.path.basename(file_path)}")
    with open(enc_file_path, 'wb') as enc_file:
        enc_file.write(encrypted_data)  # Writes the encrypted data to a new file
    messagebox.showinfo("Encryption Key", f"Your encryption key is: {key}\nPlease copy and save it securely.")
    return key

# This is used to decrypt files
def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()  # Reads the encrypted file content
    decrypted_data = bytearray(encrypted_data)
    for i in range(len(decrypted_data)):
        decrypted_data[i] ^= ord(key[i % len(key)])  # XOR operation is peroformed for each byte with the key
    dec_file_path = os.path.join(os.path.dirname(file_path), f"dec_{os.path.basename(file_path)}")
    with open(dec_file_path, 'wb') as dec_file:
        dec_file.write(decrypted_data)  # Writes the decrypted data to a new file
    messagebox.showinfo("Decryption", "File decrypted successfully!")


#----------------------------GUI---------------------------------------#
#What the Encrypt button does
def encrypt_button_action():
    file_path = filedialog.askopenfilename()  # Opens the file dialog to select a file
    if file_path:
        encrypt_file(file_path)  # Encrypts the selected file

# What the Decrypt button does
def decrypt_button_action():
    file_path = filedialog.askopenfilename()  # Opens file dialog to select a file
    if file_path:
        key = simpledialog.askstring("Input", "Enter the decryption key:")  # Asks for the decryption key
        if key:
            try:
                decrypt_file(file_path, key)  # Decrypts the selected file
            except Exception as e:
                messagebox.showerror("Error", "Invalid key or corrupted file.")  # Shosw error if decryption fails

# Main GUI setup
root = tk.Tk()
root.title("File Encryption/Decryption")

# Encrypt button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_button_action)
encrypt_button.pack(pady=10)

# Decrypt button
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_button_action)
decrypt_button.pack(pady=10)

root.mainloop()  # Runs the GUI event loop
    

