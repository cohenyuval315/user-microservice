from .app_error import AppError, ErrorSeverity, ErrorType, HTTPStatusCode, HTTP_STATUS_MESSAGES, HttpMediaType
from fastapi import Request
from lib.common.loggers import logger
from fastapi import Response
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
import traceback
# from fastapi.exception_handlers import websocket_request_validation_exception_handler,request_validation_exception_handler,http_exception_handler

class ErrorHandler:
    @staticmethod
    async def handle_error(request: Request, app_error: Exception) -> Response:
        try:
            default_headers = {
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0",
                "X-Content-Type-Options": "nosniff",
                "X-Frame-Options": "DENY",
                "X-XSS-Protection": "1; mode=block",
                "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
                "Content-Security-Policy": "default-src 'self'",
                "Referrer-Policy": "no-referrer",
            }

            # Prepare the error response dictionary
            error_response = {
                "error": HTTP_STATUS_MESSAGES.get(HTTPStatusCode.INTERNAL_SERVER_ERROR, "Internal Server Error")
            }
            status_code = HTTPStatusCode.INTERNAL_SERVER_ERROR.value  # Default to 500

            # Check if the exception is an instance of AppError
            if isinstance(app_error, AppError):
                logger.error(f"Found AppError: {app_error}")
                # Use AppError's message and status code
                error_response["error"] = app_error.get_message()
                status_code = app_error.http_status_code.value if app_error.http_status_code else status_code
            
            else:
                logger.error("Unhandled exception:", str(app_error))

            logger.error(f"An error occurred:\n {traceback.format_exc()}" )

            # Create JSON response
            response = JSONResponse(
                content=error_response,
                status_code=status_code,
                headers=default_headers,
                media_type=HttpMediaType.APPLICATION_JSON.value
            )
            return response
        
        except Exception as e:
            logger.critical(f"ERROR HANDLER IS HORRIBLE:  {str(e)}")
            # Return a default internal server error response if the error handler fails
            
            return JSONResponse(
                content={
                    "error": "An unexpected error occurred in the error handler."
                },
                status_code=HTTPStatusCode.INTERNAL_SERVER_ERROR.value,
                headers=default_headers,
                media_type=HttpMediaType.APPLICATION_JSON.value
            )
