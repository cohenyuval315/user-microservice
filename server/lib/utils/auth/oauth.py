from authlib.integrations.starlette_client import OAuth
from fastapi.security import OAuth2AuthorizationCodeBearer,OAuth2

def get_oauth_client(providers):
    oauth_client = OAuth2()
    oauth_client.register(
        name="google",
        client_id="YOUR_GOOGLE_CLIENT_ID",
        client_secret="YOUR_GOOGLE_CLIENT_SECRET",
        authorize_url="https://accounts.google.com/o/oauth2/auth",
        authorize_params=None,
        access_token_url="https://accounts.google.com/o/oauth2/token",
        access_token_params=None,
        refresh_token_url=None,
        redirect_uri="http://localhost:8000/auth/callback",
        
        client_kwargs={
            "scope": "openid profile email"
        },
    )
    return oauth_client