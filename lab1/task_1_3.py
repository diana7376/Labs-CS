def permute_alphabet(keyword):
    # Manual uppercase conversion
    upper_keyword = ""
    i = 0
    while i < len(keyword):
        c = keyword[i]
        if 'a' <= c <= 'z':
            c = chr(ord(c) - (ord('a') - ord('A')))
        upper_keyword += c
        i += 1
    keyword = upper_keyword

    seen = []
    perm = []
    i = 0
    while i < len(keyword):
        c = keyword[i]
        # Only accept A-Z and not in seen
        already = False
        j = 0
        while j < len(seen):
            if c == seen[j]:
                already = True
                break
            j += 1
        if (not already) and ('A' <= c <= 'Z'):
            perm.append(c)
            seen.append(c)
        i += 1
    # Add remaining A-Z
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0
    while i < 26:
        c = alphabet[i]
        already = False
        j = 0
        while j < len(seen):
            if c == seen[j]:
                already = True
                break
            j += 1
        if not already:
            perm.append(c)
            seen.append(c)
        i += 1
    return perm

def valid_keyword(keyword):
    # Manual uppercase conversion
    upper_keyword = ""
    i = 0
    while i < len(keyword):
        c = keyword[i]
        if 'a' <= c <= 'z':
            c = chr(ord(c) - (ord('a') - ord('A')))
        upper_keyword += c
        i += 1
    keyword = upper_keyword
    # Check length and all characters
    if len(keyword) < 7:
        return False
    i = 0
    while i < len(keyword):
        c = keyword[i]
        if not ('A' <= c <= 'Z'):
            return False
        i += 1
    return True

def valid_message(text):
    if len(text) < 7 or len(text) > 10:
        return False
    i = 0
    while i < len(text):
        char = text[i]
        if not ('A' <= char <= 'Z'):
            return False
        i += 1
    return True

def caesar_permuted(text, key1, key2, mode):
    alphabet = permute_alphabet(key2)
    result = ""
    i = 0
    while i < len(text):
        char = text[i]
        # Find index manually
        idx = -1
        j = 0
        while j < 26:
            if char == alphabet[j]:
                idx = j
                break
            j += 1
        if mode == 'encrypt':
            new_idx = (idx + key1) % 26
        else:
            new_idx = (idx - key1) % 26
        result += alphabet[new_idx]
        i += 1
    return result

def ask_mode():
    while True:
        op = input("Choose operation: encrypt/decrypt/swap/exit:\n"
                   "- 'encrypt': Encrypt your own message.\n"
                   "- 'decrypt': Decrypt your colleague's message.\n"
                   "- 'swap': Both operations sequentially.\n"
                   "- 'exit': Quit.\n"
                   "Your choice: ")
        # Manual lowercase conversion/strip
        op_clean = ""
        i = 0
        while i < len(op):
            c = op[i]
            if 'A' <= c <= 'Z':
                c = chr(ord(c) + (ord('a') - ord('A')))
            op_clean += c
            i += 1
        op_clean = op_clean.strip()
        if op_clean == 'exit':
            return 'exit'
        if op_clean == 'encrypt' or op_clean == 'decrypt' or op_clean == 'swap':
            return op_clean
        print("Invalid operation. Choose 'encrypt', 'decrypt', 'swap', or 'exit'.")

def ask_key1(message="Enter key 1 (integer 1-25): "):
    while True:
        s = input(message)
        i = 0
        key_str = ""
        while i < len(s):
            if '0' <= s[i] <= '9':
                key_str += s[i]
            i += 1
        if key_str == "":
            print("Key must be an integer between 1 and 25.")
            continue
        try:
            key = int(key_str)
            if 1 <= key <= 25:
                return key
            else:
                print("Key must be an integer between 1 and 25.")
        except:
            print("Key must be an integer between 1 and 25.")

def ask_key2(message="Enter key 2 (keyword, min. 7 uppercase letters): "):
    while True:
        keyword = input(message)
        # Manual uppercase conversion
        upper_keyword = ""
        i = 0
        while i < len(keyword):
            c = keyword[i]
            if 'a' <= c <= 'z':
                c = chr(ord(c) - (ord('a') - ord('A')))
            upper_keyword += c
            i += 1
        keyword = upper_keyword
        if valid_keyword(keyword):
            return keyword
        print("Keyword must be at least 7 uppercase letters (A-Z only).")

def ask_own_message():
    while True:
        text = input("Enter your message (7-10 uppercase letters, no spaces): ")
        # Remove spaces and manual uppercase
        filtered = ""
        i = 0
        while i < len(text):
            c = text[i]
            if c == ' ':
                i += 1
                continue
            if 'a' <= c <= 'z':
                c = chr(ord(c) - (ord('a') - ord('A')))
            filtered += c
            i += 1
        if not filtered:
            print("Text cannot be empty.")
            continue
        if valid_message(filtered):
            return filtered
        print("Message must be 7 to 10 uppercase letters (A-Z only, no spaces).")

def ask_colleague_message():
    while True:
        text = input("Enter your colleague's encrypted message (7-10 uppercase letters, no spaces): ")
        # Remove spaces and manual uppercase
        filtered = ""
        i = 0
        while i < len(text):
            c = text[i]
            if c == ' ':
                i += 1
                continue
            if 'a' <= c <= 'z':
                c = chr(ord(c) - (ord('a') - ord('A')))
            filtered += c
            i += 1
        if not filtered:
            print("Text cannot be empty.")
            continue
        if valid_message(filtered):
            return filtered
        print("Encrypted message must be 7 to 10 uppercase letters (A-Z only, no spaces).")

def main():
    print("=== CAESAR CIPHER with PERMUTED ALPHABET (TASK 3) ===")
    while True:
        op = ask_mode()
        if op == 'exit':
            print("Exiting program.")
            break
        if op == 'encrypt' or op == 'swap':
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
        if op == 'decrypt' or op == 'swap':
            print("\n-- Decrypting your colleague's message --")
            col_cipher = ask_colleague_message()
            col_key1 = ask_key1("Enter your colleague's key 1 (integer 1-25): ")
            col_key2 = ask_key2("Enter your colleague's key 2 (keyword, min. 7 uppercase letters): ")
            decrypted = caesar_permuted(col_cipher, col_key1, col_key2, 'decrypt')
            print("Decrypted message from your colleague:", decrypted)

if __name__ == "__main__":
    main()
