from itertools import combinations
from challenge01 import BASE64_ALPHABET
from challenge02 import bytes_to_hex
from challenge03 import break_single_byte_xor, score_text
from challenge05 import repeating_key_xor

def base64_to_bytes(base64_str : str = "") -> bytes:
    if not base64_str:
        return b""
    
    base64_str = base64_str.replace("\n", "").replace(" ", "")

    binary_str = ""

    for char in base64_str:
        if char in BASE64_ALPHABET:  # Geçerli karakter mi?
            binary_str += format(BASE64_ALPHABET.index(char), "06b")
        elif char == '=':
            pass
        else:
            print(f"Warning: Unknown character '{char}' ignored!")

    padding = (8 - len(binary_str) % 8) % 8
    if padding:
        binary_str = binary_str[:-padding]

    return bytes(int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8))

def hamming_distance(str1, str2) -> int:
    return sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(str1, str2))

def normalized_hamming_distance(data, keysize):
    chunks = [data[i:i + keysize] for i in range(0, len(data), keysize)][:4]
    distance = 0
    pairs = combinations(chunks, 2)
    for (x, y) in pairs:
            distance += hamming_distance(x, y)
    distance /= 6
    return distance / keysize

def gues_keysize(ciphertext):
    distances = []

    for keysize in range(2, 41):
        distance = normalized_hamming_distance(ciphertext, keysize)
        distances.append((keysize, distance))
    
    distances.sort(key=lambda x: x[1])
    return distances[:3]

def split_blocks(data: bytes, keysize: int) -> list[bytes]:
    return [data[i:i + keysize] for i in range(0, len(data), keysize)]

def transpose_blocks(blocks: list[bytes]) -> list[bytes]:
    transposed = [b"".join(block[i:i+1] for block in blocks if i < len(block)) for i in range(len(blocks[0]))]
    return transposed

def break_repeating_key_xor(ciphertext: bytes):
    distances = gues_keysize(ciphertext)

    best_score = 0
    best_key = None
    best_message = None

    for keysize, _ in distances:
        key = ""

        blocks = split_blocks(ciphertext, keysize)
        transposed_blocks = transpose_blocks(blocks)

        for block in transposed_blocks:
            block_key = break_single_byte_xor(block)[0]
            key += chr(block_key)
        plaintext = repeating_key_xor(ciphertext.decode('utf-8'), key)
        score = score_text(plaintext)
        if score > best_score:
            best_score = score
            best_message = plaintext
            best_key = key
    
    return best_key, best_message



def main():
    with open('set01/challenge06.txt', 'r') as f:
        data = f.read()
    


    ciphertext = base64_to_bytes(data)

    key, _ = break_repeating_key_xor(ciphertext)

    # print(f"Message:\n{message}")
    # print(f"Key:\n{key}")

    assert key == 'Terminator X: Bring the noise'

if __name__ == '__main__':
    main()