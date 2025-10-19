class VigenereCipher:
    ROMANIAN_ALPHABET = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
    ALPHABET_SIZE = 31
    MIN_KEY_LENGTH = 7

    def is_valid_text(self, text):
        if not text or not isinstance(text, str):
            return False
        upper_text = text.upper()
        return all(c == ' ' or c in self.ROMANIAN_ALPHABET for c in upper_text)

    def is_valid_key(self, key):
        if not key or len(key) < self.MIN_KEY_LENGTH:
            return False
        return self.is_valid_text(key)

    def preprocess_text(self, text):
        return ''.join(text.upper().split())

    def get_char_position(self, c):
        return self.ROMANIAN_ALPHABET.find(c)

    def get_char_at_position(self, pos):
        return self.ROMANIAN_ALPHABET[pos % self.ALPHABET_SIZE]

    def encrypt(self, text, key):
        if not self.is_valid_text(text):
            raise ValueError("Text invalid! Utilizați doar litere din alfabetul românesc (A-Z).")
        if not self.is_valid_key(key):
            raise ValueError(f"Cheie invalidă! Lungimea cheii trebuie să fie cel puțin {self.MIN_KEY_LENGTH} caractere și să conțină doar litere românești.")
        processed_text = self.preprocess_text(text)
        processed_key = self.preprocess_text(key)
        encrypted_text = []
        for i, plain_char in enumerate(processed_text):
            key_char = processed_key[i % len(processed_key)]
            mi = self.get_char_position(plain_char)
            ki = self.get_char_position(key_char)
            ci = (mi + ki) % self.ALPHABET_SIZE
            encrypted_text.append(self.get_char_at_position(ci))
        return ''.join(encrypted_text)

    def decrypt(self, text, key):
        if not self.is_valid_text(text):
            raise ValueError("Criptogramă invalidă! Utilizați doar litere din alfabetul românesc (A-Z, Ă, Â, Î, Ș, Ț).")
        if not self.is_valid_key(key):
            raise ValueError(f"Cheie invalidă! Lungimea cheii trebuie să fie cel puțin {self.MIN_KEY_LENGTH} caractere și să conțină doar litere românești.")
        processed_text = self.preprocess_text(text)
        processed_key = self.preprocess_text(key)
        plaintext = []
        for i, cipher_char in enumerate(processed_text):
            key_char = processed_key[i % len(processed_key)]
            ci = self.get_char_position(cipher_char)
            ki = self.get_char_position(key_char)
            mi = (ci - ki) % self.ALPHABET_SIZE
            plaintext.append(self.get_char_at_position(mi))
        return ''.join(plaintext)

    def get_alphabet(self):
        return self.ROMANIAN_ALPHABET

    def get_min_key_length(self):
        return self.MIN_KEY_LENGTH
