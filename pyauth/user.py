from typing import List


class User:
    def __init__(self, name: str, roles: List[str]) -> None:
        self.name = name
        self.roles = set(roles)

    def get_roles(self) -> List[str]:
        return self.roles
