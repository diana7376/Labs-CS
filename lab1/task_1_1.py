def get_letter_tables():
    # Manually create mappings using for-loops
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_to_index = {}
    index_to_letter = {}
    index = 0
    while index < 26:
        letter = alphabet[index]
        letter_to_index[letter] = index
        index_to_letter[index] = letter
        index += 1
    return letter_to_index, index_to_letter

def valid_message(text):
    # Only check allowed letters, no quick tricks
    allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in text:
        found = False
        i = 0
        while i < len(allowed):
            if char == allowed[i]:
                found = True
                break
            i += 1
        if not found:
            return False
    return True

def caesar_cipher(text, key, mode):
    letter_to_index, index_to_letter = get_letter_tables()
    result = ""
    tlen = 0
    while tlen < len(text):
        char = text[tlen]
        idx = letter_to_index[char]
        if mode == 'encrypt':
            new_idx = (idx + key) % 26
        else:
            new_idx = (idx - key) % 26
        result += index_to_letter[new_idx]
        tlen += 1
    return result

def ask_mode():
    while True:
        op = input("Choose operation (encrypt/decrypt) or type 'exit' to quit: ")
        op = op.strip().lower()
        if op == 'exit':
            return 'exit'
        if op == 'encrypt' or op == 'decrypt':
            return op
        print("Operation must be 'encrypt', 'decrypt', or 'exit'.")

def ask_key():
    while True:
        try:
            key = int(input("Enter key (1-25): "))
            if key >= 1 and key <= 25:
                return key
            else:
                print("Key must be an integer between 1 and 25.")
        except:
            print("Key must be an integer between 1 and 25.")

def ask_message():
    while True:
        raw_text = input("Enter message: ")
        # Remove spaces and make uppercase manually
        filtered = ""
        i = 0
        while i < len(raw_text):
            c = raw_text[i]
            if c != ' ':
                # Manual upper without .upper()
                if 'a' <= c <= 'z':
                    uc = chr(ord(c) - (ord('a') - ord('A')))
                else:
                    uc = c
                filtered += uc
            i += 1
        if not filtered:
            print("Text cannot be empty.")
            continue
        if valid_message(filtered):
            return filtered
        print("Text must contain only letters between A-Z or a-z (no punctuation, digits, or other symbols).")

def main():
    print("=== CAESAR CIPHER with PERMUTED ALPHABET(English Alphabet, Manual Mapping) (TASK 1) ===")
    while True:
        op = ask_mode()
        if op == 'exit':
            print("Exiting...")
            break
        key = ask_key()
        raw_text = ask_message()
        result = caesar_cipher(raw_text, key, op)
        if op == 'encrypt':
            print("Encrypted message:", result)
        else:
            print("Decrypted message:", result)

if __name__ == "__main__":
    main()
