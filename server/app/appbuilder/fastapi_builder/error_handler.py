from fastapi import FastAPI,Request
from server.lib.common.errors.error_handler import ErrorHandler

def setup_error_handler(app:FastAPI):
    @app.exception_handler(Exception)
    async def exception_handler(request:Request, exc:Exception):
        return await ErrorHandler.handle_error(request,exc)
        
        
