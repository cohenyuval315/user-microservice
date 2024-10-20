from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class TenantIdMixin:
    tenant_id: Mapped[str] = mapped_column(String(), nullable=True, default=None) # TODO later Nullable = False
    
    

    

    
