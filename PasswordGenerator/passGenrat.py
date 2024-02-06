import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True):
    # Define character sets
    character_set = ""
    if include_uppercase:
        character_set += string.ascii_uppercase
    if include_lowercase:
        character_set += string.ascii_lowercase
    if include_digits:
        character_set += string.digits
    if include_symbols:
        character_set += string.punctuation

    # Generate password
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

# Prompt for password criteria
while True:
    try:
        length = int(input("Enter password length: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
include_digits = input("Include digits? (y/n): ").lower() == "y"
include_symbols = input("Include symbols? (y/n): ").lower() == "y"

# Generate password
password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols)
print("Generated Password:", password)
