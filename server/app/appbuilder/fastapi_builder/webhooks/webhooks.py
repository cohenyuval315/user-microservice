from fastapi import APIRouter,Request

def setup_webhooks(router:APIRouter):
    @router.get('/webhooks/')
    async def recv_webhook(request:Request):
        pass
        # return pass
    

    