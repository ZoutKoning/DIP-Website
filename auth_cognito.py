from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
# from jose.backends.cryptography_backend import CryptographyECKey
from jose.constants import ALGORITHMS
import jose.jwt

User = get_user_model()

class CognitoAuthenticationBackend(BaseBackend):
    def authenticate(self, request, id_token = None):
        if not id_token: # No ID token provided
            return None # No ID token provided

        #Verify and decode the ID token using jose.jwt library
        try:
            claims = jose.jwt.decode(
                id_token,
                '1infvrlnju43ncak5m7l9rhtpru052tnbdv9u5l5mvum7hrvovcj',
                algorithms=ALGORITHMS.RS256,
                audience= '24572ehjeno50ma5122ql3oumd'
            )

            # Get the subject claim from the ID token
            sub = claims.get('sub')

            # Find/create a Django user that corresponds to the Cognito user
            user, created = User.objects.get_or_create(username=sub)

            return user
        except (jose.exceptions.JWTError, User.DoesNotExist):
            return None # Authentication failed

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


