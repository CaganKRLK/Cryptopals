from challenge01 import hex_to_bytes

def bytes_to_hex(byte_str):
    return ''.join([f'{byte:02x}' for byte in byte_str])

def xor_bytes(byte_str1, byte_str2):
    return bytes([b1 ^ b2 for b1, b2 in zip(byte_str1, byte_str2)])

def fixed_xor(hex_str1, hex_str2):
    raw_bytes1 = hex_to_bytes(hex_str1)
    raw_bytes2 = hex_to_bytes(hex_str2)
    return bytes_to_hex(xor_bytes(raw_bytes1, raw_bytes2))

def main():
    hex_str1 = '1c0111001f010100061a024b53535009181c'
    hex_str2 = '686974207468652062756c6c277320657965'
    expected_hex_str = '746865206b696420646f6e277420706c6179'

    assert fixed_xor(hex_str1, hex_str2) == expected_hex_str

if __name__ == '__main__':
    main()