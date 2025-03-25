import subprocess
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 driver.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]

    # Start logger process
    logger = subprocess.Popen(["python3", "logger.py", log_file], stdin=subprocess.PIPE, text=True)

    # Start encryptor process
    encryptor = subprocess.Popen(["python3", "encryptor.py"],
                                 stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 text=True)

    passkey_set = False
    history = []
    encrypted_history = []

    def log(action, message):
        """Send a log message to the logger process."""
        logger.stdin.write(f"{action} {message}\n")
        logger.stdin.flush()

    log("START", "Driver started.")

    while True:
        cmd = input("Enter command (password/encrypt/decrypt/history/quit): ").strip().lower()
        parts = cmd.split(" ", 1)

        if parts[0] == "password":
            password = input("Enter passkey: ").strip()
            encryptor.stdin.write(f"PASSKEY {password}\n")
            encryptor.stdin.flush()
            result = encryptor.stdout.readline().strip()
            print(result)
            passkey_set = True
            log("PASSWORD", "Passkey set.")

        elif parts[0] == "encrypt":
            if not passkey_set:
                print("ERROR: Passkey not set. Use 'password' command first.")
                continue
            text = parts[1] if len(parts) > 1 else input("Enter text to encrypt: ").strip()
            encryptor.stdin.write(f"ENCRYPT {text}\n")
            encryptor.stdin.flush()
            result = encryptor.stdout.readline().strip()
            print(result)

            # Extract only the result string
            encrypted_text = result.replace("RESULT ", "", 1)

            history.append(f"Encrypted: {text}")
            history.append(f"Result: {encrypted_text}")
            encrypted_history.append(encrypted_text)
            log("ENCRYPT", text)

        elif parts[0] == "decrypt":
            if not passkey_set:
                print("ERROR: Passkey not set. Use 'password' command first.")
                continue

            use_history = input("Use a string from history? (y/n): ").strip().lower()
            if use_history == 'y':
                if not encrypted_history:
                    print("No encrypted strings in history.")
                    continue
                print("Encrypted strings in history:")
                for i, enc in enumerate(encrypted_history, 1):
                    print(f"{i}. {enc}")
                try:
                    choice = int(input("Enter the number of the string to decrypt: "))
                    if 1 <= choice <= len(encrypted_history):
                        text = encrypted_history[choice - 1]
                    else:
                        print("Invalid choice.")
                        continue
                except ValueError:
                    print("Invalid input.")
                    continue
            else:
                text = input("Enter text to decrypt: ").strip()
                history.append(f"Decrypted: {text}")

            encryptor.stdin.write(f"DECRYPT {text}\n")
            encryptor.stdin.flush()
            result = encryptor.stdout.readline().strip()
            print(result)

            # Extract just the result value
            decrypted_text = result.replace("RESULT ", "", 1)
            history.append(f"Result: {decrypted_text}")
            log("DECRYPT", text)

        elif parts[0] == "history":
            print("Command History:")
            for entry in history:
                print(entry)

        elif parts[0] == "quit":
            encryptor.stdin.write("QUIT\n")
            encryptor.stdin.flush()
            log("QUIT", "Exiting.")
            logger.stdin.write("QUIT\n")
            logger.stdin.flush()
            break

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
