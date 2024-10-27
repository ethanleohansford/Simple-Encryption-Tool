from cryptography.fernet import Fernet
import os

class SimpleEncryptionTool:
    def __init__(self):
        # Generate a key for encryption and decryption
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        print("Encryption key generated. Keep it safe!")

    def save_key(self, filename):
        """Save the encryption key to a file."""
        with open(filename, 'wb') as key_file:
            key_file.write(self.key)
        print(f"Key saved to {filename}")

    def load_key(self, filename):
        """Load the encryption key from a file."""
        if os.path.exists(filename):
            with open(filename, 'rb') as key_file:
                self.key = key_file.read()
                self.cipher = Fernet(self.key)
            print(f"Key loaded from {filename}")
        else:
            print(f"Key file {filename} does not exist.")

    def encrypt(self, plaintext):
        """Encrypt the provided plaintext."""
        encrypted = self.cipher.encrypt(plaintext.encode())
        return encrypted

    def decrypt(self, encrypted_text):
        """Decrypt the provided encrypted text."""
        decrypted = self.cipher.decrypt(encrypted_text).decode()
        return decrypted

def main():
    tool = SimpleEncryptionTool()

    while True:
        choice = input("\nChoose an option:\n1. Encrypt\n2. Decrypt\n3. Save Key\n4. Load Key\n5. Exit\nEnter your choice: ")

        if choice == '1':
            plaintext = input("Enter the text to encrypt: ")
            encrypted_text = tool.encrypt(plaintext)
            print(f"Encrypted text: {encrypted_text}")

        elif choice == '2':
            encrypted_text = input("Enter the encrypted text: ")
            decrypted_text = tool.decrypt(encrypted_text.encode())
            print(f"Decrypted text: {decrypted_text}")

        elif choice == '3':
            filename = input("Enter the filename to save the key: ")
            tool.save_key(filename)

        elif choice == '4':
            filename = input("Enter the filename to load the key: ")
            tool.load_key(filename)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
