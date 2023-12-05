from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

class Encrypty:
    @staticmethod
    def encrypt_file(file_path, key):
        try:
            if file_path:
                cipher = AES.new(key, AES.MODE_EAX)
                with open(file_path, 'rb') as file:
                    data = file.read()
                    ciphertext, tag = cipher.encrypt_and_digest(data)
                with open(file_path, 'wb') as file:
                    file.write(cipher.nonce)
                    file.write(tag)
                    file.write(ciphertext)
                return True
        except Exception as e:
            print(f"Encryption failed: {str(e)}")
            return False

    @staticmethod
    def decrypt_file(file_path, key):
        try:
            if file_path:
                with open(file_path, 'rb') as file:
                    nonce = file.read(16)
                    tag = file.read(16)
                    ciphertext = file.read()

                cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
                data = cipher.decrypt_and_verify(ciphertext, tag)

                # Overwrite the original file with the decrypted data
                with open(file_path, 'wb') as file:
                    file.write(data)

                return True
        except Exception as e:
            print(f"Decryption failed: {str(e)}")
            return False
