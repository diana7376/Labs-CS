def permute_alphabet(keyword):
    # Convert to uppercase manually
    uppercase_keyword = ""
    i = 0
    while i < len(keyword):
        c = keyword[i]
        if 'a' <= c <= 'z':
            c = chr(ord(c) - (ord('a') - ord('A')))
        uppercase_keyword += c
        i += 1
    keyword = uppercase_keyword

    seen = []
    perm = []
    i = 0
    while i < len(keyword):
        c = keyword[i]
        # Only allow A-Z and not already seen
        already = False
        for s in seen:
            if c == s:
                already = True
                break
        if (not already) and ('A' <= c <= 'Z'):
            perm.append(c)
            seen.append(c)
        i += 1
    # Add remaining letters
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0
    while i < 26:
        c = alphabet[i]
        already = False
        for s in seen:
            if c == s:
                already = True
                break
        if not already:
            perm.append(c)
            seen.append(c)
        i += 1
    return perm

def valid_keyword(keyword):
    # Manual uppercase
    uppercase_keyword = ""
    i = 0
    while i < len(keyword):
        c = keyword[i]
        if 'a' <= c <= 'z':
            c = chr(ord(c) - (ord('a') - ord('A')))
        uppercase_keyword += c
        i += 1
    keyword = uppercase_keyword

    # Check length >=7 and all A-Z
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
        # Manually find index
        idx = -1
        j = 0
        while j < 26:
            if alphabet[j] == char:
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
        op = input("Choose operation (encrypt/decrypt) or type 'exit' to quit: ")
        # Manual lowercase
        op_lc = ""
        i = 0
        while i < len(op):
            c = op[i]
            # Uppercase to lowercase if needed
            if 'A' <= c <= 'Z':
                c = chr(ord(c) + (ord('a') - ord('A')))
            op_lc += c
            i += 1
        op = op_lc.strip()
        if op == 'exit':
            return 'exit'
        if op == 'encrypt' or op == 'decrypt':
            return op
        print("Operation must be 'encrypt', 'decrypt', or 'exit'.")

def ask_key1():
    while True:
        try:
            s = input("Enter key 1 (integer 1-25): ")
            i = 0
            key_str = ""
            # Ignore all non-digit characters (for safety)
            while i < len(s):
                if '0' <= s[i] <= '9':
                    key_str += s[i]
                i += 1
            if key_str == "":
                raise Exception()
            key = int(key_str)
            if 1 <= key <= 25:
                return key
            else:
                print("Key must be an integer between 1 and 25.")
        except:
            print("Key must be an integer between 1 and 25.")

def ask_key2():
    while True:
        keyword = input("Enter key 2 (Latin letters, min length 7): ")
        # Manual uppercase
        uppercase_keyword = ""
        i = 0
        while i < len(keyword):
            c = keyword[i]
            if 'a' <= c <= 'z':
                c = chr(ord(c) - (ord('a') - ord('A')))
            uppercase_keyword += c
            i += 1
        keyword = uppercase_keyword
        if valid_keyword(keyword):
            return keyword
        print("Keyword must be min 7 Latin letters (A-Z only), no symbols/digits.")

def ask_message():
    while True:
        raw_text = input("Enter message: ")
        # Remove spaces and manually uppercase
        filtered = ""
        i = 0
        while i < len(raw_text):
            c = raw_text[i]
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
        print("Text must contain only letters A-Z (no symbols/digits).")

def main():
    print("=== CAESAR CIPHER with PERMUTED ALPHABET (TASK 2) ===")
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
