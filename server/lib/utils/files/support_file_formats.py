from typing import List
from .file_formats import FileFormat

class Meta(type):
    pass

class SupportedFiles(metaclass=SingletonMeta):
    file_formats: List[str] = []
    max_file_size: int = None
    min_file_size: int = None
    languages: List[str] = []

    @classmethod
    def initialize(cls, file_formats: List[FileFormat] = None, languages: List[str] = None, max_file_size: int = None, min_file_size: int = None) -> None:
        """
        Initialize class-level settings for supported files, globally.
        This sets the allowed formats, languages, and size limits for all instances.
        """
        cls.file_formats = file_formats if file_formats else []
        cls.languages = languages if languages else []
        cls.max_file_size = max_file_size
        cls.min_file_size = min_file_size

    @classmethod
    def _is_valid_format(cls, extension: str) -> bool:
        """
        Check if the file format is valid based on the allowed file formats.
        """
        if not cls.file_formats:
            return True  # If no formats are specified, allow all
        return extension in cls.file_formats

    @classmethod
    def _is_valid_file_size(cls, file_size: int) -> bool:
        """
        Check if the file size is within the allowed range.
        """
        if cls.max_file_size and file_size > cls.max_file_size:
            return False
        if cls.min_file_size and file_size < cls.min_file_size:
            return False
        return True

    @classmethod
    def _is_valid_language(cls, file_format:str, language: str) -> bool:
        """
        Check if the language is valid based on the allowed languages.
        """
        if file_format in None:
            pass
        
        if not cls.languages:
            return True  # If no languages are specified, allow all
        return language.lower() in [lang.lower() for lang in cls.languages]

    @classmethod
    def is_valid_file(cls, filename: str, file_size: int, language: str = None) -> bool:
        """
        Main method to validate the file based on file size, format, and language.
        """
        if not cls._is_valid_file_size(file_size):
            raise ValueError(f"Invalid file size: {file_size}.")
        
        if not cls._is_valid_format(filename):
            raise ValueError(f"Invalid file format for file: {filename}.")
        
        if language and not cls._is_valid_language(language):
            raise ValueError(f"Invalid file language: {language}.")
        
        return True  # If all checks pass, the file is valid
