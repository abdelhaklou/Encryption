
from Crypto.Cipher import AES

file_to_encrypt = open("file_to_encrypt", "rb").read()

aes_key = str.encode("1234567891234567")

cipher = AES.new(aes_key, AES.MODE_OCB)
ciphertext, tag = cipher.encrypt_and_digest(file_to_encrypt)
assert len(cipher.nonce) == 15

with open("encrypted.aes", "wb") as f:
    f.write(tag)
    f.write(cipher.nonce)
    f.write(ciphertext)
