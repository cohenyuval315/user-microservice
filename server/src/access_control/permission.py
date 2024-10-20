from lib.common.orm.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column,relationship
from typing import Optional, List

class Permission(Base):
    __tablename__ = 'permissions'

    action: Mapped[str] = mapped_column(String, nullable=False)  # e.g., 'read', 'write', 'delete'
    resource: Mapped[str] = mapped_column(String, nullable=False)  # e.g., 'user', 'file', 'report'
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    # Relationships
    roles: Mapped[List['RolePermission']] = relationship('RolePermission', back_populates='permission')

    def __repr__(self):
        return f"<Permission(id={self.id}, action={self.action}, resource={self.resource})>"