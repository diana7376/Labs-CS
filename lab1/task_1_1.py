def get_letter_tables():
    letter_to_index = {chr(i): idx for idx, i in enumerate(range(ord('A'), ord('Z') + 1))}
    index_to_letter = {idx: chr(i) for idx, i in enumerate(range(ord('A'), ord('Z') + 1))}
    return letter_to_index, index_to_letter

def valid_message(text):
    for char in text:
        if char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return False
    return True

def caesar_cipher(text, key, mode):
    letter_to_index, index_to_letter = get_letter_tables()
    result = ""
    for char in text:
        idx = letter_to_index[char]
        if mode == 'encrypt':
            new_idx = (idx + key) % 26
        else:
            new_idx = (idx - key) % 26
        result += index_to_letter[new_idx]
    return result

def ask_mode():
    while True:
        op = input("Choose operation (encrypt/decrypt) or type 'exit' to quit: ").strip().lower()
        if op == 'exit':
            return 'exit'
        if op in ['encrypt', 'decrypt']:
            return op
        print("Operation must be 'encrypt', 'decrypt', or 'exit'.")

def ask_key():
    while True:
        try:
            key = int(input("Enter key (1-25): "))
            if 1 <= key <= 25:
                return key
            else:
                print("Key must be an integer between 1 and 25.")
        except ValueError:
            print("Key must be an integer between 1 and 25.")

def ask_message():
    while True:
        raw_text = input("Enter message: ").replace(" ", "").upper()
        if not raw_text:
            print("Text cannot be empty.")
            continue
        if valid_message(raw_text):
            return raw_text
        print("Text must contain only letters between A-Z or a-z (no punctuation, digits, or other symbols).")

def main():
    print("Caesar Cipher (English Alphabet, Manual Mapping)")
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
