alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_number):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_number) % 26
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter
    return cipher_text

def decrypt(original_text, shift_number):
    decrypted_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) - shift_number) % 26
            decrypted_text += alphabet[shifted_position]
        else:
            decrypted_text += letter
    return decrypted_text

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    
    if direction not in ["encode", "decode"]:
        print("Invalid choice! Please type 'encode' or 'decode'.")
        continue
    
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if direction == "encode":
        result = encrypt(text, shift)
        print(f"Encrypted: {result}")
    else:
        result = decrypt(text, shift)
        print(f"Decrypted: {result}")
    
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    
    if restart == 'no':
        should_continue = False
        print("Goodbye! 👋")