from fastapi import APIRouter
from .ping import register_ping_endpoint
from .health import register_health_endpoint
from .version import register_version_endpoint
from .uptime import register_uptime_endpoint

common_router = APIRouter()
register_ping_endpoint(common_router)
register_health_endpoint(common_router)
register_uptime_endpoint(common_router)
register_version_endpoint(common_router)
