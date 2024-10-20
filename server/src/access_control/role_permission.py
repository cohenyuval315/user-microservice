from typing import Optional
from lib.common.orm.base import Base
from sqlalchemy import ForeignKey,Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
# from role import Role
# from permission import Permission

class RolePermission(Base):
    __tablename__ = "role_permissions"
    role_id: Mapped[str] = mapped_column(ForeignKey("roles.id", ondelete='CASCADE'), primary_key=True)
    permission_id: Mapped[str] = mapped_column(ForeignKey("permissions.id", ondelete='CASCADE'), primary_key=True)
    
    extra_data: Mapped[Optional[str]]
    is_granted: Mapped[bool] = mapped_column(Boolean, default=True)

    role: Mapped["Role"] = relationship(back_populates="permissions") # type: ignore
    permission: Mapped["Permission"] = relationship(back_populates="roles") # type: ignore
    

    def __repr__(self):
        return f"<RolePermission(role_id={self.role_id}, permission_id={self.permission_id}, is_granted={self.is_granted})>"