from typing import TYPE_CHECKING

from prisma.enums import Roles

from src.exceptions.unauthorized import InvalidRoleError
from src.security._base import BaseSecurityScheme

if TYPE_CHECKING:
    from prisma.models import User


class RoleSecurity(BaseSecurityScheme):
    """Role security scheme."""

    def __init__(self, *, role: "Roles | str") -> None:
        super().__init__()

        role = role.upper()
        if role not in [role.value for role in Roles]:
            msg = f"Invalid role: {role}"
            raise ValueError(msg)

        self.role = role

        self._checks.append((self._check_role, InvalidRoleError(role=role)))

    def _check_role(self, user: "User") -> bool:
        """Check user role."""
        return self.role in user.roles
