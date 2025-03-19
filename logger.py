import sys
import time

def log_message(log_file):
   with open(log_file, 'a') as file:
       while True:
           message = sys.stdin.readline().strip()
           if message == "QUIT":
               break
           timestamp = time.strftime("%Y-%m-%d %H:%M")
           action, _, msg = message.partition(" ")
           file.write(f"{timestamp} [{action}] {msg}\n")

def main():
   if len(sys.argv) != 2:
       print("Usage: python logger.py <log_file>")
       sys.exit(1)
   log_message(sys.argv[1])

if __name__ == "__main__":
   main()
