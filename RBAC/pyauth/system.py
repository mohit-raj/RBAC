import sys
from .admin import Admin
from .user import User
from .rolemanager import RoleManager
from .resourcemanager import ResourceManager


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
                while response not in ['0', '1', '2', '3']:
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
                self._run_user_menu(response)

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
        return user

    def _login(self, username: str) -> None:
        return self.users.get(username, None)

    def _print_admin_menu(self):
        print("press 2 for create user")
        print("press 3 for edit role")

    def _run_admin_menu(self, response):
        if response == "2":
            # TODO: Create user
            ...
        elif response == "3":
            # TODO: Edit role
            ...

    def _print_user_menu(self):
        print("press 2 for view roles")
        print("press 3 for access resource")

    def _run_user_menu(self, response) -> bool:
        if response == '2':
            # TODO: View roles
            ...
        elif response == '3':
            # TODO: access resources
            ...

    def _init_users(self):
        users = {
            'blog_admin': {
                'roles': [ 'admin' ]
            },
            'editor_1': {
                'roles': [ 'editor' ]
            },
            'viewer_1': {
                'roles': [ 'viewer' ]
            }
        }

        users_dict = {}
        for username, user_info in users.items():
            if 'admin' in user_info['roles']:
                users_dict[username] = Admin(username, self.role_manager,
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
