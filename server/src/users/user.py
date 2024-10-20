from __future__ import annotations
from lib.common.orm.base import Base
from sqlalchemy import String, Boolean, DateTime,LargeBinary,JSON,Enum
from sqlalchemy.orm import Mapped, mapped_column,relationship
from typing import Optional
from .user_constants import GenderEnum, MaritalStatusEnum,PreferredContactMethodEnum
from datetime import date,datetime

class User(Base):
    __tablename__ = 'users'
    
    email: Mapped[Optional[str]] = mapped_column(String, unique=True, index=True, nullable=True)
    username: Mapped[Optional[str]] = mapped_column(String, unique=True, index=True, nullable=True)
    hashed_password: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    nickname: Mapped[Optional[str]] = mapped_column(String, unique=True, index=True, nullable=True)
    first_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    last_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    street: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    city: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    state: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    postal_code: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    country: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    timezone: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    mobile: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    gender: Mapped[Optional[GenderEnum]] = mapped_column(Enum(GenderEnum), nullable=True)
    marital_status: Mapped[Optional[MaritalStatusEnum]] = mapped_column(Enum(MaritalStatusEnum), nullable=True)
    nationality: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    preferred_language: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    preferred_contact_method: Mapped[Optional[PreferredContactMethodEnum]] = mapped_column(Enum(PreferredContactMethodEnum), nullable=True)
    occupation: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    last_login: Mapped[Optional[date]] = mapped_column(DateTime(timezone=True), nullable=True)
    birth_date: Mapped[Optional[date]] = mapped_column(DateTime(timezone=True), nullable=True)
    avatar: Mapped[Optional[bytes]] = mapped_column(LargeBinary, default=None, nullable=True)  # Store image as BYTEA  | # avatar: Mapped[Optional[str]] = mapped_column(String, nullable=True)  # URL or path
    is_disabled: Mapped[bool] = mapped_column(Boolean, default=False, nullable=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=True)
    
    additional_fields: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)  # Store dynamic user fields
    
    
    roles: Mapped[list['UserRole']] = relationship('UserRole', back_populates='user') # type: ignore

    @property
    def full_name(self)-> Optional[str]:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return None

    @property
    def age(self) -> Optional[int]:
        """Calculate age based on birth_date."""
        if self.birth_date:
            today = date.today()
            age = today.year - self.birth_date.year
            # Adjust for the case where the birthdate hasn't occurred yet this year
            if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
                age -= 1
            return age
        return None

    @property
    def full_address(self) -> Optional[str]:
        """Concatenate address components into a formatted address string."""
        address_parts = [
            self.street,
            self.city,
            self.state,
            self.postal_code,
            self.country
        ]
        formatted_parts = [part for part in address_parts if part]
        if formatted_parts:
            return ', '.join(formatted_parts)
        return None


    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
    