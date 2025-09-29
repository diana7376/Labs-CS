def permute_alphabet(keyword):
    keyword = keyword.upper()
    seen = set()
    perm = []
    for c in keyword:
        if c not in seen and 'A' <= c <= 'Z':
            perm.append(c)
            seen.add(c)
    # Add remaining letters
    for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if c not in seen:
            perm.append(c)
    return perm
def valid_keyword(keyword):
    keyword = keyword.upper()
    return len(keyword) >= 7 and all('A' <= c <= 'Z' for c in keyword)

def valid_message(text):
    for char in text:
        if char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return False
    return True

def caesar_permuted(text, key1, key2, mode):
    # Get permuted alphabet
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
        op = input("Choose operation (encrypt/decrypt) or type 'exit' to quit: ").strip().lower()
        if op == 'exit':
            return 'exit'
        if op in ['encrypt', 'decrypt']:
            return op
        print("Operation must be 'encrypt', 'decrypt', or 'exit'.")

def ask_key1():
    while True:
        try:
            key = int(input("Enter key 1 (integer 1-25): "))
            if 1 <= key <= 25:
                return key
            else:
                print("Key must be an integer between 1 and 25.")
        except ValueError:
            print("Key must be an integer between 1 and 25.")

def ask_key2():
    while True:
        keyword = input("Enter key 2 (Latin letters, min length 7): ").strip().upper()
        if valid_keyword(keyword):
            return keyword
        print("Keyword must be min 7 Latin letters (A-Z only), no symbols/digits.")

def ask_message():
    while True:
        raw_text = input("Enter message: ").replace(" ", "").upper()
        if not raw_text:
            print("Text cannot be empty.")
            continue
        if valid_message(raw_text):
            return raw_text
        print("Text must contain only letters A-Z (no symbols/digits).")

def main():
    print("Caesar Cipher with Permuted Alphabet")
    while True:
        op = ask_mode()
        if op == 'exit':
            print("Exiting...")
            break
        key1 = ask_key1()
        key2 = ask_key2()
        raw_text = ask_message()
        result = caesar_permuted(raw_text, key1, key2, op)
        if op == 'encrypt':
            print("Encrypted message:", result)
        else:
            print("Decrypted message:", result)

if __name__ == "__main__":
    main()
