def permute_alphabet(keyword):
    keyword = keyword.upper()
    seen = set()
    perm = []
    for c in keyword:
        if c not in seen and 'A' <= c <= 'Z':
            perm.append(c)
            seen.add(c)
    for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if c not in seen:
            perm.append(c)
    return perm

def valid_keyword(keyword):
    keyword = keyword.upper()
    return len(keyword) >= 7 and all('A' <= c <= 'Z' for c in keyword)

def valid_message(text):
    if not (7 <= len(text) <= 10):
        return False
    for char in text:
        if char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return False
    return True

def caesar_permuted(text, key1, key2, mode):
    alphabet = permute_alphabet(key2)
    result = ""
    for char in text:
        idx = alphabet.index(char)
        if mode == 'encrypt':
            new_idx = (idx + key1) % 26
        else:
            new_idx = (idx - key1) % 26
        result += alphabet[new_idx]
    return result

def ask_mode():
    while True:
        op = input("Choose operation: encrypt/decrypt/swap/exit:\n"
                   "- 'encrypt': Encrypt your own message.\n"
                   "- 'decrypt': Decrypt your colleague's message.\n"
                   "- 'swap': Both operations sequentially.\n"
                   "- 'exit': Quit.\n"
                   "Your choice: ").strip().lower()
        if op == 'exit':
            return 'exit'
        if op in ['encrypt', 'decrypt', 'swap']:
            return op
        print("Invalid operation. Choose 'encrypt', 'decrypt', 'swap', or 'exit'.")

def ask_key1(message="Enter key 1 (integer 1-25): "):
    while True:
        try:
            key = int(input(message))
            if 1 <= key <= 25:
                return key
            else:
                print("Key must be an integer between 1 and 25.")
        except ValueError:
            print("Key must be an integer between 1 and 25.")

def ask_key2(message="Enter key 2 (keyword, min. 7 uppercase letters): "):
    while True:
        keyword = input(message).strip().upper()
        if valid_keyword(keyword):
            return keyword
        print("Keyword must be at least 7 uppercase letters (A-Z only).")

def ask_own_message():
    while True:
        text = input("Enter your message (7-10 uppercase letters, no spaces): ").replace(" ", "").upper()
        if not text:
            print("Text cannot be empty.")
            continue
        if valid_message(text):
            return text
        print("Message must be 7 to 10 uppercase letters (A-Z only, no spaces).")

def ask_colleague_message():
    while True:
        text = input("Enter your colleague's encrypted message (7-10 uppercase letters, no spaces): ").replace(" ", "").upper()
        if not text:
            print("Text cannot be empty.")
            continue
        if valid_message(text):
            return text
        print("Encrypted message must be 7 to 10 uppercase letters (A-Z only, no spaces).")

def main():
    print("=== CAESAR CIPHER with PERMUTED ALPHABET (TASK 3) ===")
    while True:
        op = ask_mode()
        if op == 'exit':
            print("Exiting program.")
            break
        if op in ['encrypt', 'swap']:
            print("\n-- Encrypting your message --")
            own_message = ask_own_message()
            own_key1 = ask_key1("Enter your key 1 (integer 1-25): ")
            own_key2 = ask_key2("Enter your key 2 (keyword, min. 7 uppercase letters): ")
            encrypted = caesar_permuted(own_message, own_key1, own_key2, 'encrypt')
            print("Your encrypted message:", encrypted)
            print("Give your partner:")
            print(f"  - Encrypted message: {encrypted}")
            print(f"  - Key 1: {own_key1}")
            print(f"  - Key 2: {own_key2}")
        if op in ['decrypt', 'swap']:
            print("\n-- Decrypting your colleague's message --")
            col_cipher = ask_colleague_message()
            col_key1 = ask_key1("Enter your colleague's key 1 (integer 1-25): ")
            col_key2 = ask_key2("Enter your colleague's key 2 (keyword, min. 7 uppercase letters): ")
            decrypted = caesar_permuted(col_cipher, col_key1, col_key2, 'decrypt')
            print("Decrypted message from your colleague:", decrypted)

if __name__ == "__main__":
    main()
