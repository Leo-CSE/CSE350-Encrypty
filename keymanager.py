from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

class KeyManager:
    KEY_FILE = "encryption_key.bin"
    SALT_FILE = "key_salt.bin"

    @staticmethod
    def generate_salt():
        return get_random_bytes(16)

    @staticmethod
    def derive_key_from_password(master_password, salt):
        return PBKDF2(master_password, salt, dkLen=32, count=1000000)

    @staticmethod
    def load_key():
        try:
            with open(KeyManager.KEY_FILE, 'rb') as key_file:
                return key_file.read()
        except FileNotFoundError:
            return None

    @staticmethod
    def save_key(key):
        with open(KeyManager.KEY_FILE, 'wb') as key_file:
            key_file.write(key)

    @staticmethod
    def load_salt():
        try:
            with open(KeyManager.SALT_FILE, 'rb') as salt_file:
                return salt_file.read()
        except FileNotFoundError:
            return None

    @staticmethod
    def save_salt(salt):
        with open(KeyManager.SALT_FILE, 'wb') as salt_file:
            salt_file.write(salt)
