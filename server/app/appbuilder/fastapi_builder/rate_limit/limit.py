import typing

import redis.asyncio as redis
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI,Request,Response, WebSocket
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter,WebSocketRateLimiter



def rate_limiter(times:int,milliseconds:int, seconds:int,minutes:int,hours:int, identifier:typing.Callable,callback:typing.Callable) -> RateLimiter:
    return RateLimiter(
        times=times, 
        seconds=seconds,
        callback=callback,
        hours=hours,
        milliseconds=milliseconds,
        identifier=identifier,
        minutes=minutes
    )
    
def rate_limiter_ws(times:int,milliseconds:int, seconds:int,minutes:int,hours:int, identifier:typing.Callable,callback:typing.Callable) -> WebSocketRateLimiter:
    return WebSocketRateLimiter(
        times=times, 
        seconds=seconds,
        callback=callback,
        hours=hours,
        milliseconds=milliseconds,
        identifier=identifier,
        minutes=minutes
    )
    

def redis_rate_limiter(redis_url:str):
    @asynccontextmanager
    async def lifespan(_: FastAPI):
        redis_connection = redis.from_url(redis_url, encoding="utf8")
        await FastAPILimiter.init(redis_connection)
        yield
        await FastAPILimiter.close()
        
    return lifespan
        






