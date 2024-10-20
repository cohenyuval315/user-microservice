import typing
from datetime import datetime,timedelta,timezone
from enum import Enum
import jwt
import uuid


class JWTAlgorithm(Enum):
    HS256 = "HS256"  # HMAC with SHA-256
    HS384 = "HS384"  # HMAC with SHA-384
    HS512 = "HS512"  # HMAC with SHA-512
    RS256 = "RS256"  # RSA with SHA-256
    RS384 = "RS384"  # RSA with SHA-384
    RS512 = "RS512"  # RSA with SHA-512
    ES256 = "ES256"  # ECDSA with SHA-256
    ES384 = "ES384"  # ECDSA with SHA-384
    ES512 = "ES512"  # ECDSA with SHA-512
    PS256 = "PS256"  # RSA-PSS with SHA-256
    PS384 = "PS384"  # RSA-PSS with SHA-384
    PS512 = "PS512"  # RSA-PSS with SHA-512
    EdDSA = "EdDSA"  # Edwards-curve Digital Signature Algorithm
    

class JWTTokenType(Enum):
    ACCESS_TOKEN = "access_token"
    REFRESH_TOKEN = "refresh_token"
    ID_TOKEN = "id_token"
    
def create_jwt_token(secret_key:str,  data: dict, expires_delta: timedelta, token_type:JWTTokenType, algorithm:JWTAlgorithm=JWTAlgorithm.HS256):
    to_encode = data.copy()
    to_encode.update({
        "jti": str(uuid.uuid4()),  # JWT Token ID
        "iat": datetime.now(timezone.utc),  # Issued At
        "exp": datetime.now(timezone.utc) + expires_delta,
        "token_type":token_type.value
    })
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm.value)
    return encoded_jwt


def decode_jwt_token(secret_key:str, token: str, algorithms:typing.List[JWTAlgorithm]=[JWTAlgorithm.HS256]):
    try:
        return jwt.decode(token, secret_key, algorithms=algorithms)
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")
    

async def refresh_access_token(secret_key:str,refresh_token: str, data: dict, expires_delta: timedelta, algorithm:JWTAlgorithm=JWTAlgorithm.HS256, algorithms:typing.List[JWTAlgorithm]=[JWTAlgorithm.HS256]):
    payload = decode_jwt_token(secret_key, refresh_token, algorithms=algorithms)        
    if payload.get("token_type") != JWTTokenType.REFRESH_TOKEN.value:
        # raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid type for token")
        return None
    new_access_token = create_jwt_token(secret_key,data,expires_delta,JWTTokenType.ACCESS_TOKEN,algorithm)
    return new_access_token    
    # try:

    
    # except jwt.ExpiredSignatureError:
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token has expired")
    
    # except jwt.JWTError:
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")