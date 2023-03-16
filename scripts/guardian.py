from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from argon2 import PasswordHasher
import secrets
import re
import os


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

        self.algorithm = self.__get_algorithm(algorithm, self.key)
        self.modes = self.__get_algorithm(mode, self.nonce)

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

    def __get_algorithm(self, algorithm: str, key: bytes):
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

    def __get_mode(self, mode: str, nonce: bytes):
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

    def hash_password(self, password: str) -> bytes:
        """Hash a password using a secure password hashing algorithm.

        :param password: The password to hash.
        :type password: str

        :return: The hashed password.
        :rtype: bytes
        """
        return self.password_hasher.hash(password)

    def verify_password(self, password_hash: bytes, password: str) -> bool:
        """Verify a password against its hash.

        :param password_hash: The hash of the password.
        :type password_hash: bytes

        :param password: The password to verify.
        :type password: str

        :return: True if the password matches its hash, False otherwise.
        :rtype: bool
        """
        try:
            self.password_hasher.verify(password_hash, password.encode())
            return True

        except ValueError:
            return False

    def encrypt(self, data: str) -> bytes:
        """Encrypts the provided string.

        :param data: The string to be encrypted.
        :type data: str

        :return: The encrypted data as bytes.
        :rtype: bytes
        """
        encryptor = self.cipher.encryptor()
        return encryptor.update(data.encode()) + encryptor.finalize()

    def decrypt(self, cipher_data: bytes) -> str:
        """Decrypts the provided bytes.

        :param cipher_data: The encrypted data to be decrypted.
        :type cipher_data: bytes

        :return: The decrypted data as a string.
        :rtype: str
        """
        decryptor = self.cipher.decryptor()
        data = decryptor.update(cipher_data) + decryptor.finalize()
        return data.decode()

    @staticmethod
    def generate_session_token() -> str:
        """Generate a secure random session token.

        :return: A random session token.
        :rtype: str
        """
        return secrets.token_hex(16)

    @staticmethod
    def generate_recovery_password_link() -> str:
        """Generate a secure recovery password link.

        :return: A recovery password link.
        :rtype: str
        """
        return secrets.token_urlsafe(32)

    @staticmethod
    def is_valid_phone_number(phone_number: str) -> bool:
        """Validate a phone number using a regular expression.

        :param phone_number: The phone number to validate.
        :type phone_number: str

        :return: True if the phone number is valid, False otherwise.
        :rtype: bool
        """
        regex = r"^\d{10}$|^\d{11}$|^\d{12}$"
        return re.fullmatch(regex, phone_number) is not None

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Validate an email address using a regular expression.

        :param email: The email address to validate.
        :type email: str

        :return: True if the email address is valid, False otherwise.
        :rtype: bool
        """
        regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.fullmatch(regex, email) is not None