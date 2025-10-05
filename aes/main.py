import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def aes256_ctr_encrypt(key: bytes, plaintext: bytes) -> bytes:
    if len(key) != 32:
        raise ValueError("AES-256 key must be 32 bytes.")
    nonce = os.urandom(16)  # 128-бітний IV (CTR mode називає його nonce)
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return nonce + ciphertext  # префіксуємо nonce

def aes256_ctr_decrypt(key: bytes, blob: bytes) -> bytes:
    if len(blob) < 16:
        raise ValueError("ciphertext too short")
    nonce, ciphertext = blob[:16], blob[16:]
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()

if __name__ == "__main__":
    key = os.urandom(32)
    msg = b"AES-256-CTR demo using cryptography stdlib."
    blob = aes256_ctr_encrypt(key, msg)
    recovered = aes256_ctr_decrypt(key, blob)

    print(f"Key: {key.hex()}")
    print(f"Nonce: {blob[:16].hex()}")
    print(f"Plain: {msg!r}")
    print(f"Cipher(hex): {blob.hex()}")
    print(f"Decrypted: {recovered!r}")
    print("OK" if recovered == msg else "FAIL")
