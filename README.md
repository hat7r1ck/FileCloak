# FileCloak
FileCloak is a simple file encryption and decryption tool built using Python and the Tkinter library. It allows you to secure your files by encrypting them using the Fernet symmetric encryption algorithm. You can also decrypt and delete files securely.

![Screenshot 2023-09-02 083923](https://github.com/hat7r1ck/FileCloak/assets/110708720/718fb484-765c-4b79-b5d9-19b36efdade7)

## Features

- Encrypt files to keep them secure.
- Decrypt encrypted files when you need to access them.
- Securely delete files, making them unrecoverable.
- Dark mode for ease of use.

## How It Works

FileCloak uses the Fernet symmetric encryption algorithm, which requires a secret encryption key to encrypt and decrypt files. Here's how the program handles the encryption key:

1. When you first run the program, it checks if an encryption key file (`key.key`) exists in the program's directory.
2. If the key file exists, the program loads the encryption key from the file.
3. If the key file doesn't exist, FileCloak generates a random encryption key, saves it to `key.key`, and uses it for encryption and decryption.

This approach ensures that you can use the same encryption key across multiple sessions of the program, so you don't have to remember it or input it each time.

## Getting Started

1. Clone or download this repository to your local machine.

2. Make sure you have Python installed. FileCloak is compatible with Python 3.6 and above.

3. Install the required Python packages using pip:

- Python 3.7 or higher installed on your system.
- cryptography
- tkinter

4. Run the program:

5. Use the program to browse, encrypt, decrypt, and delete files securely.

## Usage

1. **Browse for Files**: Click the "Browse" button to select files you want to operate on.

2. **Encrypt Files**: After selecting files, click the "Encrypt File" button to encrypt them. The original files will be deleted securely.

3. **Decrypt Files**: To decrypt previously encrypted files, click the "Decrypt File" button. Decrypted files will be saved without the ".enc" extension.

4. **Delete Files**: To securely delete files without encryption, click the "Delete Files" button. Deleted files are unrecoverable.

5. **Clear List**: Click the "Clear List" button to clear the file list.

6. **Dark Mode**: Toggle the "Dark Mode" checkbox for a dark-themed user interface.

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, please create an issue or submit a pull request.

