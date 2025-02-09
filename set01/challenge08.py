from Crypto.Cipher.AES import block_size


def count_repetitions(ciphertext):
    chunks = [ciphertext[i:i + block_size] for i in range(0, len(ciphertext), block_size)]
    number_of_duplicates = len(chunks) - len(set(chunks))
    return number_of_duplicates


def detect_ecb_encrypted_ciphertext(ciphertexts):
    best = (-1, 0)

    for i in range(len(ciphertexts)):
        repetitions = count_repetitions(ciphertexts[i])
        best = max(best, (i, repetitions), key=lambda ii: ii[1])

    return best


def main():
    with open("set01/challenge08.txt") as f:
        ciphertexts = [bytes.fromhex(line.strip()) for line in f]
    result = detect_ecb_encrypted_ciphertext(ciphertexts)

    assert result[0] == 132


if __name__ == "__main__":
    main()
