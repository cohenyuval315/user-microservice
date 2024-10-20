from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
# from config import SERVE_FRONTEND,FROTNEND_FOLDER

def setup_static_html_serve(app:FastAPI,directory:str):
    app.mount("/", StaticFiles(
            directory=directory, 
            html=True, 
            check_dir=True,
            follow_symlink=False,
            packages=None
        ), name="static",
    )
