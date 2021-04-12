# py-auth

A python authentication program.

## Flow

* Display list of users -> Prompt to select user.
* Admin login:
  * Display menu
    1. Create a User.
        1. Enter user name -> Add roles.
    1. Create Role.
        1. Select resource -> Add permissions.
    1. Edit Role
        1. Select a role
            1. Add resource.
            2. Remove resource.
            3. Edit resource permissions.
        1. Remove roles.
    1. Access resource.
        1. Select resource -> Select action type -> Show auth status.
    1. Logout
    1. Exit
* User (Non-Admin) login:
  * Display menu
    1. View roles.
    1. Access resource.
        1. Select resource -> Select action type -> Show auth status.
    1. Logout
    1. Exit

## OOP concepts

* Implement Admin and non-admin classes.
* Add features as functions to respective classes.

## Files

* main<nolink>.py
  * Driver code for the program.
  * Has the menu loop.

## Classes

* **System**:
  * Attributes:
    * users : list
    * role_manager : RoleManager
    * resource_manager : ResourceManager
  * Functions:
    * init ()
    * run ()

* **ActionType**:
  * Attributes:
    * create : boolean
    * read : boolean
    * update : boolean
    * delete : boolean

* **RoleManager (Base class):**
  * Maintains a single object with all roles and permissions.
  * Attributes:
    * role_name : { <br>
            &nbsp;&nbsp;resource_name : { <br>
                &nbsp;&nbsp;&nbsp;&nbsp;action_type : boolean <br>
        &nbsp;&nbsp;&nbsp;&nbsp;} <br>
        &nbsp;&nbsp;}
  * Funtions:
    * add_role (role_name : str)
    * remove_role (role_name : str)
    * add_role_resource (role_name : str, resource_name : str, permissions : Action_type)
    * remove_role_resource (role_name : str, resource_name : str)
    * update_role_resource (role_name : str, resource_name : str, permissions : Action_type)
    * get_resource_permissions (role_name : str, resource_name : str)
    * check_resource_permission (role_name : str, resource_name : str, action_type : str)
    * remove_resource (resource_name : str/List)

* **ResourceManager (Base class)**:
  * Maintains the resources object.
  * Attributes:
    * resources : set ()
  * Functions:
    * add_resource (resource_name : str/List)
    * get_resources ()
    * remove_resource (resource_name : str/List)

* **User (Base class)**:
  * Attributes:
    * name : str
    * roles : set()
  * Functions:
    * get_roles ()

* **Admin (Sub class)**:
  * Inherits from  User.
  * Attributes:
    * role_manager : RoleManager
    * resource_manager : ResourceManager
  * Functions:
    * create_user (user_name : str, roles : array)

## Assumptions

1. Operations are limted to CRUD (Create, Read, Update and Delete).

## Assignment Link

* <https://github.com/mohit-raj/backend-developer-assignment/blob/main/README.md>