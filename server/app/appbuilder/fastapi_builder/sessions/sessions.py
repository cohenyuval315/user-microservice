from fastapi import FastAPI
from fastapi_sessions import SessionMiddleware,get_session,RedisSession


def setup_session_middleware(app:FastAPI,secret_key):
    session_middleware = SessionMiddleware(
        session_name="myapp_session",
        secret_key=secret_key,
        store=RedisSession(redis),
    )
    app.add_middleware(session_middleware)

def setup_redis_session_middleware(app:FastAPI,session_name:str,secret_key:str):
    session_middleware = SessionMiddleware(
        session_name=session_name,
        secret_key=secret_key,
        store=RedisSession(redis),
    )
    app.add_middleware(session_middleware)
