class SingletonMeta:
    """A generic singleton class."""
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
            # Initialize the instance if needed
            if 'initialize' in kwargs:
                instance.initialize(*args, **kwargs['initialize'])
        return cls._instances[cls]