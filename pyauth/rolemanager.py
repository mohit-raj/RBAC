from typing import Dict, List, Union
from dataclasses import asdict

from .actiontype import ActionType

class RoleManager:
    def __init__ (self, roles: Dict = {}) -> None:
        self.roles = roles
        for role_name, resource_perms in self.roles.items():
            for resource_name, resource_perm in resource_perms.items():
                self.roles[role_name][resource_name] = ActionType(**resource_perm)
    
    def get_roles (self) -> List[str]:
        return list (self.roles.keys ())
    
    def add_role (self, role_name : str) -> None:
        self.roles [role_name] = {}
    
    def remove_role (self, role_name : str) -> None:
        self.roles.pop (role_name)
    
    def add_role_resource (self, role_name : str, resource_name : str, permissions : ActionType) -> None:
        self.roles [role_name] [resource_name] = permissions
    
    def update_role_resource (self, role_name : str, resource_name : str, permissions : ActionType) -> None:
        self.roles [role_name] [resource_name] = permissions
    
    def remove_role_resource (self, role_name : str, resource_name : str) -> None:
        self.roles [role_name].pop (resource_name)

    def get_role_resources (self, role_name : str) -> List[str]:
        return list (self.roles [role_name].keys ())
    
    def get_role_resource_permissions (self, role_name : str, resource_name : str) -> ActionType:
        return self.roles [role_name] [resource_name]
    
    def check_resource_permission (self, role_name : str, resource_name : str, action_type : bool) -> bool:
        return asdict(self.roles [role_name] [resource_name]).get(action_type)
    
    def remove_resource (self, del_resource: Union[str, List[str]]) -> None:
        if type (del_resource) is list:
            for role in self.roles:
                for resource in del_resource:
                    if resource in role:
                        role.pop (resource)
        else:
            for role in self.roles:
                if del_resource in role:
                    role.pop (del_resource)
    
    
