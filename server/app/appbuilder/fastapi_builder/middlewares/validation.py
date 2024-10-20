from fastapi.responses import JSONResponse
from pydantic import ValidationError
from fastapi import FastAPI, Request



def setup_validation(app:FastAPI,protocol:str="http"):
    @app.middleware(protocol)
    async def validation_handler(request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except ValidationError as ve:
            # If a validation error occurs, handle it here
            return JSONResponse(
                status_code=422,
                content={"detail": "Validation error occurred", "errors": ve.errors()},
            )
        