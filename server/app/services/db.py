from lib.common.orm.database import Database
from src.users.user import User
from src.access_control.role import Role
from src.access_control.permission import Permission
from src.access_control.role_permission import RolePermission
from src.access_control.role_hierarchy import RoleHierarchy
from src.access_control.user_role import UserRole

db = Database()

def init_db():
    pass