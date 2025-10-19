from vigenere_cipher import VigenereCipher

def main():
    cipher = VigenereCipher()
    print("Alfabetul românesc:", cipher.get_alphabet())
    print("Lungimea minimă a cheii:", cipher.get_min_key_length(), "caractere\n")

    while True:
        try:
            print("Alegeți operația:")
            print(" 1. Criptare")
            print(" 2. Decriptare")
            print(" 3. Ieșire")
            choice = input("Opțiunea dumneavoastră: ")
            if choice == "3":
                break
            if choice not in ("1", "2"):
                print("\n Opțiune invalidă! Alegeți 1, 2 sau 3.\n")
                continue

            key = input(f"Introduceți cheia (min. {cipher.get_min_key_length()} caractere): ")
            if not cipher.is_valid_key(key):
                print("\n Cheie invalidă!")
                print(" - Lungimea minimă:", cipher.get_min_key_length(), "caractere")
                print(" - Utilizați doar litere din alfabetul românesc:", cipher.get_alphabet(), "\n")
                continue

            if choice == "1":
                input_text = input("Introduceți mesajul de criptat: ")
            else:
                input_text = input("Introduceți criptograma de decriptat: ")

            if not cipher.is_valid_text(input_text):
                print("\n Text invalid!")
                print(" - Utilizați doar litere din alfabetul românesc:", cipher.get_alphabet(), "\n")
                continue

            print()
            if choice == "1":
                result = cipher.encrypt(input_text, key)
                print("Mesaj original:", input_text)
                print("Criptogramă:", result)
            else:
                result = cipher.decrypt(input_text, key)
                print("Criptogramă:", input_text)
                print("Mesaj decriptat:", result)
            print()
        except Exception as e:
            print("\nEroare:", str(e), "\n")

if __name__ == "__main__":
    main()
