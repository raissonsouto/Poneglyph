import argon2


class Guardian:
    SALT_LENGTH = 16
    KEY_LENGTH = 16
    N = 2**14
    R = 8
    P = 1

    def __init__(self) -> None:
        self.cipher = None

    @staticmethod
    def hash_password(password):
        return argon2.argon2_hash(password)

    @staticmethod
    def verify_password(password_hash, password):
        return argon2.argon2_verify(password_hash, password)

    @staticmethod
    def encrypt(data, password):
        if data:
            key = Scrypt(salt=secrets.token_bytes(Security.SALT_LENGTH), length=Security.KEY_LENGTH, n=Security.N, r=Security.R, p=Security.P, backend=default_backend())
            key = key.derive(password)
            f = Fernet(key)
            return f.encrypt(data.encode())

    @staticmethod
    def decrypt(data, password):
        if data:
            key = Scrypt(salt=secrets.token_bytes(Security.SALT_LENGTH), length=Security.KEY_LENGTH, n=Security.N, r=Security.R, p=Security.P, backend=default_backend())
            key = key.derive(password)
            f = Fernet(key)
            return f.decrypt(data).decode()
