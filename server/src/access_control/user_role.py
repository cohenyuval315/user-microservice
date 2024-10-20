from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship,mapped_column,Mapped
from lib.common.orm.base import Base
# from src.users.user import User
# from role import Role

class UserRole(Base):
    __tablename__ = 'user_roles'
    
    
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id',  ondelete='CASCADE') , primary_key=True)
    role_id: Mapped[str] = mapped_column(ForeignKey('roles.id' ,ondelete='CASCADE'), primary_key=True)
    

    user: Mapped['User'] = relationship(back_populates="roles") # type: ignore
    role: Mapped['Role'] = relationship(back_populates="users") # type: ignore


    def __repr__(self):
        return f"<UserRole(user_id={self.user_id}, role_id={self.role_id}, assigned_at={self.created_at})>"