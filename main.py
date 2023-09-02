import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from cryptography.fernet import Fernet

# Generate a random encryption key
encryption_key = Fernet.generate_key()
fernet = Fernet(encryption_key)

def delete_files():
    files_to_delete = file_list.get(1.0, "end-1c").split("\n")
    try:
        for file in files_to_delete:
            if os.path.exists(file):
                os.remove(file)
                result_text.config(text=f"Deleted {file}", fg="green")
            else:
                result_text.config(text=f"{file} not found.", fg="red")
    except Exception as e:
        result_text.config(text=f"An error occurred: {e}", fg="red")

def clear_file_list():
    file_list.delete(1.0, "end")

def browse_files():
    clear_file_list()  # Clear the file list before adding new files
    file_paths = filedialog.askopenfilenames()
    for file_path in file_paths:
        file_list.insert("end", file_path)

def encrypt_file():
    file_to_encrypt = file_list.get(1.0, "end-1c").strip()
    try:
        with open(file_to_encrypt, "rb") as f:
            file_data = f.read()
        encrypted_data = fernet.encrypt(file_data)
        
        encrypted_file = file_to_encrypt + ".enc"
        with open(encrypted_file, "wb") as f:
            f.write(encrypted_data)

        # Delete the original file
        os.remove(file_to_encrypt)

        result_text.config(text=f"Encrypted and deleted {file_to_encrypt}", fg="green")
    except Exception as e:
        result_text.config(text=f"An error occurred: {e}", fg="red")

def decrypt_file():
    file_to_decrypt = file_list.get(1.0, "end-1c").strip()
    try:
        with open(file_to_decrypt, "rb") as f:
            file_data = f.read()
        decrypted_data = fernet.decrypt(file_data)
        
        decrypted_file = file_to_decrypt.replace(".enc", "")
        with open(decrypted_file, "wb") as f:
            f.write(decrypted_data)

        result_text.config(text=f"Decrypted {file_to_decrypt} to {decrypted_file}", fg="green")
    except Exception as e:
        result_text.config(text=f"An error occurred: {e}", fg="red")

def clear_files():
    file_list.delete(1.0, "end")
    result_text.config(text="Cleared file list", fg="blue")

def toggle_dark_mode():
    dark_mode = dark_mode_var.get()
    if dark_mode:
        # Dark mode colors
        app.configure(bg="#1e1e1e")
        file_label.configure(bg="#1e1e1e", fg="white")
        file_list.configure(bg="#333333", fg="white", insertbackground="white")
        result_text.configure(bg="#1e1e1e", fg="green")
        
        # Configure the style for dark mode with black text
        dark_style = ttk.Style()
        dark_style.configure("Dark.TButton", padding=10, font=("Arial", 12), foreground="black")
        browse_button.configure(style="Dark.TButton")  # Apply the style to the button
        encrypt_button.configure(style="Dark.TButton")  # Apply the style to the button
        decrypt_button.configure(style="Dark.TButton")  # Apply the style to the button
        delete_button.configure(style="Dark.TButton")  # Apply the style to the button
        clear_button.configure(style="Dark.TButton")  # Apply the style to the button
    else:
        # Light mode colors
        app.configure(bg="white")
        file_label.configure(bg="white", fg="black")
        file_list.configure(bg="white", fg="black", insertbackground="black")
        result_text.configure(bg="white", fg="green")
        
        # Reset the style to default for light mode
        light_style = ttk.Style()
        light_style.configure("TButton", padding=10, font=("Arial", 12))
        browse_button.configure(style="TButton")  # Apply the default style to the button
        encrypt_button.configure(style="TButton")  # Apply the default style to the button
        decrypt_button.configure(style="TButton")  # Apply the default style to the button
        delete_button.configure(style="TButton")  # Apply the default style to the button
        clear_button.configure(style="TButton")  # Apply the default style to the button



# Create the main window
app = tk.Tk()
app.title("FileCloak")
app.geometry("600x500")  # Set initial window size

# Create style for buttons
style = ttk.Style()

# Dark mode style
style.configure("Dark.TButton", padding=10, font=("Arial", 12), foreground="white", background="#333333")

# Light mode style
style.configure("TButton", padding=10, font=("Arial", 12))

# Dark mode variable
dark_mode_var = tk.BooleanVar(value=False)

# Create widgets
file_label = tk.Label(app, text="Select files:")
file_list = tk.Text(app, height=12, width=50)
browse_button = ttk.Button(app, text="Browse", command=browse_files)
encrypt_button = ttk.Button(app, text="Encrypt File", command=encrypt_file)
decrypt_button = ttk.Button(app, text="Decrypt File", command=decrypt_file)
delete_button = ttk.Button(app, text="Delete Files", command=delete_files)
clear_button = ttk.Button(app, text="Clear List", command=clear_files)
result_text = tk.Label(app, text="", fg="green", anchor="w")
dark_mode_checkbox = ttk.Checkbutton(app, text="Dark Mode", variable=dark_mode_var, command=toggle_dark_mode)

# Place widgets using grid layout
file_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
file_list.grid(row=1, column=0, padx=10, pady=10, columnspan=2, rowspan=6, sticky="nsew")
browse_button.grid(row=14, column=0, padx=10, pady=10, sticky="w")
encrypt_button.grid(row=15, column=0, padx=10, pady=10, sticky="w")
decrypt_button.grid(row=16, column=0, padx=10, pady=10, sticky="w")
delete_button.grid(row=17, column=0, padx=10, pady=10, sticky="w")
clear_button.grid(row=18, column=0, padx=10, pady=10, sticky="w")
result_text.grid(row=19, column=0, columnspan=2, padx=10, pady=10, sticky="w")
dark_mode_checkbox.grid(row=20, column=0, columnspan=2, padx=10, pady=10, sticky="w")

# Configure grid rows and columns
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# Start the application
app.mainloop()
