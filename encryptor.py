import sys

passkey = None

def caesar_cipher(text, shift, decrypt=False):
   result = []
   shift = -shift if decrypt else shift
   for char in text:
       if char.isalpha():
           base = ord('A') if char.isupper() else ord('a')
           result.append(chr((ord(char) - base + shift) % 26 + base))
       else:
           result.append(char)
   return "".join(result)

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

   elif command == "QUIT":
       break
