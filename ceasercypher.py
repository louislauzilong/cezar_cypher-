def enc(text, shift):
    result = ""
    for char in text:
        if char.isalpha():                     
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result   

# Usage
encrypted = enc("Hello World!", 3)
print("Encrypted:", encrypted)
decrypted = enc(encrypted, -3)
print("Decrypted:", decrypted)
