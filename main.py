from utils.encryption import EncryptionManager
from utils.storage import StorageManager
import threading
import time
import sys

SECRET_KEY = "alexa123"
auth_successful = False

def countdown_timer():
    global auth_successful
    for remaining in range(15, 0, -1):
        if auth_successful:
            return
        print(f"Time left: {remaining} seconds", end="\r", flush=True)
        time.sleep(1)
    if not auth_successful:
        print("\nTime is up! Exiting the application.")
        sys.exit()

def authenticate():
    global auth_successful
    print("Enter the Secret Key for credential access (You have 15 seconds):")
    timer_thread = threading.Thread(target=countdown_timer)
    timer_thread.start()
    input_key = input("\nEnter Secret Key: ")
    if input_key == SECRET_KEY:
        auth_successful = True
        print("Authentication successful!")
        return True
    print("Authentication failed. Access denied.")
    return False

def main():
    print("Password Manager")
    print("================")
    print("1. Store a new credential")
    print("2. Retrieve stored credentials")
    print("3. Exit")

    choice = input("Enter your choice: ")
    storage = StorageManager()

    if choice == "1":
        website = input("Enter the website: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        encrypted_username = EncryptionManager.encrypt(username)
        encrypted_password = EncryptionManager.encrypt(password)
        storage.store_credential(website, encrypted_username, encrypted_password)
        print("Credential stored successfully!")
    elif choice == "2":
        if authenticate():
            credentials = storage.retrieve_credentials()
            print("\nStored Credentials:")
            for website, creds in credentials.items():
                decrypted_username = EncryptionManager.decrypt(creds['username'])
                decrypted_password = EncryptionManager.decrypt(creds['password'])
                print(f"Website: {website}")
                print(f"Username: {decrypted_username}")
                print(f"Password: {decrypted_password}")
                print("-" * 30)
    elif choice == "3":
        print("Exiting Password Manager. Goodbye!")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
