from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from argon2 import PasswordHasher
import re


class Guardian:
    SALT_LENGTH = 16
    KEY_LENGTH = 16
    N = 2**14
    R = 8
    P = 1

    def __init__(self, key: bytes, nonce: bytes) -> None:
        self.algorithms = algorithms.AES(key)
        self.modes = modes.CTR(nonce)
        self.cipher = Cipher(algorithm=self.algorithms, mode=self.modes)
        self.password_hasher = PasswordHasher()

    def hash_password(self, password):
        return self.password_hasher.hash(password)

    def verify_password(self, password_hash, password):
        return self.password_hasher.verify(password_hash, password)

    def encrypt(self, data):
        encryptor = self.cipher.encryptor()
        return encryptor.update(data) + encryptor.finalize()

    def decryptor(self, cipher_data):
        decryptor = self.cipher.decryptor()
        return decryptor.update(cipher_data) + decryptor.finalize()

    @staticmethod
    def is_valid_phone_number(phone_number: str) -> bool:
        regex = r"^\d{10}$|^\d{11}$|^\d{12}$"
        return re.fullmatch(regex, phone_number) is not None

    @staticmethod
    def is_valid_email(email: str) -> bool:
        regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.fullmatch(regex, email) is not None
