BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def hex_to_bytes(hex_str):
    return bytes(int(hex_str[i:i+2], 16) for i in range(0, len(hex_str), 2))

def bytes_to_base64(byte_str):
    binary_str = ''.join([f'{byte:08b}' for byte in byte_str])
    padding = (6 - len(binary_str) % 6) % 6
    binary_str += '0' * padding

    base64_str = ''
    for i in range(0, len(binary_str), 6):
        index = int(binary_str[i:i+6], 2)
        base64_str += BASE64_ALPHABET[index]

    padding = (4 - len(base64_str) % 4) % 4
    base64_str += '=' * padding

    return base64_str

def hex_to_base64(hex_str):
    raw_bytes = hex_to_bytes(hex_str)
    return bytes_to_base64(raw_bytes)

def main():
    hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    base64_str = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

    assert hex_to_base64(hex_str) == base64_str

if __name__ == '__main__':
    main()