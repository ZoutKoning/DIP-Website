import boto3
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

class CognitoBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        # Initialize Cognito client
        client = boto3.client('cognito-idp', region_name='us-east-1')

        try:
            resp = client.admin_initiate_auth(
                UserPoolId='us-east-1_mwt8Tw8od',
                ClientId='24572ehjeno50ma5122ql3oumd',
                AuthFlow='ADMIN_NO_SRP_AUTH',
                AuthParameters={
                    'USERNAME': username,
                    'PASSWORD': password,
                },
            )

            # If authentication was successful
            if resp.get('ChallengeName') == 'NEW_PASSWORD_REQUIRED':
                # You can handle the password change requirement here
                # For now, we just pass
                pass
            elif resp.get('AuthenticationResult'):
                # Try to get or create a local Django user
                user_model = get_user_model()
                user, created = user_model.objects.get_or_create(username=username)
                return user
        except client.exceptions.NotAuthorizedException:
            pass
        return None

    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
