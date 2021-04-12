import os
import sys

from dataclasses import asdict
from typing import List
from .admin import Admin
from .user import User
from .actiontype import ActionType
from .rolemanager import RoleManager
from .resourcemanager import ResourceManager
from .actiontype import ActionType


class System:
    def __init__(self) -> None:
        # Initialize users, resources, and roles
        roles = self._init_roles()
        self.role_manager = RoleManager(roles)
        resources = self._init_resources()
        self.resource_manager = ResourceManager(resources)
        self.users = self._init_users()

    def run(self) -> None:
        # Login Menu
        user = self._run_login_menu()

        # Run the menu
        while True:
            print("press 0 to exit")
            print("press 1 for login as another user")

            if isinstance(user, Admin):
                # Run the admin menu
                self._print_admin_menu()
                response = input("Enter your choice: ")
                while response not in ['0', '1', '2', '3', '4']:
                    print("Invalid input, try again", file=sys.stderr)
                    response = input("Enter your choice: ")
                self._run_admin_menu(response)
            else:
                # Run the user menu
                self._print_user_menu()
                response = input("Enter your choice: ")
                while response not in ['0', '1', '2', '3']:
                    print("Invalid input, try again", file=sys.stderr)
                    response = input("Enter your choice: ")
                self._run_user_menu(user, response)

            if response == '0':
                return
            elif response == '1':
                user = self._run_login_menu()

    def _run_login_menu(self):
        user = None
        while user is None:
            username = input("Username: ")
            user = self._login(username)

            if user is None:
                print("Incorrect user, try again", file=sys.stderr)

        print(f"hi! you are logged in as {user.name}")
        return user

    def _login(self, username: str) -> None:
        return self.users.get(username, None)

    def _print_admin_menu(self) -> None:
        print("press 2 for create user")
        print("press 3 for create role")
        print("press 4 to edit a role")
    
    def _print_create_user_menu(self) -> None:
        print ("enter username for new user: ")
    
    def _print_user_add_roles_menu(self) -> List[str]:
        all_roles = self.role_manager.get_roles ()
        print("select roles for new user : " + ', '.join (all_roles) + " as 1/0 (E.g.: 0110 for second and third roles.)")
        return all_roles

    def _run_admin_menu(self, response) -> None:
        if response == "2":
            self._print_create_user_menu ()
            
            new_username = input('username: ')
            while new_username in self.users:
                print("Invalid input, try again : Username already exists", file=sys.stderr)
                new_username = input('username: ')
            

            all_roles = self._print_user_add_roles_menu ()
            role_selection = input("enter roles: ")
            role_names = [ all_roles [i] for i in range (len (role_selection)) if role_selection [i] == '1' ]
            if 'admin' in role_names:
                self.users [new_username] = Admin (new_username, role_names, self.role_manager, self.resource_manager)
            else:
                self.users [new_username] = User (new_username, role_names)
            
        elif response == "3":
            self._run_create_role_menu()
        elif response == "4":
            self._run_edit_role_menu()

    def _edit_role_menu (self):
        print ("Select role to edit")
        all_roles = self.role_manager.get_roles ()
        for idx, role in enumerate (all_roles, 1):
            print (f"press {idx} to edit {role}")
        
        selected_role = int (input("Enter your choice: "))
        while selected_role not in range (1, len (all_roles)+1):
            print("Invalid input, try again", file=sys.stderr)
            selected_role = int (input("Enter your choice: "))
        return all_roles [selected_role - 1]
    
    def _format_permissions (self, permissions: ActionType) -> str:
        actions = ActionType.get_action_types ()
        return ', '.join ([ action for action in actions if (asdict(permissions).get(action)) ])

    def _print_role_resource_permissions (self, role_name: str):
        resources = self.role_manager.get_role_resources (role_name)
        print("Resource permissions as follows:")
        for resource in resources:
            permissions = self._format_permissions (self.role_manager.get_role_resource_permissions (role_name, resource))
            print (f"{resource} : {permissions}")


    def _print_edit_role_resources_menu (self):
        print ("press 0 to save")
        print ("press 1 to view resource permissions")
        print ("press 2 to edit resource permissions")
        
    
    def _permissions_menu (self) -> ActionType:
        print("Enter permissions for create, read, update, delete as 1/0 (E.g.: 0110 for read and update permissions).")
        perm = input("enter permission: ")
        return ActionType(*[True if x == '1' else False for x in list(perm)])

    '''
    TODO : [WIP]
    def _add_role_resource_menu (self, role_name: str) -> None:
        current_resources = self.role_manager.get_role_resources (role_name)
        all_resources = self.resource_manager.get_resources ()
        rem_resources = [ res for res in all_resources if res not in current_resources]

        for idx, resource in enumerate (rem_resources, 1):
            print (f"press {idx} to add {resource}.")
        response = int (input("Enter your choice: "))
        while response not in range (1, len (rem_resources)+1):
            print("Invalid input, try again", file=sys.stderr)
            response = int (input("Enter your choice: "))
        
        resource_name = rem_resources [response - 1]
        permissions = self._permissions_menu ()

        self.role_manager.add_role_resource (role_name, resource_name, permissions)
    '''

    '''
    TODO : [WIP]
    def _remove_role_resource_menu (self, role_name: str) -> None:
        resources = self.role_manager.get_role_resources (role_name)

        formatted_resource_str = ', '.join (resources)
        print(f"Select resources to delete: {formatted_resource_str}  as 1/0 (E.g.: 0110 for second and third resource")
        del_resources = input("enter: ")

        del_resources_name = [ resources [i] for i in range (len (del_resources)) if del_resources [i] == '1' ]
        
        for resource_name in del_resources_name:
            self.role_manager.remove_role_resource (role_name, resource_name)
    '''

    def _edit_role_resource_menu (self, role_name: str) -> None:
        resources = self.role_manager.get_role_resources (role_name)

        for idx, resource in enumerate (resources, 1):
            print (f"press {idx} to edit {resource} permissions.")
        response = int (input("Enter your choice: "))
        while response not in range (1, len (resources)+1):
            print("Invalid input, try again", file=sys.stderr)
            response = int (input("Enter your choice: "))
        
        resource_name = resources [response - 1]
        permissions = self._permissions_menu ()

        self.role_manager.update_role_resource (role_name, resource_name, permissions)
        
    def _run_create_role_menu(self):
        print("Creating a new role")
        role_name = input("Enter rolename: ")

        # Add role
        self.role_manager.add_role(role_name=role_name)

        # Add resources
        print(f"Select resources with permissions for {role_name}")
        print(f"press 0 to save role")

        # Get resource name
        resource_names = sorted(list(
            self.resource_manager.get_resources()))
        for idx, resource_name in enumerate(resource_names, 1):
            print(f"{idx} {resource_name}")

        while True:
            resource_idx = input("* Select resource number: ")
            if resource_idx == '0':
                return
            resource_idx = int(resource_idx) - 1
            resource_name = resource_names[resource_idx]

            print(
                "Enter permissions for create, read, update, delete as 1/0 (E.g.: 0110 for read and update permissions)."
            )
            perm = input("enter permission: ")
            permissions = ActionType(*[True if x == '1' else False for x in list(perm)])
            self.role_manager.add_role_resource(role_name, resource_name,
                                                permissions)
        return            

    def _run_edit_role_menu(self) -> None:
        selected_role = self._edit_role_menu()

        while True:
            self._print_edit_role_resources_menu()
            response = input("Enter your choice: ")
            while response not in ['0', '1', '2', '3', '4']:
                print("Invalid input, try again", file=sys.stderr)
                response = input("Enter your choice: ")
            
            if response == '0':
                return
            elif response == '1':
                self._print_role_resource_permissions (selected_role)
            elif response == '2':
                self._edit_role_resource_menu (selected_role)
            print ()
        return

    def _print_user_menu(self) -> None:
        print("press 2 for view roles")
        print("press 3 for access resource")

    def _run_user_menu(self, user, response) -> bool:
        if response == '2':
            user_name = user.name
            user_roles = user.get_roles()
            print("Assigned role/roles to " + user_name + " : ", end=' ')
            for idx, role in enumerate(user_roles, 1):
                print(str(idx) + '.) ' + role, end=' ')

        elif response == '3':
            user_name = user.name
            user_roles = user.get_roles()
            resources = list(self.resource_manager.get_resources())
            print("Select the resource you want to access : ")
            for idx, resource in enumerate(resources, 1):
                print("Press " + str(idx) + " for " + resource)
            resource = int(input())
            actions = ActionType.get_action_types()
            for idx, action_type in enumerate(actions, 1):
                print("Press " + str(idx) + " for " + action_type)
            action_type = int(input())
            for role in user_roles:
                if self.role_manager.check_resource_permission(
                        role, resources[resource - 1],
                        actions[action_type - 1]):
                    print('Resource Accessed!')
                    return
            print('Resource Access Denied!')

    def _init_users(self):
        users = {
            'blog_admin': {
                'roles': ['admin']
            },
            'editor_1': {
                'roles': ['editor', 'viewer']
            },
            'viewer_1': {
                'roles': ['viewer']
            },
        }

        users_dict = {}
        for username, user_info in users.items():
            if 'admin' in user_info['roles']:
                users_dict[username] = Admin(username, user_info['roles'], self.role_manager,
                                             self.resource_manager)
            else:
                users_dict[username] = User(username, user_info['roles'])
        return users_dict

    def _init_roles(self):
        roles = {
            'admin': {},
            'editor': {
                'blog_page': {
                    'create': False,
                    'read': True,
                    'update': True,
                    'delete': False
                },
                'article': {
                    'create': True,
                    'read': True,
                    'update': True,
                    'delete': True
                },
                'comment': {
                    'create': True,
                    'read': True,
                    'update': True,
                    'delete': True
                }
            },
            'viewer': {
                'blog_page': {
                    'create': False,
                    'read': True,
                    'update': False,
                    'delete': False
                },
                'article': {
                    'create': False,
                    'read': True,
                    'update': False,
                    'delete': False
                },
                'comment': {
                    'create': True,
                    'read': True,
                    'update': True,
                    'delete': True
                }
            }
        }

        return roles

    def _init_resources(self):
        resources = ['blog_page', 'article', 'comment']

        return resources
