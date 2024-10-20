import enum
from lib.shared.base_enum_meta import BaseEnumMeta

class GenderEnum(str,enum.Enum,metaclass=BaseEnumMeta):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"
    
class MaritalStatusEnum(str, enum.Enum,metaclass=BaseEnumMeta):
    SINGLE = "single"
    MARRIED = "married"
    DIVORCED = "divorced"
    WIDOWED = "widowed"
    OTHER = "other"
    
class PreferredContactMethodEnum(str, enum.Enum,metaclass=BaseEnumMeta):
    EMAIL = "email"
    PHONE = "phone"
    SMS = "sms"
    NONE = "none"
    

class ConsentStatus(str, enum.Enum,metaclass=BaseEnumMeta):
    accepted = "accepted"
    declined = "declined"
    

class PrivacyPolicyVersion(str, enum.Enum,metaclass=BaseEnumMeta):
    v1 = "1.0"
    
class NotificationMethodEnum(str, enum.Enum,metaclass=BaseEnumMeta):
    email = "email"
    sms = "sms"
    push = "push"
