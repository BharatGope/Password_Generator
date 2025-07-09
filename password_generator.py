import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main
print("=== Simple Password Generator ===")
try:
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")
except ValueError:
    print("Please enter a valid number.")
