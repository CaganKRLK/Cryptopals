from challenge01 import hex_to_bytes

def single_byte_xor(input_bytes, key) -> bytes :
    return bytes(key ^ byte for byte in input_bytes)

def score_text(text: str) -> int:
    freq = "ETAOIN SHRDLUetaoinshrdlu"
    return sum(text.count(c) for c in freq)

def break_single_byte_xor(ciphertext: bytes) -> tuple :

    best_score = 0
    best_key = None
    best_message = None

    for key in range(256):
        decrypted = single_byte_xor(ciphertext, key)
        
        try:
            text = decrypted.decode('utf-8')
            score = score_text(text)

            if score > best_score:
                best_score = score
                best_key = key
                best_message = text
        except UnicodeDecodeError:
            pass

    return best_key, best_message

def main():
    hex_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    key, message = break_single_byte_xor(hex_to_bytes(hex_str))

    assert chr(key) == 'X' and message == "Cooking MC's like a pound of bacon"

if __name__ == '__main__':
    main()