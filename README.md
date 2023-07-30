**Project Description**:
This project is a simple and secure password manager named "PassManager", created using Python and the Tkinter library for the GUI. The application allows users to store their passwords and validate them. All passwords stored are hashed using bcrypt, providing an added layer of security.

**How to Run**:
1. Install Python
2. Install required libraries using pip
   pip install tkinter
   pip install bcrypt

3. Save the script to preferred locatio
4. Open a terminal/command prompt, navigate to the directory where you saved the script, and run the script with Python:
python passmanager.py

**Usage**:
When the application starts, you'll see a simple user interface with a few fields to input data:

Master Password: This field requires the master password, which for the sake of this project is hardcoded as "keem".
Site Name: Enter the site for which you want to store or verify the password.
Password: Enter the password that you wish to store or verify.
The buttons provided have the following functionality:

Store Password: Stores the password provided in the password field for the given site. The password is hashed before storing. The password must be at least 8 characters long and contain both letters and numbers.
Verify Password: Verifies the password provided against the stored hashed password for the given site.
If the input is incorrect or doesn't follow the criteria, appropriate error messages are displayed. Similarly, success messages are displayed when passwords are successfully stored or verified.

**Important Note**:
This is a basic password manager and is intended to be a coding project for learning purposes. It doesn't persist stored passwords between sessions, and it doesn't implement all the features and security measures you would expect from a production-ready password manager. Always use a reliable and tested password manager for real-world usage.

**License**:
This project is open-source, feel free to use it, modify it, or distribute it as you wish. However, no warranty is provided.
