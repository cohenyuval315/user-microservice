from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()

def setup_gzip(app:FastAPI,minimum_size:int=1000,compresslevel:int=5):
    app.add_middleware(GZipMiddleware, minimum_size=minimum_size, compresslevel=compresslevel)

