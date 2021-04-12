from dataclasses import dataclass
from typing import List

@dataclass
class ActionType:
    create: bool = False
    read: bool = False
    update: bool = False
    delete: bool = False

    @classmethod
    def get_action_types(self) -> List[str]:
        actions = ['create', 'read', 'update', 'delete']
        return actions

