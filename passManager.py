# Import required libraries
from tkinter import *
from tkinter import messagebox
import bcrypt

# Initialize the main Tkinter window
root = Tk()

# Title for our window
root.title("PassManager")

# Defining the master password
master_password = "keem"

# Creating a dictionary to store the site names and passwords
passwords = {}

# This function is used to hash the user's passwords
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

# This function checks if the provided password matches the stored password
def check_password(site, password):
    hashed_password = passwords[site]
    if bcrypt.checkpw(password.encode(), hashed_password):
        return True
    else:
        return False

# This function checks the strength of the user's password
def check_password_strength(password):
    has_number = False
    has_letter = False

    for char in password:
        if char.isdigit():
            has_number = True
        if char.isalpha():
            has_letter = True

    if len(password) < 8 or not has_number or not has_letter:
        return False
    else:
        return True

# Creating the master password entry box
master_password_label = Label(root, text="Master Password:")
master_password_label.grid(row=0, column=0)

master_password_entry = Entry(root)
master_password_entry.grid(row=0, column=1)

# Creating the site name entry box
site_label = Label(root, text="Site Name:")
site_label.grid(row=1, column=0)

site_entry = Entry(root)
site_entry.grid(row=1, column=1)

# Displaying the password requirements
requirements = Label(root, text="Password Requirements: At least 8 characters, contains letters and numbers.")
requirements.grid(row=2, column=0, columnspan=2)

# Creating the password entry box
password_label = Label(root, text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(root)
password_entry.grid(row=3, column=1)

# This function is used to store the user's password when the button is pressed
def store_password():
    master = master_password_entry.get()
    site = site_entry.get()
    password = password_entry.get()

    # Check if the master password is correct
    if master != master_password:
        messagebox.showerror("Error", "Invalid master password!")
        return

    # Check if the password is strong enough
    if not check_password_strength(password):
        messagebox.showerror("Error", "Password does not meet requirements.")
        return

    # If it is, we hash the password
    hashed_password = hash_password(password)

    # Store the hashed password in our dictionary
    passwords[site] = hashed_password

    # Clear all the entry boxes
    master_password_entry.delete(0, 'end')
    site_entry.delete(0, 'end')
    password_entry.delete(0, 'end')

    # Show a success message to the user
    messagebox.showinfo("Success", "Password stored successfully!")

# This function is used to verify the user's password when the button is pressed
def verify_password():
    master = master_password_entry.get()
    site = site_entry.get()
    password = password_entry.get()

    # Check if the master password is correct
    if master != master_password:
        messagebox.showerror("Error", "Invalid master password!")
        return

    # Check if the site exists in the password dictionary
    if site not in passwords:
        messagebox.showerror("Error", "No password stored for this site!")
        return

    # Check if the provided password matches the stored password
    if check_password(site, password):
        messagebox.showinfo("Success", "Password verified successfully!")
    else:
        messagebox.showerror("Error", "Password does not match the stored password!")

    # Clear all the entry boxes
    master_password_entry.delete(0, 'end')
    site_entry.delete(0, 'end')
    password_entry.delete(0, 'end')

# Creating the button to store the password
store_button = Button(root, text="Store Password", command=store_password)
store_button.grid(row=4, column=1)

# Creating the button to verify the password
verify_button = Button(root, text="Verify Password", command=verify_password)
verify_button.grid(row=5, column=1)


# Running the Tkinter event loop
root.mainloop()