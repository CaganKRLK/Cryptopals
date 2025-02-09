from base64 import b64decode
from Crypto.Cipher import AES
import hashlib

def decrypt_aes_ecb(encrypted_data: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data

def main():
    with open('set01/challenge07.txt', 'r') as f:
        encrypted_data_base64 = f.read().replace('\n', '')
    key = b"YELLOW SUBMARINE"

    encrypted_data = b64decode(encrypted_data_base64)
    decrypted_data = decrypt_aes_ecb(encrypted_data, key)

    excepted_hash = "368f2b80b437209451355b750181b378f425cc00af3922bcecc8d4a7d84a5198"

    decrypted_hash = hashlib.sha256(decrypted_data).hexdigest()

    assert excepted_hash == decrypted_hash

if __name__ == "__main__":
    main()