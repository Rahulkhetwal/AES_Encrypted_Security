# Password Manager

A simple yet secure **Password Manager** application built using Python. This project allows users to store, retrieve, and manage their passwords efficiently, with all sensitive data encrypted using **AES-256 encryption** for maximum security.
The application includes an additional layer of security by requiring a Secret Key for retrieving credentials, with a 15-second timer to ensure timely authentication.

---

## 🔒 **Key Features**
- **Store Credentials**: Save website credentials (username and password) securely.
- **Retrieve Credentials**: Access your stored credentials with an additional secret key validation.
- **Secret Key Authentication**: A secret key is required to retrieve credentials, adding an extra layer of security.
- **Time-Bound Authentication**: A 15-second countdown timer ensures that the secret key is entered within the time limit.
- **Secure Encryption**: Implements AES-256 encryption to protect your passwords.
- **User-Friendly Interface**: Simple terminal-based interaction for easy use.

---

## 🛠️ **Technologies Used**
- **Python**: Core programming language.
- **PyCryptodome**: Library used for AES encryption and decryption.
- **JSON**: File-based storage for encrypted data.
- **Threading**: For implementing the 15-second countdown timer during authentication.

---

## ⚙️ **Installation and Setup**
1. **Clone the Repository**:
   ```bash
   git clone <your-repo-url>
   cd AESPASSMANAGER2

2. **Install Dependencies**: 
   Ensure Python 3.x is installed.   Then,install the required library:
   ```bash
   pip install pycryptodome

3. **Run the Application**: 
   Start the program by running:
   ```bash
   python main.py


🖥️ How to Use

1.Save a Password:

    Choose the "Store a new credential" option from the menu.
    Enter the website name, username, and password to store.

2.Retrieve a Password:

    Choose the "Retrieve stored credential" option.
    Enter the website name to view its saved credentials.
    You will be prompted to enter a Secret Key.
    You have 15 seconds to enter the correct key, or the program will exit.

3.Exit:

    Select "Exit" from the menu to close the application.


📂 Project Structure

AESPASSMANAGER2/

├── main.py               # Main script for user interaction
├── utils/
│   ├── encryption.py     # Encryption and decryption logic
│   └── storage.py        # Handles storing and retrieving credentials
├── credentials.json      # Encrypted password storage
├── README.md             # Project documentation


💻 Example Interaction

## Saving a Password:
Password Manager
1. Store a new credential
2. Retrieve stored credentials
3. Exit
Enter your choice: 1
Enter website: example.com
Enter username: user123
Enter password: pass@123
Credential stored successfully!

## Retrieving a Password:
Password Manager
1. Store a new credential
2. Retrieve stored credentials
3. Exit
Enter your choice: 2
Enter website: example.com

Enter the Secret Key for credential access (You have 15 seconds):
Enter Secret Key: alexa123

Stored Credentials:
Website: example.com
Username: user123
Password: pass@123

🔐 Security Details

#Encryption: All passwords are encrypted using AES-256 before being stored.

#Decryption: Passwords are decrypted only when retrieved by the user after successful authentication.

#Authentication: A secret key is required to access the stored credentials. The key must be entered within 15 seconds, or the program will automatically exit.

#Storage: Encrypted credentials are stored in credentials.json.



🚀 Future Enhancements

1.Add a graphical user interface (GUI) for better usability.
2.Implement a Master Password for accessing the password manager.
3.Support export and import of credentials.
4.Enable password strength analysis during creation.
5.Implement multi-factor authentication for an added layer of security.

📄 License

This project is developed as part of an academic minor project and is for educational purposes only.

👨‍💻 Contributors
[Rahul Khetwal]
Feel free to contribute by submitting issues or pull requests!


