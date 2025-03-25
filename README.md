# Vigenère Cipher CLI Tool

## Overview

This project implements a command-line interface (CLI) for encrypting and decrypting messages using the Vigenère cipher. It supports logging all activities and maintains a history of encrypted/decrypted strings. The system is split across three files, each with a specific role, and communicates via subprocesses.

---

## Files and Their Roles

- **driver.py**  
  The main file that users interact with. It handles user input, manages communication with the logger and encryptor subprocesses, and maintains command and result history.

- **encryptor.py**  
  Processes ENCRYPT, DECRYPT, and PASSKEY commands from standard input using the Vigenère cipher. Responds with encrypted or decrypted text.

- **logger.py**  
  Logs commands and events to a specified log file, each with a timestamp and action label. Runs as a separate subprocess from the driver.

---

## How to Run

1. Make sure you have Python 3 installed.

2. Run the driver with a log file as an argument:

 python3 driver.py logfile.txt

3. Available Commands (typed into the CLI):
- `password` – Set the passkey for encryption/decryption.
- `encrypt <text>` – Encrypt the provided text.
- `encrypt` – Prompt to enter text to encrypt.
- `decrypt` – Decrypt using a new string or select one from encryption history.
- `history` – View all user command and result history.
- `quit` – Exit the program and shut down logger/encryptor subprocesses.

---