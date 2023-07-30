import json
import base64
import ssl
import random
import string
from tkinter import *
from tkinter import messagebox, filedialog
from cryptography.fernet import Fernet

# Disable SSL certificate verification temporarily
ssl._create_default_https_context = ssl._create_unverified_context

class PasswordManager:
    def __init__(self):
        self.master_password = "keem"
        self.key = Fernet.generate_key()
        self.passwords = {}
        #window
        self.root = Tk()
        self.root.title("Password Manager")

        #master password
        self.master_password_label = Label(self.root, text="Master Password:")
        self.master_password_label.grid(row=0, column=0)
        self.master_password_entry = Entry(self.root, show="*")
        self.master_password_entry.grid(row=0, column=1)

        #password entry
        self.site_label = Label(self.root, text="Site Name:")
        self.site_label.grid(row=1, column=0)
        self.site_entry = Entry(self.root)
        self.site_entry.grid(row=1, column=1)
        self.requirements = Label(self.root, text="Password Requirements: At least 8 characters, contains letters and numbers.")
        self.requirements.grid(row=2, column=0, columnspan=2)
        self.password_label = Label(self.root, text="Password:")
        self.password_label.grid(row=3, column=0)
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.grid(row=3, column=1)

        #options
        self.generate_button = Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=4, column=1, padx=10, pady=5)
        self.store_button = Button(self.root, text="Store Password", command=self.store_password)
        self.store_button.grid(row=5, column=1, padx=10, pady=5)
        self.view_button = Button(self.root, text="View Passwords", command=self.view_passwords)
        self.view_button.grid(row=6, column=1, padx=10, pady=5)
        self.delete_button = Button(self.root, text="Delete Password", command=self.delete_password)
        self.delete_button.grid(row=7, column=1, padx=10, pady=5)
        self.export_button = Button(self.root, text="Export Passwords", command=self.export_passwords)
        self.export_button.grid(row=8, column=1, padx=10, pady=5)
        self.import_button = Button(self.root, text="Import Passwords", command=self.import_passwords)
        self.import_button.grid(row=9, column=1, padx=10, pady=5)

        self.root.mainloop()

    def encrypt_password(self, password):
        f = Fernet(self.key)
        encrypted_password = f.encrypt(password.encode())
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        f = Fernet(self.key)
        decrypted_password = f.decrypt(encrypted_password).decode()
        return decrypted_password

    @staticmethod
    def check_password_strength(password):
        has_number = any(char.isdigit() for char in password)
        has_letter = any(char.isalpha() for char in password)
        if len(password) < 8 or not has_number or not has_letter:
            return False
        else:
            return True

    def store_password(self):
        master = self.master_password_entry.get()
        site = self.site_entry.get()
        password = self.password_entry.get()
        if master != self.master_password:
            messagebox.showerror("Error", "Invalid master password!")
            return
        if not self.check_password_strength(password):
            messagebox.showerror("Error", "Password does not meet requirements.")
            return
        encrypted_password = self.encrypt_password(password)
        self.passwords[site] = encrypted_password
        self.update_password_list()
        self.master_password_entry.delete(0, 'end')
        self.site_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')

    def generate_password(self):
        while True:
            letters = string.ascii_letters
            digits = string.digits
            password = ''.join(random.choice(letters + digits) for i in range(12))
            if self.check_password_strength(password):
                break
        self.password_entry.delete(0, 'end')
        self.password_entry.insert(0, password)

    def view_passwords(self):
        password_list = ""
        for site, encrypted_password in self.passwords.items():
            decrypted_password = self.decrypt_password(encrypted_password)
            password_list += f"Site: {site}\nPassword: {decrypted_password}\n\n"
        if password_list:
            messagebox.showinfo("Stored Passwords", password_list)
        else:
            messagebox.showinfo("Stored Passwords", "No passwords stored.")

    def delete_password(self):
        selected_site = self.password_listbox.get(self.password_listbox.curselection())
        if selected_site:
            del self.passwords[selected_site]
            self.update_password_list()

    def import_passwords(self):
        file_path = filedialog.askopenfilename(filetypes=(("Text Files", "*.txt"), ("Rich Text Files", "*.rtf")))
        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.passwords = json.load(file)
                    # Convert keys back to bytes from Base64 encoded string
                    self.passwords = {site: base64.b64decode(encrypted_password) for site, encrypted_password in self.passwords.items()}
                    self.update_password_list()
            except FileNotFoundError as e:
                messagebox.showerror("Error", f"File not found. Error: {str(e)}")
            except json.JSONDecodeError as e:
                messagebox.showerror("Error", f"Failed to import passwords. Invalid JSON format. Error: {str(e)}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to import passwords! Error: {str(e)}")

    def export_passwords(self):
        file_path = filedialog.asksaveasfilename(filetypes=(("Text Files", "*.txt"), ("Rich Text Files", "*.rtf")))
        if file_path:
            try:
                # Convert keys to Base64 encoded string to store in JSON
                passwords_to_export = {site: base64.b64encode(encrypted_password).decode() for site, encrypted_password in self.passwords.items()}
                with open(file_path, "w") as file:
                    json.dump(passwords_to_export, file)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export passwords! Error: {str(e)}")

    def update_password_list(self):
        self.password_listbox.delete(0, END)
        for site in self.passwords:
            self.password_listbox.insert(END, site)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    password_manager = PasswordManager()
    password_manager.run()
