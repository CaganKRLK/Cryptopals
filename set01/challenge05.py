from challenge02 import bytes_to_hex

def repeating_key_xor(plaintext, key):
    key_bytes = [ord(c) for c in key]
    key_length = len(key_bytes)

    ciphertext = []
    for i, char in enumerate(plaintext):
        key_byte = key_bytes[i % key_length]
        ciphertext.append(chr(ord(char) ^ key_byte))
    return ''.join(ciphertext)

def main():
    key = 'ICE'
    plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

    ciphertext = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

    # print(bytes_to_hex(repeating_key_xor(plaintext,key).encode()))

    assert bytes_to_hex(repeating_key_xor(plaintext,key).encode()) == ciphertext

if __name__ == '__main__':
    main()