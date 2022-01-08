from users.serializers import TokenUserSerializer


def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': TokenUserSerializer(user, context={'request': request}).data
    }
