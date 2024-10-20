from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import uuid
from ..constants import ID_LENGTH,MAX_ID_LENGTH,MIN_ID_LENGTH
from lib.utils.id.generate_id import generate_id

class IdMixin:
    """Id Mixin Class"""
    __abstract__ = True
    
    id: Mapped[str] = mapped_column(
        String(ID_LENGTH), 
        primary_key=True, 
        default=lambda: generate_id(
            id_length=ID_LENGTH,
            min_id_length=MIN_ID_LENGTH,
            max_id_length=MAX_ID_LENGTH
        )
    )
    
    

    

    
