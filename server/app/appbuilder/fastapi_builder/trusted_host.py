from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware


def setup_trusted_host(app:FastAPI):
    allowed_hosts = ["example.com", "*.example.com"]
    app.add_middleware(
        TrustedHostMiddleware, allowed_hosts=allowed_hosts
    )
