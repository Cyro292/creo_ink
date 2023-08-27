from datetime import timedelta

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings

# Token settings
api_settings.DEFAULTS['ACCESS_TOKEN_LIFETIME'] = timedelta(minutes=60)  # Set the token lifetime
api_settings.DEFAULTS['REFRESH_TOKEN_LIFETIME'] = timedelta(days=1)  # Set the refresh token lifetime
api_settings.DEFAULTS['ROTATE_REFRESH_TOKENS'] = False  # Disable automatic rotation of refresh tokens
api_settings.DEFAULTS['BLACKLIST_AFTER_ROTATION'] = True  # Blacklist old refresh tokens after rotation
