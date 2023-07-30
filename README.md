# PassManager
This repository contains the source code for a simple Password Manager application built using Python. The application allows users to securely store, generate, view, delete, import, and export passwords.

**Features**
Store passwords for various sites or applications.
Generate strong, random passwords with a single click.
View all stored passwords.
Delete passwords when no longer needed.
Export passwords to a text or rich text file.
Import passwords from a text or rich text file.
Tech Stack
The Password Manager application is built using the following Python modules:

**Tkinter** for the graphical user interface.
**Cryptography.Fernet** for password encryption and decryption.
**Json** for exporting and importing passwords.
**Random** and **String** for generating random passwords.
**Base64** for encoding encrypted passwords for JSON storage.

**Usage**
To run the program, execute the main python script as below:

bash
python password_manager.py
This will launch a GUI application. Here's how to use its features:

**Store Passwords:**
Enter the master password (currently set as "keem" within the script), the site name, and the site password. Click "Store Password" to save the password. The password should be at least 8 characters long and contain both numbers and letters.

**Generate Passwords:**
Enter the master password and the site name. Click "Generate Password" to generate a strong, random password. The generated password will be shown in the password field. Click "Store Password" to save the generated password.

**View Passwords:**
Enter the master password and click "View Passwords" to view all stored passwords.

**Delete Passwords:**
Enter the master password, select a site from the list box, and click "Delete Password" to delete a password.

**Export Passwords:**
Enter the master password and click "Export Passwords" to save all passwords to a file. Choose a file location and name in the file dialog.

**Import Passwords:**
Enter the master password and click "Import Passwords" to load passwords from a file. Choose a file in the file dialog.

**Security**
Passwords are stored in memory and are encrypted using symmetric key cryptography. The key is generated each time the application is started and is not saved anywhere. The encryption and decryption is handled by the Cryptography.Fernet module.

 **Note**: this application is a simple example and may not meet all requirements for secure password storage, such as securely handling the master password or storing the passwords when the application is not running. For real-world use, you would want to consider additional security measures.

**Contributing**
Please feel free to fork this repository and submit pull requests for any features or improvements you wish to contribute. You can also open an issue if you find any bugs or have suggestions for improvements.

**License**
This project is released under the MIT License.

**Disclaimer**
This project is intended for educational purposes only. It is not secure enough for real-world, professional use without further improvements. Use it at your own risk.
