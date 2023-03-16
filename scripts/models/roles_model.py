from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
# from sqlalchemy.orm import relationship
from scripts.setup import db, Base, logger


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    parent_id = Column(Integer, ForeignKey('roles.id'))
    capacity = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_edited = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # children = relationship("Role", backref="parent", remote_side=[id]) #  should I use it?

    def __init__(self, name: str, capacity: int, parent=None) -> None:
        self.name = name
        self.capacity = capacity
        self.parent = parent
        self.created_at = datetime.now()

        db.session.add(self)
        db.session.commit()

        logger.info(f"Role '{self.name}' created with id={self.id}, capacity={self.capacity} and parent={self.parent}")

    def __repr__(self) -> str:
        return f'<Role: {self.name}>'

    @classmethod
    def get_by_id(cls, role_id: int) -> "Role":
        """Get a role by its ID.

        :param role_id: The ID of the role to retrieve.
        :type role_id: int
        :return: The Role object with the specified ID, or None if no such role exists.
        """
        role = cls.query.get(role_id)

        if role:
            logger.info(f"Role '{role_id}' retrieved with name={role.name}")
        else:
            logger.warning(f"No role found with ID '{role_id}'")
        return role

    @classmethod
    def get_by_role_name(cls, role_name: str) -> "Role":
        """Get a role by its name.

        :param role_name: The name of the role to retrieve.
        :type role_name: str
        :return: The Role object with the specified name, or None if no such role exists.
        """
        role = cls.query.filter_by(name=role_name).first()

        if role:
            logger.info(f"Role '{role_name}' retrieved with id={role.id}")
        else:
            logger.warning(f"No role found with name '{role_name}'")
        return role

    @classmethod
    def list_all_roles_name(cls) -> list:
        """Get the names of all roles in the database.

        :return: A list of all role names in the database.
        """
        logger.debug("Retrieving names of all roles in the database")

        roles = cls.query.all()
        role_names = [role.name for role in roles]

        logger.debug(f"Found {len(role_names)} roles")

        return role_names

    def update(self, name=None, capacity=None, parent=None) -> None:
        """Update the properties of a Role object.

        :param name: The new name of the role. If not provided, the name is not changed.
        :type name: str

        :param capacity: The new capacity of the role. If not provided, the capacity is not changed.
        :type capacity: int

        :param parent: The new parent of the role. If not provided, the parent is not changed.
        :type parent: Role
        """
        if name is not None:
            self.name = name

        if capacity is not None:
            self.capacity = capacity

        if parent is not None:
            self.parent = parent

        self.last_edited = datetime.utcnow()

        logger.info(
            f"Role '{self.name}' updated with id={self.id}, capacity={self.capacity}, and superior={self.superior}")

    @classmethod
    def delete_by_id(cls, role_id: int) -> None:
        """
        Delete a Role object from the database by its ID.

        :param role_id: The ID of the role to delete.
        :type role_id: int
        """
        role = cls.query.get(role_id)

        if role:
            db.session.delete(role)
            db.session.commit()
            logger.info(f"Role '{role.name}' with id={role.id} deleted")
        else:
            logger.warning(f"No role found with id={role_id}")

    @classmethod
    def delete_by_name(cls, role_name: str) -> None:
        """
        Delete a Role object from the database by its name.

        :param role_name: The name of the role to delete.
        :type role_name: str
        """
        role = cls.query.filter_by(name=role_name).first()

        if role:
            db.session.delete(role)
            db.session.commit()
            logger.info(f"Role '{role_name}' with id={role.id} deleted")
        else:
            logger.warning(f"No role found with name '{role_name}'")
