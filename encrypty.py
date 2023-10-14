from Crypto.Cipher import AES 
from Crypto.Random import get_random_bytes
import secrets

# Generate 256-bit key
key = secrets.token_bytes(32)
print(key)

# Encryption Function
def encrypt_file(file_path, key):
    try:
        # Create cypher using key
        cipher = AES.new(key, AES.MODE_EAX)
        # Read contents of file
        with open(file_path, 'rb') as file:
            data = file.read()
            # Encrypt data and generate tag
            ciphertext, tag = cipher.encrypt_and_digest(data)
        # Write none, tag, ad ciphertext back to file
        with open(file_path, 'wb') as file:
            file.write(cipher.nonce)
            file.write(tag)
            file.write(ciphertext)
    except Exception as e:
        print(f"Encryption failed: {str(e)}")
        
# Decryption Function
def decrypt_file(file_path, key):
    try:
        # Read nonce, tag, and ciphertext from file
        with open(file_path, 'rb') as file:
            nonce = file.read(16)
            tag = file.read(16)
            ciphertext = file.read()
        # Create cipher obj using key and nonce
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        # Decrypt ciphertext and verify tag
        data = cipher.decrypt_and_verify(ciphertext, tag)
        # Write decrypted data back to file
        with open(file_path, 'wb') as file:
            file.write(data)
    except Exception as e:
        print(f"Decryption failed: {str(e)}")
