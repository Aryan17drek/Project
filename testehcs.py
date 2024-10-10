import tkinter as tk
from tkinter import messagebox
from tkinter import font

def decode_caesar_cipher(cipher_text, shift):
    decoded_text = []
    
    for char in cipher_text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            decoded_char = chr((ord(char) - base - shift + 26) % 26 + base)
            decoded_text.append(decoded_char)
        else:
            decoded_text.append(char)
    
    return ''.join(decoded_text)

def decode():
    cipher_text = entry_cipher.get()
    
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number for the shift.")
        return
    
    if not cipher_text:
        messagebox.showwarning("Input Error", "Please enter the ciphertext.")
        return
    
    if shift == 0:
        # Brute-force option
        result_text = ""
        for shift in range(1, 26):
            result_text += f"Shift {shift}: {decode_caesar_cipher(cipher_text, shift)}\n"
        result_label.config(text=result_text)
    else:
        decoded_text = decode_caesar_cipher(cipher_text, shift)
        result_label.config(text=f"Decoded text: {decoded_text}")

# Initialize the GUI window
window = tk.Tk()
window.title("Caesar Cipher Decoder")
window.geometry("800x600")
window.configure(bg="#2c3e50")

# Custom font
title_font = font.Font(family="Helvetica", size=24, weight="bold")
label_font = font.Font(family="Helvetica", size=14)
output_font = font.Font(family="Helvetica", size=18, weight="bold")  # Larger and bolder font for output

# Title label
title_label = tk.Label(window, text="Caesar Cipher Decoder", font=title_font, fg="#ecf0f1", bg="#2c3e50")
title_label.pack(pady=30)

# Instruction label
instructions = tk.Label(window, text="Enter your ciphertext and the shift value (or 0 for brute-force).", font=label_font, fg="#bdc3c7", bg="#2c3e50")
instructions.pack(pady=10)

# Frame for input fields
input_frame = tk.Frame(window, bg="#34495e", padx=20, pady=20)
input_frame.pack(pady=20)

# Ciphertext input
tk.Label(input_frame, text="Ciphertext:", font=label_font, fg="#ecf0f1", bg="#34495e").grid(row=0, column=0, sticky="w", pady=10)
entry_cipher = tk.Entry(input_frame, width=60, font=label_font)
entry_cipher.grid(row=0, column=1, pady=10)

# Shift value input
tk.Label(input_frame, text="Shift Value (0 for brute-force):", font=label_font, fg="#ecf0f1", bg="#34495e").grid(row=1, column=0, sticky="w", pady=10)
shift_entry = tk.Entry(input_frame, width=10, font=label_font)
shift_entry.grid(row=1, column=1, pady=10, sticky="w")

# Decode button
decode_button = tk.Button(window, text="Decode", command=decode, bg="#e74c3c", fg="white", font=label_font, padx=30, pady=10)
decode_button.pack(pady=30)

# Result label with enhanced styling
result_label = tk.Label(window, text="", wraplength=700, justify="left", font=output_font, fg="#2ecc71", bg="#34495e", padx=20, pady=20, borderwidth=2, relief="solid")
result_label.pack(pady=20)

# Footer label
footer_label = tk.Label(window, text="Developed by Kumar Aryan | Powered by Python & Tkinter", font=("Helvetica", 12), fg="#95a5a6", bg="#2c3e50")
footer_label.pack(side="bottom", pady=20)

# Run the GUI loop
window.mainloop()



