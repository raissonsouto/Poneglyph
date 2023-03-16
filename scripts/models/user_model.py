from datetime import datetime
from scripts.setup import db, guardian, Base, logger, redis_client
import json


class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.LargeBinary, unique=True, nullable=False)
    email = db.Column(db.LargeBinary, unique=True, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)
    phone = db.Column(db.LargeBinary, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, username: str, email: str, password: str, phone: str):
        self.username = guardian.encrypt(username)
        self.email = guardian.encrypt(email)
        self.password = guardian.hash_password(password)
        self.phone = guardian.encrypt(phone)
        self.created_at = datetime.now()
        self.last_edited = None

        db.session.add(self)
        db.session.commit()

    def __repr__(self) -> str:
        return f'<User {self._decrypt(self.username)}>'

    @classmethod
    def get_user_by_id(cls, user_id):
        """Get a user by its ID.

        :param user_id: The ID of the user to retrieve.
        :type user_id: int
        :return: The User object with the specified ID, or None if no such user exists.
        """
        user = cls.query.get(user_id)

        if user:
            logger.info(f"User '{user_id}' retrieved with username={user.name}")
        else:
            logger.warning(f"No user found with ID '{user_id}'")
        return user

    @classmethod
    def get_user_by_username(cls, username):
        """Get a user by its name.

        :param username: The name of the user to retrieve.
        :type username: str
        :return: The User object with the specified username, or None if no such user exists.
        """
        user = cls.query.filter_by(name=username).first()

        if user:
            logger.info(f"User '{username}' retrieved with id={user.id}")
        else:
            logger.warning(f"No user found with username '{username}'")
        return user

    @classmethod
    def get_all_username(cls) -> list:
        """Get the names of all users in the database.

        :return: A list of all usernames in the database.
        """
        logger.debug("Retrieving names of all users in the database")

        users = cls.query.all()
        usernames = [user.username for user in users]

        logger.debug(f"Found {len(usernames)} users")

        return usernames

    def update(self, username=None, email=None, password=None, phone=None) -> None:
        """Update the properties of a User object.

        :param username: The new username of the user.
        :type username: str

        :param email: The new email of the user.
        :type email: str

        :param password: The new password of the user.
        :type password: str

        :param phone: The new phone number of the user.
        :type phone: str
        """
        if username:  # and self.get_by_username(username) is not None:
            self.username = guardian.encrypt(username, password)
        if email:
            self.email = guardian.encrypt(email, password)
        if password:
            self.password = guardian.hash_password(password)
        if phone:
            self.phone = guardian.encrypt(phone, password)

        self.last_edited = datetime.utcnow()

        logger.info(f"User '{self.username}' updated with id={self.id}, ")

        db.session.commit()

    @classmethod
    def delete_by_id(cls, user_id: int) -> None:
        """Delete a User object from the database by its ID.

        :param user_id: The ID of the user to delete.
        :type user_id: int
        """
        user = cls.query.get(user_id)

        if user:
            db.session.delete(user)
            db.session.commit()
            logger.info(f"User '{user.username}' with id={user.id} deleted")
        else:
            logger.warning(f"No user found with id={user_id}")

    @classmethod
    def delete_by_username(cls, username: str) -> None:
        """Delete a User object from the database by its username.

        :param username: The username of the role to delete.
        :type username: str
        """
        user = cls.query.filter_by(name=username).first()

        if user:
            db.session.delete(user)
            db.session.commit()
            logger.info(f"User '{username}' with id={user.id} deleted")
        else:
            logger.warning(f"No user found with username '{username}'")

    @classmethod
    def authenticate(cls, username: str, password: str) -> str:
        """Authenticate a user by username and password.

        :param username: The username of the user to authenticate.
        :type username: str

        :param password: The password of the user to authenticate.
        :type password: str

        :return: A session token if the authentication was successful, None otherwise.
        :rtype: Optional[str]
        """
        user = cls.query.filter_by(username=username).first()

        if user is not None and user.check_password(password):
            session_token = guardian.get_session_token()

            redis_client.set(session_token, json.dumps({'user_id': user.id}))

            logger.info(f"Authentication successful for user {username}")
            return session_token

        else:
            logger.warning(f"Authentication failed for user {username}")
            return None  # @todo: fix this
