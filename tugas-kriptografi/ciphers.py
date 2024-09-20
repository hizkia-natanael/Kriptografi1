import tkinter as tk
from tkinter import filedialog, messagebox

# Vigenere Cipher (tanpa menggunakan library eksternal)
def clean_text(text):
    return ''.join(filter(str.isalpha, text)).upper()

def vigenere_encrypt(plaintext, key):
    plaintext = clean_text(plaintext)
    key = clean_text(key)
    cipher = ''
    key_len = len(key)
    
    for i in range(len(plaintext)):
        cipher += chr(((ord(plaintext[i]) - 65) + (ord(key[i % key_len]) - 65)) % 26 + 65)
    return cipher

def vigenere_decrypt(ciphertext, key):
    ciphertext = clean_text(ciphertext)
    key = clean_text(key)
    plain = ''
    key_len = len(key)
    
    for i in range(len(ciphertext)):
        plain += chr(((ord(ciphertext[i]) - 65) - (ord(key[i % key_len]) - 65)) % 26 + 65)
    return plain

# Playfair Cipher (tanpa menggunakan library eksternal)
def generate_playfair_matrix(key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x))).replace("J", "I").upper()
    matrix = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    for letter in key:
        if letter not in matrix:
            matrix.append(letter)
    for letter in alphabet:
        if letter not in matrix:
            matrix.append(letter)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def playfair_encrypt(plaintext, key):
    plaintext = clean_text(plaintext)
    key_matrix = generate_playfair_matrix(key)
    return plaintext  

def playfair_decrypt(ciphertext, key):
    ciphertext = clean_text(ciphertext)
    key_matrix = generate_playfair_matrix(key)
    return ciphertext  

# Hill Cipher (tanpa menggunakan library eksternal)
def hill_encrypt(plaintext, key_matrix):
    return plaintext 

def hill_decrypt(ciphertext, key_matrix):
    return ciphertext 

# Mengaplikasikan GUI
def encrypt_text():
    message = input_text.get("1.0", "end-1c")
    key = key_input.get()
    cipher_type = cipher_option.get()

    if len(key) < 12:
        messagebox.showerror("Error", "Kunci harus memiliki minimal 12 karakter!")
        return

    if cipher_type == "Vigenere":
        result = vigenere_encrypt(message, key)
    elif cipher_type == "Playfair":
        result = playfair_encrypt(message, key)
    elif cipher_type == "Hill":
        result = hill_encrypt(message, key)  # Key matrix is not implemented yet
    else:
        result = "Invalid Cipher"

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

def decrypt_text():
    message = input_text.get("1.0", "end-1c")
    key = key_input.get()
    cipher_type = cipher_option.get()

    if len(key) < 12:
        messagebox.showerror("Error", "Kunci harus memiliki minimal 12 karakter!")
        return

    if cipher_type == "Vigenere":
        result = vigenere_decrypt(message, key)
    elif cipher_type == "Playfair":
        result = playfair_decrypt(message, key)
    elif cipher_type == "Hill":
        result = hill_decrypt(message, key)  # Key matrix is not implemented yet
    else:
        result = "Invalid Cipher"

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            input_text.delete("1.0", tk.END)
            input_text.insert(tk.END, file.read())

# Aplikasi Utama
root = tk.Tk()
root.title("Cryptography Program")

cipher_option = tk.StringVar(value="Vigenere")

# Area Input Teks
tk.Label(root, text="Input Text:").grid(row=0, column=0)
input_text = tk.Text(root, height=10, width=40)
input_text.grid(row=1, column=0, columnspan=2)

# Area Output Teks
tk.Label(root, text="Output Text:").grid(row=0, column=2)
output_text = tk.Text(root, height=10, width=40)
output_text.grid(row=1, column=2, columnspan=2)

# Input Kunci
tk.Label(root, text="Key:").grid(row=2, column=0)
key_input = tk.Entry(root, width=40)
key_input.grid(row=2, column=1)

# Menu Pilihan Sandi
tk.Label(root, text="Cipher:").grid(row=2, column=2)
cipher_menu = tk.OptionMenu(root, cipher_option, "Vigenere", "Playfair", "Hill")
cipher_menu.grid(row=2, column=3)

# Tombol tombol
tk.Button(root, text="Enkripsi", command=encrypt_text).grid(row=3, column=0)
tk.Button(root, text="Deskripsi", command=decrypt_text).grid(row=3, column=1)
tk.Button(root, text="Buka File", command=open_file).grid(row=3, column=2)

root.mainloop()
