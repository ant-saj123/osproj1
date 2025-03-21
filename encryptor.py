import sys

passkey = None

def vigenere_cipher(text, key, decrypt=False):
    result = []
    key = key.lower()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            if decrypt:
                shift = -shift

            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted_char)

            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

while True:
    line = sys.stdin.readline().strip()
    if not line:
        continue

    parts = line.split(" ", 1)
    command = parts[0].upper()

    if command == "PASSKEY":
        passkey = parts[1] if len(parts) > 1 else None
        print("PASSKEY SET")
        sys.stdout.flush()

    elif command == "ENCRYPT" and passkey:
        text = parts[1] if len(parts) > 1 else ""
        encrypted_text = vigenere_cipher(text, passkey, decrypt=False)
        print(f"RESULT {encrypted_text}")
        sys.stdout.flush()

    elif command == "DECRYPT" and passkey:
        text = parts[1] if len(parts) > 1 else ""
        decrypted_text = vigenere_cipher(text, passkey, decrypt=True)
        print(f"RESULT {decrypted_text}")
        sys.stdout.flush()

    elif command == "QUIT":
        break
