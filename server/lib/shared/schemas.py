from pydantic import BaseModel, Field,ConfigDict
from typing import Optional, List, Any, Dict
from enum import Enum
from typing import Type


# def create_pydantic_model(model: Type[Base]) -> Type[BaseModel]:
#     attributes = {c.name: (c.type_, ...) for c in model.__table__.columns}
#     return type(f'{model.__name__}Schema', (BaseModel,), attributes)


class PaginationSchema(BaseModel):
    total: Optional[int] = None
    page: Optional[int] = None
    page_size: Optional[int] = None
    
    
class MetaSchema(BaseModel):
    pagination: Optional[PaginationSchema] = None
    

class BaseResponseSchema(BaseModel):
    data: Optional[Any] = None  # When returning actual data
    message: Optional[str] = None  # Success or info message
    error: Optional[str] = None  # Error message in case of failure
    status_code: Optional[int] = Field(default=200, description="HTTP status code")
    meta: Optional[MetaSchema] = None  # Metadata, often for pagination
    warnings: Optional[List[str]] = None  # Warnings or additional information



class BaseSchema(BaseModel):
    APP_API_KEY: str
    TENANT_API_KEY: str


class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"

class BaseManySchema(BaseSchema):
    model_config:ConfigDict = ConfigDict(
        from_attributes=True
    )    
    offset: int = Field(default=0, ge=0)
    limit: int = Field(default=10, ge=1)
    sort_by: Optional[str] = None
    sort_order: SortOrder = SortOrder.asc
    filters: Optional[Dict[str, Any]] = None  # Flexible filters
    tags: Optional[List[str]] = None  # Flexible filters

    
        


