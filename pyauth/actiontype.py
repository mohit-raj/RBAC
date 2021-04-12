from dataclasses import dataclass


@dataclass
class ActionType:
    create: bool = False
    read: bool = False
    update: bool = False
    delete: bool = False
