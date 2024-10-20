from unicorn import UnicornMiddleware
from fastapi import FastAPI
from typing import Any


def setup_unicorn(app:FastAPI,**kwargs:Any):
    app.add_middleware(UnicornMiddleware,kwargs=kwargs)