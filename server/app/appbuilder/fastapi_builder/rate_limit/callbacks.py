from fastapi import Request,Response
import math
from lib.common.errors import AppError,ErrorSeverity,ErrorType
from lib.common.constants import HTTPStatusCode

async def to_many_requests_callback(request: Request, response: Response, pexpire: int):
    """
    default callback when too many requests
    :param request:
    :param pexpire: The remaining milliseconds
    :param response:
    :return:
    """
    expire = math.ceil(pexpire / 1000)
    raise AppError(
        None,
        "too many requests",
        "too many requests time x bla y , endpont bla ",
        "endpoint ",
        True,
        ErrorSeverity.NONE_OPERATIONAL,
        ErrorType.HTTP_ERROR,
        HTTPStatusCode.TOO_MANY_REQUESTS,
        "retry after",
        {"Retry-After": str(expire)}
           
    )
    
    # raise HTTPException(
    #     HTTP_429_TOO_MANY_REQUESTS, "Too Many Requests", headers={"Retry-After": str(expire)}
    # )