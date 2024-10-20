from typing import Optional
from lib.common.orm.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class RoleHierarchy(Base):
    __tablename__ = "role_hierarchy"
    
    parent_role_id: Mapped[str] = mapped_column(ForeignKey('roles.id', ondelete='CASCADE'), primary_key=True)
    child_role_id: Mapped[str] = mapped_column(ForeignKey('roles.id', ondelete='CASCADE'), primary_key=True)
    
    extra_data: Mapped[Optional[str]]
    
    parent_role: Mapped['Role'] = relationship('Role', foreign_keys=[parent_role_id], back_populates='child_roles') # type: ignore
    child_role: Mapped['Role'] = relationship('Role', foreign_keys=[child_role_id], back_populates='parent_roles') # type: ignore


    def __repr__(self):
        return f"<RoleHierarchy(parent_role_id={self.parent_role_id}, child_role_id={self.child_role_id}, inherited_at={self.created_at})>"