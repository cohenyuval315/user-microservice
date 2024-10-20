# from typing import Optional, Union, Dict, Any, List,Tuple
# from .error_type import ErrorType
# from .error_severity import ErrorSeverity
# from lib.common.constants import HTTP_STATUS_MESSAGES,HTTPStatusCode,HttpMediaType
# import traceback



# class AppError(Exception):
#     app_name:str
#     #level =
    
#     def __init__(
#         self,
#         error:Any=None,
#         title:str="",
#         description: Optional[str] = "",
#         context: Optional[str] = "",
#         operable: Optional[bool] = True,
#         severity: Optional[ErrorSeverity] = ErrorSeverity.NONE_OPERATIONAL,
#         error_type: Optional[ErrorType] = ErrorType.HTTP_ERROR,
#         http_status_code: Optional[HTTPStatusCode] = None,
#         user_message: Optional[str] = None,
#         headers: Optional[Dict[str, str]] = None,
#         *args: Optional[Tuple[Any, ...]],
#         **kwargs: Optional[Dict[str, Any]]
#     ):
#         super().__init__(error)
#         self.error = error
#         self.title = title
#         self.description = description
#         self.context = context
#         self.operable = operable
#         self.severity = severity
#         self.error_type = error_type
#         self.http_status_code = http_status_code
#         self.http_message = HTTP_STATUS_MESSAGES[self.http_status_code] if self.http_status_code else None
#         self.user_message = user_message
#         self.headers = headers
#         self.args = args
#         self.kwargs = kwargs
        
            
#     @classmethod
#     def set_context(cls, app_name):
#         cls.app_name = app_name
        
#     def get_message(self) -> str:
#         return self.user_message if self.user_message else self.http_message
    
#     def _info(self):
#         pass
    
#     def _debug(self):
#         pass

#     def _trace(self):
#         pass

#     def _warn(self):
#         pass

#     def _error(self):
#         pass

#     def _fatal(self):
#         pass
    
#     def __str__(self):
#         string = super().__str__()
#         return string
        

    
    
    

from typing import Optional, Union, Dict, Any, List, Tuple
from .error_type import ErrorType
from .error_severity import ErrorSeverity
from lib.common.constants import HTTP_STATUS_MESSAGES, HTTPStatusCode, HttpMediaType
import traceback

class AppError(Exception):
    app_name: Optional[str] = None  # Class-level attribute for app context

    def __init__(
        self,
        error: Any = None,
        title: str = "",
        description: Optional[str] = "",
        context: Optional[str] = "",
        operable: Optional[bool] = True,
        severity: Optional[ErrorSeverity] = ErrorSeverity.NONE_OPERATIONAL,
        error_type: Optional[ErrorType] = ErrorType.HTTP_ERROR,
        http_status_code: Optional[HTTPStatusCode] = HTTPStatusCode.INTERNAL_SERVER_ERROR,  # Default to 500
        user_message: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        *args: Optional[Tuple[Any, ...]],
        **kwargs: Optional[Dict[str, Any]]
    ):
        # Initialize base Exception with error message
        super().__init__(str(error) if error else "An application error occurred")
        
        # Instance attributes
        self.error = error
        self.title = title
        self.description = description
        self.context = context
        self.operable = operable
        self.severity = severity
        self.error_type = error_type
        self.http_status_code = http_status_code
        self.http_message = HTTP_STATUS_MESSAGES.get(self.http_status_code, "Unknown Error")
        self.user_message = user_message
        self.headers = headers if headers else {}
        self.args = args
        self.kwargs = kwargs
        
    @classmethod
    def set_context(cls, app_name: str):
        """Set application name context as a class-level attribute."""
        cls.app_name = app_name
        
    def get_message(self) -> str:
        """Return user message if available, otherwise the HTTP message."""
        return self.user_message if self.user_message else self.http_message
    
    def __str__(self):
        """Return a string representation of the error."""
        return f"{self.title}: {self.get_message()}"
    
    def _info(self):
        """Log informational level error details."""
        return f"INFO: {self.__str__()}"
    
    def _debug(self):
        """Log debugging information about the error."""
        return f"DEBUG: {traceback.format_exc()}"
    
    def _trace(self):
        """Log traceback for in-depth debugging."""
        return f"TRACE: {traceback.format_exc()}"

    def _warn(self):
        """Log warning level error."""
        return f"WARNING: {self.__str__()}"
    
    def _error(self):
        """Log the error message."""
        return f"ERROR: {self.__str__()}"

    def _fatal(self):
        """Log fatal error message."""
        return f"FATAL: {self.__str__()}"


