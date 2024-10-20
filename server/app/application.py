import sys 
sys.path.append("..")
sys.path.append("src")

from contextlib import asynccontextmanager
from fastapi import FastAPI
from server.src.base_router import base_router
from server.app.appbuilder.fastapi_builder.cors import setup_cors_middleware

from server.app.services.monitoring import setup_monitoring
from server.app.appbuilder.fastapi_builder.error_handler import setup_error_handler
from server.app.services.db import db


# from server.app.appbuilder.fastapi_builder.unicorn import setup_unicorn
# from server.app.appbuilder.fastapi_builder.trusted_host import setup_trusted_host
# from server.app.appbuilder.fastapi_builder.secure_protocol import setup_secure_protocol
# from server.app.appbuilder.fastapi_builder.gzip import setup_gzip
# from server.app.appbuilder.fastapi_builder.serve import setup_static_html_serve
# from server.app.appbuilder.fastapi_builder.middlewares.validation import setup_validation



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    await db.start()
    # ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
    yield
    # Clean up the ML models and release the resources
    # ml_models.clear()
    # shutdown


def create_app() -> FastAPI:
    
    app = FastAPI(lifespan=lifespan)
    
    app.include_router(base_router)
    # setup_validation(app,"http")
    setup_cors_middleware(app)
    setup_monitoring(app)
    setup_error_handler(app)
    
    # setup_unicorn(app)
    # setup_static_html_serve(app) # maybe for the each part 
    # setup_secure_protocol(app)
    # setup_trusted_host(app)
    # setup_gzip(app)
    

    return app

