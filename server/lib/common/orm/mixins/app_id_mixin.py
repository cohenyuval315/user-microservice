from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class AppIdMixin:
    """define a series of common elements that may be applied to mapped
    classes using this class as a mixin class."""

    app_id: Mapped[str] = mapped_column(String(), nullable=True, default=None) # TODO later Nullable = False
    
    

    

    
