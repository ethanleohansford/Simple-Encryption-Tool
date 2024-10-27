# Simple Encryption Tool

A simple encryption tool implemented in Python that uses the `cryptography` library for encrypting and decrypting text. This tool allows you to securely store sensitive information.

## Features
- Generate a secure encryption key.
- Encrypt and decrypt messages.
- Save and load the encryption key from a file.

## Technologies Used
- **Python**
- **Cryptography Library**: Provides secure encryption methods.

## Requirements
- **Python 3.6+**
- **cryptography** library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Simple-Encryption-Tool.git
   cd Simple-Encryption-Tool
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the encryption tool:**
  ```bash
  python encryptor.py
  ```
  This will start the tool and display a menu of options.
2. **Choose an option:**
- Encrypt: Enter the text to encrypt.
- Decrypt: Enter the encrypted text to decrypt.
- Save Key: Save the generated encryption key to a file.
- Load Key: Load an encryption key from a file.
- Exit: Exit the tool.

## Example

- Encrypting a message:
  ```vbnet
  Enter the text to encrypt: Hello, World!
  Encrypted text: gAAAAABg...
  ```
- Decrypting a message:
  ```arduino
  Enter the encrypted text: gAAAAABg...
  Decrypted text: Hello, World!
  ```
## Limitations

- This tool is a basic implementation and is intended for educational purposes. For production use, consider additional security measures.
Contributing

Contributions are welcome! Feel free to submit issues or pull requests for enhancements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Conclusion
This simple encryption tool demonstrates how to use basic cryptographic techniques to secure data. You can enhance it by adding features like password protection for the key or implementing a GUI for better user interaction. In future i will add further modifications or additional features!
