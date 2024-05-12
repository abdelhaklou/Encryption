
import rsa


# Generate public and private keys and save in local files

def generateKeys():
    public_key, private_key = rsa.newkeys(2048)
    with open("public_key.txt", "wb") as public_file:
        public_file.write(public_key.save_pkcs1())
    with open("private_key.txt", "wb") as private_file:
        private_file.write(private_key.save_pkcs1())    

# Load saved public key from local file

def loadPublicKey(path):
    with open(path, mode='rb') as public_file:
        keydata = public_file.read()
    return rsa.PublicKey.load_pkcs1(keydata)


# Load saved private key from local file

def loadPrivateKey(path):
    with open(path, mode='rb') as private_file:
        keydata = private_file.read()
    return rsa.PrivateKey.load_pkcs1(keydata)    

# Sign message

def sign_message(message_to_sign):
    signature = rsa.sign(message_to_sign.encode(), loadPrivateKey("private_key.txt"), "SHA-256")
    with open("signature", "wb") as f:
        f.write(signature)

# Verify signature of message

def verify_message(message_to_sign):        
    with open("signature", "rb") as f:
        signature = f.read()
    return rsa.verify(message_to_sign.encode(), signature, loadPublicKey("public_key.txt"))

# Encrypt message

def encrypt_message(message):
    message = rsa.encrypt(message.encode(), loadPublicKey("public_key.txt"))
    return message

# Decrypt message

def decrypt_message(encrypted_message):
    decrypted_message = rsa.decrypt(encrypted_message, loadPrivateKey("private_key.txt"))
    return decrypted_message


message = "This is a sample message to encrypt with RSA"





