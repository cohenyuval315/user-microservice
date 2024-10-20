from typing import List,Dict
import magic

class FileFormat:
    def __init__(self, extension: str, mime_type: str, description: str, is_binary: bool):
        self.extension = extension
        self.mime_type = mime_type
        self.description = description
        self.is_binary = is_binary
        
    def __str__(self) -> str:
        return self.extension
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value,FileFormat):
            return self.extension.lower() == value.extension.lower() and self.mime_type.lower() == value.mime_type.lower() and self.is_binary == value.is_binary
        elif isinstance(value,str):
            return self.extension.lower() == value.lower() or  "." + self.extension.lower() == value.lower() or self.mime_type.lower() == value.lower()
        return False
        
class FileFormats:
    BINARY = "bin"
    PDF = "pdf"
    DOCX = "docx"
    DOC = "doc"
    XML = "xml"
    HTML = "html"
    YAML = "yaml"
    INI = "ini"
    MD = "md"
    TXT = "txt"
    JSON = "json"
    PROTOBUF = "proto"
    AVRO = "avro"
    CSV = "csv"
    SVG = "svg"
    PNG = "png"
    JPEG = "jpeg"
    BMP = "bmp"
    XLS = "xls"
    XLSX = "xlsx"
    MP4 = "mp4"
    PARQUET = "parquet"
    ORC = "orc"
    TIFF = "tiff"
    GIF = "gif"
    ZIP = "zip"
    EXE = "exe"
    MD5 = "md5"
    SHA256 = "sha256"
    
    formats: Dict[str, FileFormat] = {
        PDF: FileFormat(
            extension=PDF,
            mime_type="application/pdf",
            description="Portable Document Format. Commonly used for documents, contains text, images, and can be encrypted or signed.",
            is_binary=True
        ),
        DOCX: FileFormat(
            extension=DOCX,
            mime_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            description="Microsoft Word Document. A binary format for documents with rich formatting, images, and other elements.",
            is_binary=True
        ),
        DOC: FileFormat(
            extension=DOC,
            mime_type="application/msword",
            description="Older Microsoft Word Document format, primarily binary-based but can contain text, images, and other elements.",
            is_binary=True
        ),
        XML: FileFormat(
            extension=XML,
            mime_type="application/xml",
            description="Extensible Markup Language. A text-based format used to represent structured data. Widely used in web technologies.",
            is_binary=False
        ),
        HTML: FileFormat(
            extension=HTML,
            mime_type="text/html",
            description="HyperText Markup Language. Used to define the structure of web pages. Text-based but can include references to binary files like images.",
            is_binary=False
        ),
        YAML: FileFormat(
            extension=YAML,
            mime_type="application/x-yaml",
            description="YAML Ain't Markup Language. A text-based format for configuration files, often used in cloud-native applications.",
            is_binary=False
        ),
        INI: FileFormat(
            extension=INI,
            mime_type="text/plain",
            description="INI Configuration File. A simple text-based format used for configuration settings in many systems and software.",
            is_binary=False
        ),
        MD: FileFormat(
            extension=MD,
            mime_type="text/markdown",
            description="Markdown. A lightweight markup language primarily used for formatting plain text with simple formatting syntax.",
            is_binary=False
        ),
        TXT: FileFormat(
            extension=TXT,
            mime_type="text/plain",
            description="Plain Text. A basic format containing unformatted text.",
            is_binary=False
        ),
        JSON: FileFormat(
            extension=JSON,
            mime_type="application/json",
            description="JavaScript Object Notation. A lightweight, text-based format for data exchange, commonly used in APIs.",
            is_binary=False
        ),
        CSV: FileFormat(
            extension=CSV,
            mime_type="text/csv",
            description="Comma-Separated Values. A text-based format used to represent tabular data, where values are separated by commas.",
            is_binary=False
        ),
        PROTOBUF: FileFormat(
            extension=PROTOBUF,
            mime_type="application/x-protobuf",
            description="Protocol Buffers. A language-neutral, columnar binary format used to serialize structured data. Efficient for communication between services.",
            is_binary=True
        ),
        AVRO: FileFormat(
            extension=AVRO,
            mime_type="application/avro",
            description="Apache Avro. A binary format used for data serialization, often in data processing systems. Unlike Protobuf, it's not columnar.",
            is_binary=True
        ),
        SVG: FileFormat(
            extension=SVG,
            mime_type="image/svg+xml",
            description="Scalable Vector Graphics. A text-based format for vector images, often used in web and graphic design.",
            is_binary=False
        ),
        PNG: FileFormat(
            extension=PNG,
            mime_type="image/png",
            description="Portable Network Graphics. A binary format for raster images, supports lossless compression.",
            is_binary=True
        ),
        JPEG: FileFormat(
            extension=JPEG,
            mime_type="image/jpeg",
            description="Joint Photographic Experts Group. A binary format for lossy-compressed raster images.",
            is_binary=True
        ),
        BMP: FileFormat(
            extension=BMP,
            mime_type="image/bmp",
            description="Bitmap Image. A binary format used for raster images, supports uncompressed storage.",
            is_binary=True
        ),
        XLS: FileFormat(
            extension=XLS,
            mime_type="application/vnd.ms-excel",
            description="Microsoft Excel Spreadsheet (Legacy). A binary format for spreadsheets containing data in cells, supports formulas, charts, etc.",
            is_binary=True
        ),
        XLSX: FileFormat(
            extension=XLSX,
            mime_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            description="Microsoft Excel Spreadsheet (Modern). A binary format for spreadsheets with support for formulas, charts, and rich formatting.",
            is_binary=True
        ),
        MP4: FileFormat(
            extension=MP4,
            mime_type="video/mp4",
            description="MPEG-4 Video. A binary format for video files that supports both video and audio.",
            is_binary=True
        ),
        PARQUET: FileFormat(
            extension=PARQUET,
            mime_type="application/x-parquet",
            description="Apache Parquet. A columnar, binary format used for efficient data storage, commonly used in big data processing.",
            is_binary=True
        ),
        ORC: FileFormat(
            extension=ORC,
            mime_type="application/x-orc",
            description="Optimized Row Columnar. A binary format optimized for reading and writing large datasets in Hadoop-based systems.",
            is_binary=True
        ),
        TIFF: FileFormat(
            extension=TIFF,
            mime_type="image/tiff",
            description="Tagged Image File Format. A binary format for raster images, supports lossless compression and is often used in professional imaging.",
            is_binary=True
        ),
        GIF: FileFormat(
            extension=GIF,
            mime_type="image/gif",
            description="Graphics Interchange Format. A binary format for simple raster images, supports animation and limited color palettes.",
            is_binary=True
        ),
        ZIP: FileFormat(
            extension=ZIP,
            mime_type="application/zip",
            description="ZIP Archive. A binary format used for file compression and archiving, supports compression of multiple files into one archive.",
            is_binary=True
        ),
        EXE: FileFormat(
            extension=EXE,
            mime_type="application/vnd.microsoft.portable-executable",
            description="Executable File. A binary format used for Windows executables, contains compiled code that can be executed by the operating system.",
            is_binary=True
        ),
        MD5: FileFormat(
            extension=MD5,
            mime_type="text/plain",
            description="MD5 Hash. A cryptographic hash function used to verify the integrity of files or strings. The output is a fixed-length binary string, often represented as hexadecimal.",
            is_binary=True
        ),
        SHA256: FileFormat(
            extension=SHA256,
            mime_type="text/plain",
            description="SHA-256 Hash. A cryptographic hash function used for integrity verification. Outputs a 256-bit binary string, commonly used in cryptography.",
            is_binary=True
        ),
        BINARY: FileFormat(
            extension=BINARY,
            mime_type="application/octet-stream",
            description="Simple Binary File. A raw binary file format without a predefined structure. Commonly used for arbitrary binary data.",
            is_binary=True
        )
    }


    def __init__(self, extension: str):
        """
        Initialize the FileFormat class with a specific file extension.
        :param extension: file extension (e.g., 'pdf', 'docx')
        """
        self.extension = extension.lower()
        if self.extension not in self.formats:
            raise ValueError(f"Unsupported file format: {self.extension}")
        self.data = self.formats[self.extension]
        
    @classmethod
    def _create_instance(cls, extension: str):
        """
        Private method to create a new instance of the class.
        """
        return cls(extension)
    
    @classmethod
    def get_format_from_extension(cls, extension: str):
        """
        Validate if the given file extension is supported and return an instance.
        """
        if extension.lower() in cls.formats:
            return cls._create_instance(extension)

    @classmethod
    def get_format_from_mime_type(cls, mime_type: str):
        """
        Get the format based on its MIME type.
        """
        for format_data in cls.formats.values():
            if format_data.mime_type == mime_type:
                return format_data
        # raise ValueError(f"No file format found for MIME type: {mime_type}")

    @classmethod
    def get_format_from_binary(cls, file_path: str):
        """
        Determine the file format from the binary data using the python-magic library.
        """
        mime = magic.Magic(mime=True)
        mime_type = mime.from_file(file_path)
        if mime_type:
            return cls.get_format_from_mime_type(mime_type)
        else:
            raise ValueError(f"Could not find MIME type for file path: {file_path}")

    @classmethod
    def validate_format(cls, extension: str):
        """
        Validate if the given file extension is supported.
        """
        return extension.lower() in cls.formats
    
    @classmethod
    def list_formats(cls) -> list:
        """
        List all supported file formats.
        """
        return list(cls.formats.keys())

    @classmethod
    def add_format(cls, extension: str, mime_type: str, description: str, is_binary: bool) -> bool:
        """
        Add a new file format dynamically.
        """
        extension = extension.lower()
        if extension not in cls.formats:   
            cls.formats[extension] = {
                "mime_type": mime_type,
                "description": description,
                "is_binary": is_binary
            }
            return extension
        
    @classmethod
    def add_multiple_formats(cls, formats_list: List[Dict[str, str]]):
        """
        Add multiple formats dynamically.
        """
        added = []
        for format_data in formats_list:
            added.append(cls.add_format(
                format_data['extension'], 
                format_data['mime_type'], 
                format_data['description'], 
                format_data['is_binary']
            ))
        return added

    @classmethod
    def remove_format(cls, extension: str):
        """
        Remove a file format dynamically if it exists.
        """
        extension = extension.lower()
        if extension in cls.formats:
            del cls.formats[extension]
            return extension
        
    @classmethod
    def remove_all_formats(cls):
        """
        Remove all formats from the dictionary.
        """
        cls.formats.clear()
    
    def get_mime_type(self):
        """
        Return the MIME type for the file format.
        """
        return self.data.mime_type

    def get_description(self) -> str:
        """
        Return a human-readable description for the file format.
        """
        return self.data.description

    def is_binary(self) -> bool:
        """
        Check if the file format is binary.
        """
        return self.data.is_binary


    def __str__(self) -> str:
        return self.extension
    
    
if __name__ == "__main__":
    import unittest
    class TestFileFormat(unittest.TestCase):
        
        def test_binary_format(self):
            binary_format = FileFormats.get_format_from_extension(FileFormats.BINARY)
            self.assertEqual(binary_format.get_mime_type(), "application/octet-stream")
            self.assertEqual(binary_format.get_description(), "Simple Binary File. A raw binary file format without a predefined structure. Commonly used for arbitrary binary data.")
            self.assertTrue(binary_format.is_binary())

        def test_pdf_format(self):
            pdf_format = FileFormats.get_format_from_extension(FileFormats.PDF)
            self.assertEqual(pdf_format.get_mime_type(), "application/pdf")
            self.assertTrue(pdf_format.is_binary())

        def test_invalid_format(self):
            self.assertIsNone(FileFormats.get_format_from_extension("unknown"))

        def test_list_formats(self):
            formats = FileFormats.list_formats()
            self.assertIn(FileFormats.PDF, formats)
            self.assertIn(FileFormats.BINARY, formats)
            
    unittest.main()
