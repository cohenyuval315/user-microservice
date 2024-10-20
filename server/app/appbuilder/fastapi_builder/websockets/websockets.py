from fastapi import APIRouter,Request
from fastapi.websockets import WebSocket,WebSocketDisconnect,WebSocketState

def setup_webhooks(router:APIRouter):
    @router.get('/websocket')
    async def connect_websocket(websocket,request:Request):
        pass
    
    

    