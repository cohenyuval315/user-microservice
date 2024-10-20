from lib.common.constants.http_status_code import HTTPStatusCode

HTTP_STATUS_MESSAGES = {
    HTTPStatusCode.CONTINUE: "Continue",
    HTTPStatusCode.SWITCHING_PROTOCOLS: "Switching Protocols",
    HTTPStatusCode.PROCESSING: "Processing",
    HTTPStatusCode.EARLY_HINTS: "Early Hints",
    HTTPStatusCode.OK: "OK",
    HTTPStatusCode.CREATED: "Created",
    HTTPStatusCode.ACCEPTED: "Accepted",
    HTTPStatusCode.NON_AUTHORITATIVE_INFORMATION: "Non-Authoritative Information",
    HTTPStatusCode.NO_CONTENT: "No Content",
    HTTPStatusCode.RESET_CONTENT: "Reset Content",
    HTTPStatusCode.PARTIAL_CONTENT: "Partial Content",
    HTTPStatusCode.MULTI_STATUS: "Multi-Status",
    HTTPStatusCode.ALREADY_REPORTED: "Already Reported",
    HTTPStatusCode.IM_USED: "IM Used",
    HTTPStatusCode.MULTIPLE_CHOICES: "Multiple Choices",
    HTTPStatusCode.MOVED_PERMANENTLY: "Moved Permanently",
    HTTPStatusCode.FOUND: "Found",
    HTTPStatusCode.SEE_OTHER: "See Other",
    HTTPStatusCode.NOT_MODIFIED: "Not Modified",
    HTTPStatusCode.USE_PROXY: "Use Proxy",
    HTTPStatusCode.TEMPORARY_REDIRECT: "Temporary Redirect",
    HTTPStatusCode.PERMANENT_REDIRECT: "Permanent Redirect",
    HTTPStatusCode.BAD_REQUEST: "Bad Request",
    HTTPStatusCode.UNAUTHORIZED: "Unauthorized",
    HTTPStatusCode.PAYMENT_REQUIRED: "Payment Required",
    HTTPStatusCode.FORBIDDEN: "Forbidden",
    HTTPStatusCode.NOT_FOUND: "Not Found",
    HTTPStatusCode.METHOD_NOT_ALLOWED: "Method Not Allowed",
    HTTPStatusCode.NOT_ACCEPTABLE: "Not Acceptable",
    HTTPStatusCode.PROXY_AUTHENTICATION_REQUIRED: "Proxy Authentication Required",
    HTTPStatusCode.REQUEST_TIMEOUT: "Request Timeout",
    HTTPStatusCode.CONFLICT: "Conflict",
    HTTPStatusCode.GONE: "Gone",
    HTTPStatusCode.LENGTH_REQUIRED: "Length Required",
    HTTPStatusCode.PRECONDITION_FAILED: "Precondition Failed",
    HTTPStatusCode.PAYLOAD_TOO_LARGE: "Payload Too Large",
    HTTPStatusCode.URI_TOO_LONG: "URI Too Long",
    HTTPStatusCode.UNSUPPORTED_MEDIA_TYPE: "Unsupported Media Type",
    HTTPStatusCode.RANGE_NOT_SATISFIABLE: "Range Not Satisfiable",
    HTTPStatusCode.EXPECTATION_FAILED: "Expectation Failed",
    HTTPStatusCode.IM_A_TEAPOT: "I'm a teapot",
    HTTPStatusCode.INTERNAL_SERVER_ERROR: "Internal Server Error",
    HTTPStatusCode.NOT_IMPLEMENTED: "Not Implemented",
    HTTPStatusCode.BAD_GATEWAY: "Bad Gateway",
    HTTPStatusCode.SERVICE_UNAVAILABLE: "Service Unavailable",
    HTTPStatusCode.GATEWAY_TIMEOUT: "Gateway Timeout",
    HTTPStatusCode.HTTP_VERSION_NOT_SUPPORTED: "HTTP Version Not Supported",
}
