from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

def setup_secure_protocol(app:FastAPI):
    """
        app:FastAPI
    """
    app.add_middleware(HTTPSRedirectMiddleware)
