
from django.contrib.auth.hashers import check_password
from .models import Users as User
from django.db.models import Q





class EmailPhoneUsernameAuthenticationBackend(object):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(
                Q(username=username) | Q(email=username)
            )

        except User.DoesNotExist:
            return None

        if user and check_password(password, user.password):
            return user

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None