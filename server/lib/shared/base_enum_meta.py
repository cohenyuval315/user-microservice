import enum 

class BaseEnumMeta(enum.EnumMeta):  
    def __contains__(cls, item): 
        return item in cls.__members__.values()
    
    def __str__(cls):
        return ', '.join(cls.__members__.values())