# OOP

```python
from abc import ABC
from typing import Protocol

class Entity(ABC):
    def __init__(self, entity_id: int):
        self._id = entity_id

    @property
    def id(self) -> int:
        return self._id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Entity):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id!r})"

class User(Entity):
    """
    - Inheritance (Entity)
    - Encapsulation via properties (__var_name)
    - Class and static methods (decorators)
    """

    DEFAULT_ROLE = "user"

    def __init__(self, user_id: int, name: str, role: str | None = None):
        super().__init__(user_id)

        if not self.is_valid_name(name):
            raise ValueError("Invalid user name")

        self._name = name
        self._role = role or self.DEFAULT_ROLE
        self._active = True

    # -----------------
    # Properties
    # -----------------

    @property
    def name(self) -> str:
        return self._name

    @property
    def role(self) -> str:
        return self._role

    @role.setter
    def role(self, value: str) -> None:
        if not value:
            raise ValueError("Role cannot be empty")
        self._role = value

    @property
    def is_active(self) -> bool:
        """Whether the user is active in the system."""
        return self._active

    # -----------------
    # Behavior
    # -----------------

    def deactivate(self) -> None:
        self._active = False

    def greet(self) -> str:
        """Polymorphic behavior entry point."""
        return f"Hi, I'm {self.name} ({self.role})"

    # -----------------
    # Factories & helpers
    # -----------------

    @classmethod
    def from_dict(cls, payload: dict) -> "User":
        return cls(
            user_id=payload["id"],
            name=payload["name"],
            role=payload.get("role"),
        )

    @staticmethod
    def is_valid_name(name: str) -> bool:
        return bool(name and name.strip())

u = User(1, "John")

u.greet()
```