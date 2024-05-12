import sys
from Crypto.Cipher import AES


aes_key = b'1234567891234567'
with open("encrypted.aes", "rb") as f:
    tag = f.read(16)
    nonce = f.read(15)
    ciphertext = f.read()

cipher = AES.new(aes_key, AES.MODE_OCB, nonce=nonce)
try:
    decrypted_file = cipher.decrypt_and_verify(ciphertext, tag)
except ValueError:
    print("The message was modified!")
    sys.exit(1)


print(ciphertext, " =>", message)
