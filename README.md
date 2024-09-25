# Password-Manager-Python
Password Manager 🔒
This project implements a Password Manager that uses the Fernet class from the cryptography module to encrypt and decrypt user passwords. It allows users to securely store account passwords and retrieve them when needed, ensuring a safe and user-friendly experience.

🛠️ My Approach
The Password Manager is designed with a focus on security and simplicity. By utilizing Fernet encryption from the cryptography library, passwords are stored in an encrypted format, making them unreadable without the correct decryption key. The application offers two primary functions:

Adding new passwords
Viewing stored passwords
🔑 Key Features
Encryption with Fernet:
The application generates a secure encryption key using Fernet.generate_key(), which is saved in a file called key.key. This key is used for both encrypting and decrypting passwords, ensuring their security.

Password Storage:
Usernames and encrypted passwords are stored in a plain text file named password.text, with each entry formatted as:

User Input:
The application interactively allows users to choose whether they want to add new passwords or view existing ones.

🚀 How It Works
The program consists of several key functions:

write_key(): Generates and writes the encryption key to a file.
load_key(): Loads the encryption key from the file.
add(): Encrypts a password and stores it in password.text.
view(): Decrypts stored passwords and displays them to the user.
