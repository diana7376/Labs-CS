from des_task import apply_pc1, calc_Ci_Di, input_key_64, gen_key_64, ROTATIONS

def main():
    choice = input("Alegeți [1] introducere manuală, [2] generare aleatorie:\n")
    if choice == '1':
        key_64 = input_key_64()
    else:
        key_64 = gen_key_64()
        print("[Cheie generată aleator]:", ''.join(str(b) for b in key_64))

    C0, D0 = apply_pc1(key_64)
    print("\n[Tabel PC-1 aplicat]:")
    print("C0:", ''.join(str(b) for b in C0))
    print("D0:", ''.join(str(b) for b in D0))

    i = int(input("Introduceți runda i (1-16): "))
    if not (1 <= i <= 16):
        raise ValueError("Runda trebuie să fie între 1 și 16.")

    print(f"\n--- Pași rotiri pentru runda {i} ---")
    C, D = C0.copy(), D0.copy()
    for rnd in range(i):
        print(f"Rotire nr. {rnd + 1}: {ROTATIONS[rnd]} poziții.")
        C = C[ROTATIONS[rnd]:] + C[:ROTATIONS[rnd]]
        D = D[ROTATIONS[rnd]:] + D[:ROTATIONS[rnd]]
        print(f" C după rotire {rnd + 1}:", ''.join(str(b) for b in C))
        print(f" D după rotire {rnd + 1}:", ''.join(str(b) for b in D))

    print("\nRezultat final pentru runda", i)
    print("Ci:", ''.join(str(b) for b in C))
    print("Di:", ''.join(str(b) for b in D))

if __name__ == "__main__":
    main()
