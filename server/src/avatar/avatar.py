from typing import Annotated
from fastapi import File, UploadFile,APIRouter, Request
from lib.utils.files.temporary_file_handler import TemporaryFileHandler
from lib.utils.files.filename import normalize_filename,MAX_FILENAME_LENGTH
from lib.utils.files.is_valid_file import is_valid_file_format,is_valid_file_size
from backend.server.lib.utils.files._file_format import get_file_format
from config import ALLOWED_FILE_EXTENSIONS,MAX_FILE_SIZE


def upload_avatar_endpoint(router:APIRouter):
    @router.post("/upload")
    async def upload_file(file: UploadFile,request: Request, *args, **kwargs):
        file_size = len(file)
        file_format = get_file_format(file.filename)
        
        if not is_valid_file_size(file_size,MAX_FILE_SIZE):
            return {} #TODO
        
        if not is_valid_file_format(file_format,ALLOWED_FILE_EXTENSIONS):
            return {} #TODO
        
        filename = normalize_filename(file.filename)
        
        return {
            "file_action":"upload",
            "normal_filename": file.filename,
            "filename": filename,
            "file_size": file_size,
            "file_format":file_format
        }

def read_file_endpoint(router:APIRouter):
    @router.post("/read")
    async def read_file(file: UploadFile, request: Request, *args, **kwargs):
        TEMP_FILE_HANDLER_THRESHOLD = 1000
        file_size = len(file)
        
        if file_size > TEMP_FILE_HANDLER_THRESHOLD:
            tfh = TemporaryFileHandler()
            file_data = file.read()
            file_path = tfh.save_file(
                file_data=file_data,
                filename=file.filename,
                user_id=1#user_id # TODO
            ) 
            
            tfh.delete_file(file_path)
        
        
        return {
            "file_action":"read",
            "filename": file.filename,
            "file_size": file_size
        }



def create_file_endpoint(router:APIRouter):
    @router.post("/create")
    async def create_file(file: Annotated[bytes, File()], request: Request, *args, **kwargs):
        return {
            "file_action":"create",
            
        }
    
    
def update_file_endpoint(router:APIRouter):
    @router.put("/delete")
    async def update_file(file_id:str,file: UploadFile, request: Request, *args, **kwargs):
        return {
            "file_action":"update",
            "file_id":file_id,
            "filename": file.filename
        }
    

def delete_file_endpoint(router:APIRouter):
    @router.delete("/delete")
    async def delete_file(file_id:str, request: Request, *args, **kwargs):
        return {
            "file_action":"delete",
            "filename": file_id
        }



