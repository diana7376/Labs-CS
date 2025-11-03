PC_1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]
ROTATIONS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def apply_pc1(key_bits):
    """Aplică permutarea PC-1 și returnează C0, D0."""
    permuted = [key_bits[i - 1] for i in PC_1]
    C0 = permuted[:28]
    D0 = permuted[28:]
    return C0, D0

def left_rotate(bits, n):
    """Rotire la stânga a bitilor cu n poziții."""
    return bits[n:] + bits[:n]

def calc_Ci_Di(C0, D0, i):
    """Calculează Ci și Di pentru runda i, afișând fiecare pas."""
    C, D = C0.copy(), D0.copy()
    for rnd in range(i):
        C = left_rotate(C, ROTATIONS[rnd])
        D = left_rotate(D, ROTATIONS[rnd])
    return C, D

def input_key_64():
    key_str = input("Introduceți cheia DES de 64 biți (ex: 011100101...):\n")
    key_bits = [int(b) for b in key_str if b in '01']
    if len(key_bits) != 64:
        raise ValueError("Cheia trebuie să conțină exact 64 biți.")
    return key_bits

def gen_key_64():
    import random
    return [random.randint(0, 1) for _ in range(64)]
