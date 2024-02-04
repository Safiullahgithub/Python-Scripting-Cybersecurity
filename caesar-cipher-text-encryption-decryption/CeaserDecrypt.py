#Implement a script that encrypts or decrypts text using the Caesar cipher technique.



def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():  # Encrypt/decrypt only alphabetic characters
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset) if encrypt else chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char  # Preserve non-alphabetic characters
    return result

# Example usage
plaintext = "Hello, how are you!"
shift_value = 3
encrypted_text = caesar_cipher(plaintext, shift_value, encrypt=True)
print("Encrypted text:", encrypted_text)
decrypted_text = caesar_cipher(encrypted_text, shift_value, encrypt=False)
print("Decrypted text:", decrypted_text)