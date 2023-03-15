from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from argon2 import PasswordHasher
import secrets
import re
import os


def get_algorithm(algorithm: str, key: bytes):
    """
    Returns the algorithm object based on the encryption algorithm string provided as an environment variable
    """
    if algorithm == "AES":
        return algorithms.AES(key)
    elif algorithm == "Camellia":
        return algorithms.Camellia(key)
    elif algorithm == "TripleDES":
        return algorithms.TripleDES(key)
    else:
        raise ValueError("Invalid algorithm string provided")


def get_mode(mode: str, nonce: bytes):
    """
    Returns the mode object based on the encryption mode string provided as an environment variable
    """
    if mode == "CTR":
        return modes.CTR(nonce)
    elif mode == "GSM":
        return modes.GCM(nonce)
    elif mode == "CBC":
        return modes.CBC(nonce)
    else:
        raise ValueError("Invalid mode string provided")


class Guardian:

    def __init__(self, time_cost, memory_cost, parallelism, hash_len, salt_len, encoding, type, algorithm, mode, key, nonce) -> None:
        self.TIME_COST = time_cost
        self.MEMORY_COST = memory_cost
        self.PARALLELISM = parallelism
        self.HASH_LEN = hash_len
        self.SALT_LEN = salt_len
        self.ENCODING = encoding
        self.TYPE = type

        self.key = bytes.fromhex(key)
        self.nonce = bytes.fromhex(nonce)

        self.algorithm = get_algorithm(algorithm, self.key)
        self.modes = get_mode(mode, self.nonce)

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
            # missing type
        )

    def hash_password(self, password):
        return self.password_hasher.hash(password)

    def verify_password(self, password_hash, password):
        return self.password_hasher.verify(password_hash, password)

    def encrypt(self, data: str) -> bytes:
        encryptor = self.cipher.encryptor()
        return encryptor.update(data.encode()) + encryptor.finalize()

    def decrypt(self, cipher_data: bytes) -> str:
        decryptor = self.cipher.decryptor()
        data = decryptor.update(cipher_data) + decryptor.finalize()
        return data.decode()

    @staticmethod
    def generate_session_token():
        return secrets.token_hex(16)

    @staticmethod
    def generate_recovery_password_link():
        return secrets.token_urlsafe(32)

    @staticmethod
    def is_valid_phone_number(phone_number: str) -> bool:
        regex = r"^\d{10}$|^\d{11}$|^\d{12}$"
        return re.fullmatch(regex, phone_number) is not None

    @staticmethod
    def is_valid_email(email: str) -> bool:
        regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.fullmatch(regex, email) is not None
