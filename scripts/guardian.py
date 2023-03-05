from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from argon2 import PasswordHasher
import re
import os


def get_algorithm():
    if os.getenv("TIME_COST") == "":
        pass


class Guardian:
    TIME_COST = int(os.getenv("TIME_COST"))
    MEMORY_COST = int(os.getenv("MEMORY_COST"))
    PARALLELISM = int(os.getenv("PARALLELISM"))
    HASH_LEN = int(os.getenv("HASH_LEN"))
    SALT_LEN = int(os.getenv("SALT_LEN"))
    ENCODING = os.getenv("ENCODING")
    TYPE = os.getenv("TYPE")

    def __init__(self, key: bytes, nonce: bytes) -> None:

        self.algorithm = algorithms.AES(key)
        self.modes = modes.CTR(nonce)

        self.cipher = Cipher(
            algorithm=self.algorithm,
            mode=self.modes
        )
        self.password_hasher = PasswordHasher(
            time_cost=self.TIME_COST,
            memory_cost=self.MEMORY_COST,
            parallelism=self.PARALLELISM,
            hash_len=self.HASH_LEN,
            salt_len=self.SALT_LEN,
            encoding=self.ENCODING
        )

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
