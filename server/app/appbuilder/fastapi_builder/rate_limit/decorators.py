from functools import wraps
from ..exceptions import WebSocketRateLimitException
from fastapi import WebSocket
from fastapi_limiter.depends import WebSocketRateLimiter

def websocket_rate_limit(ratelimiter: WebSocketRateLimiter, context_key: str = None):
    def decorator(func):
        @wraps(func)
        async def wrapper(websocket: WebSocket, *args, **kwargs):
            try:
                await ratelimiter(websocket, context_key=context_key)
                return await func(websocket, *args, **kwargs)
            except WebSocketRateLimitException:
                await websocket.send_text(f"Rate limit exceeded. Please try again later.")
        return wrapper
    return decorator