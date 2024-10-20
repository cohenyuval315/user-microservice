import enum

class HttpMediaType(enum.Enum):
    APPLICATION_JSON = "application/json"
    APPLICATION_XML = "application/xml"
    TEXT_HTML = "text/html"
    TEXT_PLAIN = "text/plain"
    TEXT_CSS = "text/css"
    APPLICATION_JAVASCRIPT = "application/javascript"
    IMAGE_PNG = "image/png"
    IMAGE_JPEG = "image/jpeg"
    IMAGE_GIF = "image/gif"
    MULTIPART_FORM_DATA = "multipart/form-data"
    APPLICATION_OCTET_STREAM = "application/octet-stream"
    APPLICATION_PDF = "application/pdf"
    AUDIO_MPEG = "audio/mpeg"
    VIDEO_MP4 = "video/mp4"
