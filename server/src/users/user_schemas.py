from lib.shared.schemas import BaseSchema,BaseManySchema,BaseResponseSchema
from typing import List,Optional,Dict,Any,Literal
from datetime import datetime,date
from pydantic import BaseModel, HttpUrl,constr,field_validator,Field,EmailStr,StringConstraints
import re
import pycountry
import pytz
from lib.utils.language.language import Language
from .user_constants import GenderEnum,MaritalStatusEnum, NotificationMethodEnum,PreferredContactMethodEnum,ConsentStatus,PrivacyPolicyVersion
from typing_extensions import Annotated

class AddressSchema(BaseModel):
    street : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Street", description="Street address") 
    
    city : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="City", description="City name") 

    state : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="State", description="State or region") 
        
    postal_code : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Postal Code", description="Postal or ZIP code")    
    
    country : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Country", description="Country code (ISO Alpha-2)")
    
    # @field_validator('postal_code')
    # def validate_postal_code(self, v):
    #     """
    #         v
    #     """
    #     if v and not re.match(r'^\d{4,10}$', v):  # Adjust as needed
    #         raise ValueError("Invalid postal code format.")
    #     return v

    # @field_validator('country')
    # def validate_country(self, v):
    #     """
    #         v
    #     """
    #     if v and not pycountry.countries.get(alpha_2=v):
    #         raise ValueError("Invalid country code.")
    #     return v
    
    
class UserIdentifierSchema(BaseModel):
    id : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="User ID", description="Unique identifier for the user")
    email : Annotated[
                    Optional[EmailStr],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Email", description="User email address")
    username : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Username", description="User's username")
    
    mobile : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=r'^\+?[1-9]\d{1,14}$',                        
                    ),
                ] = Field(None, title="Mobile", description="International mobile number")   
    
    password : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=r'^\+?[1-9]\d{1,14}$',                        
                    ),
                ] = Field(None, title="Password", description="Password")    

    # @field_validator("id")
    # def validate_id(self, v):
    #     return v
        
    # @field_validator("email")
    # def validate_email(self, v):
    #     return v    
    
    # @field_validator("mobile")
    # def validate_mobile(self, v):
    #     return v
    
    # @field_validator("username")
    # def validate_username(self, v):
    #     return v
    
    # @field_validator("password")
    # def validate_password(self, v):
    #     return v
    
    
class UserProfileSchema(BaseModel):
    nickname : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=r'^\+?[1-9]\d{1,14}$',                        
                    ),
                ] = Field(None, title="Nickname", description="User's nickname") 
        
    address: Optional[AddressSchema] = Field(None, title="Address", description="User's address details")
    
    first_name : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="First Name", description="User's first name")    
    
    middle_name : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Middle Name", description="User's Middle name")     
    
    last_name : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Last Name", description="User's last name")
    
    gender : Annotated[
                    Optional[GenderEnum],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Gender", description="Gender of the user")
    
    marital_status : Annotated[
                    Optional[MaritalStatusEnum],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Marital Status", description="Marital status of the user")

    nationality : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Nationality", description="Nationality code (ISO Alpha-2)")
    
    birth_date : Annotated[
                    Optional[date],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Birth Date", description="User's birth date")
    
    avatar : Optional[bytes] = Field(None, title="Avatar", description="User's profile picture")
    
    avatar_url : Optional[HttpUrl] = Field(None, title="Avatar URL", description="URL to the user's avatar image")
    
    occupation : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Occupation", description="User's occupation")

    organization : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Organization", description="User's Organization")
        
    
    
    # @field_validator("nationality")
    # def validate_nationality(cls, v):
    #     if v and not pycountry.countries.get(alpha_2=v.upper()):
    #         raise ValueError("Invalid nationality code.")
    #     return v.upper() if v else v


class UserConsentSchema(BaseModel):
    privacy_policy_version : Annotated[
                    Optional[PrivacyPolicyVersion],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Privacy Policy Version", description="Version of the privacy policy accepted by the user")
    
    privacy_policy_accepted : Annotated[
                    Optional[ConsentStatus],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Privacy Policy Accepted", description="Whether the user has accepted the privacy policy")
    
    terms_of_service_accepted : Annotated[
                    Optional[ConsentStatus],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Terms of Service Accepted", description="Whether the user has accepted the terms of service")

    marketing_consent : Annotated[
                    Optional[ConsentStatus],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Marketing Consent", description="Consent for marketing communications")
    
    consent_date : Annotated[
                    Optional[datetime],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Consent Date", description="Date and time when consent was given")


class UserNotificationPreferencesSchema(BaseModel):
    receive_newsletters : Annotated[
                    Optional[bool],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Receive Newsletters", description="Whether the user wants to receive newsletters")    
    
    receive_product_updates : Annotated[
                    Optional[bool],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Receive Product Updates", description="Whether the user wants to receive product updates")        
    
    preferred_notification_methods : Annotated[
                    Optional[List[NotificationMethodEnum]],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Preferred Notification Methods", description="Preferred methods for receiving notifications")            
    
    
class UserSettings(BaseModel):
    timezone : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Timezone", description="IANA timezone string")
        
        
    preferred_language : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Preferred Language", description="Language code (e.g., 'en', 'es')")
    
    preferred_contact_method : Annotated[
                    Optional[PreferredContactMethodEnum],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Preferred Contact Method", description="Preferred method of contact")

    notification_preferences : Optional[UserNotificationPreferencesSchema] = Field(None, title="User Notification Preferences", description="User Notification Preferences")
    consent : Optional[UserConsentSchema] = Field(None, title="User Consent Statuses", description="User Consent Statuses")

    # @field_validator("timezone")
    # def validate_timezone(cls, v):
    #     if v and v not in pytz.all_timezones:
    #         raise ValueError("Invalid timezone.")
    #     return v
    
    # @field_validator("preferred_language")
    # def validate_preferred_language(cls, v):
    #     valid_languages = {"en", "es", "fr", "de"}
    #     if v and v not in valid_languages:
    #         raise ValueError(f"Invalid language code. Must be one of: {', '.join(valid_languages)}")
    #     return v


class UserRoleSchema(BaseModel):
    role_id : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Role ID", description="Unique identifier for the role")
    
    role_name : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Role Name", description="Name of the role")        
    
    
class UserAccessControlSchema(BaseModel):
    roles : Annotated[
                    Optional[List[UserRoleSchema]],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Roles", description="List of roles assigned to the user")        


class UserLocationSchema(BaseModel):
    latitude: float = Field(None, ge=-90, le=90, title="Latitude", description="Geographic latitude")
    longitude: float = Field(None, ge=-180, le=180, title="Longitude", description="Geographic longitude")
    timestamp: datetime = Field(None, title="Timestamp", description="Time of the location record")


class UserAdditionalFieldsSchema(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, title="Additional Fields", description="Any additional user data")    
    
    # @field_validator("additional_fields")
    # def validate_custom_fields(cls, v):
    #     if not isinstance(v, dict):
    #         raise ValueError("Custom fields must be a dictionary.")
    #     return v
    
    
class BaseUserSchema(BaseModel):
    # auth: Optional[UserIdentifierSchema] = Field(None, title="Authentication", description="User authentication details")
    # profile: Optional[UserProfileSchema] = Field(None, title="Profile", description="User's personal information")
    # settings: Optional[UserSettings] = Field(None, title="Settings", description="User's settings and preferences")
    # access_control: Optional[UserAccessControlSchema] = Field(None, title="Roles", description="User's roles and permissions")
    # location: Optional[UserLocationSchema] = Field(None, title="Location", description="User's location data")
    # additional_fields: Optional[UserAdditionalFieldsSchema] = Field(None, title="Additional Fields", description="Any additional user data")
    
    
    # User's identifier
    id : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="User ID", description="Unique identifier for the user")
    email : Annotated[
                    Optional[EmailStr],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Email", description="User email address")
    username : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Username", description="User's username")
    
    mobile : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=r'^\+?[1-9]\d{1,14}$',                        
                    ),
                ] = Field(None, title="Mobile", description="International mobile number")   
    
    password : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=r'^\+?[1-9]\d{1,14}$',                        
                    ),
                ] = Field(None, title="Password", description="Password")    

    
    
    # profile
    nickname : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=r'^\+?[1-9]\d{1,14}$',                        
                    ),
                ] = Field(None, title="Nickname", description="User's nickname") 
        
    address: Optional[AddressSchema] = Field(None, title="Address", description="User's address details")
    
    first_name : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="First Name", description="User's first name")    
    
    middle_name : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Middle Name", description="User's Middle name")     
    
    last_name : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Last Name", description="User's last name")
    
    gender : Annotated[
                    Optional[GenderEnum],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Gender", description="Gender of the user")
    
    marital_status : Annotated[
                    Optional[MaritalStatusEnum],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Marital Status", description="Marital status of the user")

    nationality : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Nationality", description="Nationality code (ISO Alpha-2)")
    
    birth_date : Annotated[
                    Optional[date],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Birth Date", description="User's birth date")
    
    avatar : Optional[bytes] = Field(None, title="Avatar", description="User's profile picture")
    
    avatar_url : Optional[HttpUrl] = Field(None, title="Avatar URL", description="URL to the user's avatar image")
    
    occupation : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Occupation", description="User's occupation")

    organization : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Organization", description="User's Organization")
        
    
    
    # consent
    privacy_policy_version : Annotated[
                    Optional[PrivacyPolicyVersion],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Privacy Policy Version", description="Version of the privacy policy accepted by the user")
    
    privacy_policy_accepted : Annotated[
                    Optional[ConsentStatus],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Privacy Policy Accepted", description="Whether the user has accepted the privacy policy")
    
    terms_of_service_accepted : Annotated[
                    Optional[ConsentStatus],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Terms of Service Accepted", description="Whether the user has accepted the terms of service")

    marketing_consent : Annotated[
                    Optional[ConsentStatus],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Marketing Consent", description="Consent for marketing communications")
    
    consent_date : Annotated[
                    Optional[datetime],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Consent Date", description="Date and time when consent was given")



    # settings
    timezone : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Timezone", description="IANA timezone string")
        
        
    preferred_language : Annotated[
                    Optional[str],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Preferred Language", description="Language code (e.g., 'en', 'es')")
    
    preferred_contact_method : Annotated[
                    Optional[PreferredContactMethodEnum],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Preferred Contact Method", description="Preferred method of contact")

    # settings notification preferences
    receive_newsletters : Annotated[
                    Optional[bool],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Receive Newsletters", description="Whether the user wants to receive newsletters")    
    
    receive_product_updates : Annotated[
                    Optional[bool],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Receive Product Updates", description="Whether the user wants to receive product updates")        
    
    preferred_notification_methods : Annotated[
                    Optional[List[NotificationMethodEnum]],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Preferred Notification Methods", description="Preferred methods for receiving notifications")            
        
    consent : Optional[UserConsentSchema] = Field(None, title="User Consent Statuses", description="User Consent Statuses")
    


    
    # user roles
    roles : Annotated[
                    Optional[List[UserRoleSchema]],
                    StringConstraints(
                        strip_whitespace=True, 
                        to_upper=None, 
                        to_lower=None,
                        strict=None,
                        max_length=None,
                        min_length=None,                        
                        pattern=None,                        
                    ),
                ] = Field(None, title="Roles", description="List of roles assigned to the user")        

    
    
    # location
    latitude: float = Field(None, ge=-90, le=90, title="Latitude", description="Geographic latitude")
    longitude: float = Field(None, ge=-180, le=180, title="Longitude", description="Geographic longitude")
    timestamp: datetime = Field(None, title="Timestamp", description="Time of the location record")
    
    # additional fields - w.e
    additional_fields: Optional[Dict[str, Any]] = Field(None, title="Additional Fields", description="Any additional user data")    


class UserCreateSchema(BaseUserSchema): 
    first_name: Optional[str] = Field(None, title="User's First Name", description="User's First Name")
    pass

class UserUpdateSchema(BaseUserSchema):
    updates:Optional[Any] = None

class UsersGetManySchema(BaseManySchema): 
    model_config = {"extra": "forbid"}
    sort_by: Optional[Literal["created_at", "updated_at"]] = "created_at"

class UserResponseSchema(BaseResponseSchema):
    data: Optional[Any] = None

class UsersResponseSchema(BaseResponseSchema):   
    data: Optional[Any] = None# {"users": List[BaseUserSchema]}

    








class BaseUsersManySchema(BaseManySchema):
    user_ids: Optional[List[str]] = None    
    
    
class UsersUpdateManySchema(BaseUsersManySchema):
    pass

class UsersDeleteManySchema(BaseUsersManySchema):
    pass
    

    



