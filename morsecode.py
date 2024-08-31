# Dictionary representing the morse code chart 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 
                    'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 
                    'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 
                    'Z':'--..', '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', '7':'--...', 
                    '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', 
                    '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(': '-.--.', ')':'-.--.-'} 

def encrypt(message):
    """Encrypts the English message into Morse code."""
    cipher = ''
    for letter in message:
        if letter != ' ':
            # Looks up the dictionary and adds the corresponding morse code
            cipher += MORSE_CODE_DICT.get(letter.upper(), '') + ' '
        else:
            cipher += ' '
    return cipher.strip()

def decrypt(message):
    """Decrypts Morse code message into English."""
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if letter != ' ':
            citext += letter
        else:
            if citext:
                # Find the corresponding English letter for the Morse code
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
            if letter == ' ':
                decipher += ' '
    return decipher.strip()

def main():
    print("Welcome to the Morse Code Translator!")
    print("Choose an option:")
    print("1. Encrypt English to Morse")
    print("2. Decrypt Morse to English")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        return

    if choice == '1':
        message = input("Enter the English message to encrypt: ").strip()
        result = encrypt(message)
        print("\nMorse Code:")
        print(result)
    elif choice == '2':
        message = input("Enter the Morse code to decrypt (use spaces to separate letters and double spaces for words): ").strip()
        result = decrypt(message)
        print("\nEnglish Message:")
        print(result)

if __name__ == "__main__":
    main()
