from typing import List
from .user import User
from .rolemanager import RoleManager
from .resourcemanager import ResourceManager


class Admin(User):
    def __init__(self, name: str,  roles: List[str], role_manager: RoleManager,
                 resource_manager: ResourceManager) -> None:
        super().__init__(name, roles)
        self.role_manager = role_manager
        self.resource_manager = resource_manager
