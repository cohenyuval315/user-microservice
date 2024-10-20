from lib.common.orm.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column,  relationship
from typing import List, Optional
from .role_hierarchy import RoleHierarchy
# from role_permission import RolePermission
# from user_role import UserRole

class Role(Base):
    __tablename__ = 'roles'
    
    name: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    # Relationships
    users: Mapped[List['UserRole']] = relationship('UserRole', back_populates='role') # type: ignore
    permissions: Mapped[List['RolePermission']] = relationship('RolePermission', back_populates='role') # type: ignore

    parent_roles: Mapped[List['RoleHierarchy']] = relationship()

    # Hierarchical relationships
    parent_roles: Mapped[List['RoleHierarchy']] = relationship('RoleHierarchy', foreign_keys=[RoleHierarchy.child_role_id], back_populates='child_role')
    child_roles: Mapped[List['RoleHierarchy']] = relationship('RoleHierarchy', foreign_keys=[RoleHierarchy.parent_role_id], back_populates='parent_role')

    def __repr__(self):
        return f"<Role(id={self.id}, name={self.name}) desc={self.description}>"