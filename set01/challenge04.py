from challenge01 import hex_to_bytes
from challenge03 import score_text, break_single_byte_xor

def detect_single_character_xor(hash_list : list):
    best_score = 0
    best_key = None
    best_message = None
    best_line = None

    for i, hash in enumerate(hash_list):
        hash = hash.replace('\n', '')
        key, message = break_single_byte_xor(hex_to_bytes(hash))

        if message:
            score = score_text(message)
            if score > best_score:
                best_score = score
                best_key = key
                best_message = message
                best_line = i+1
    
    return best_line, best_key, best_message

def main():
    with open('set01/challenge04.txt', 'r') as f:
        hash_list = f.readlines()
    
    line, key, message = detect_single_character_xor(hash_list)

    # print(f"Line: {line}")
    # print(f"Key: {chr(key)}")
    # print(f"Message: {message}")

    assert line == 171 and chr(key) == '5' and message == 'Now that the party is jumping\n'

if __name__ == '__main__':
    main()