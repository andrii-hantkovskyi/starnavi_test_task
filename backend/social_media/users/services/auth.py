from django.contrib.auth import get_user_model

User = get_user_model()


def register_user(email, password) -> User:
    if not all((email, password)):
        raise ValueError('Not all fields provided')

    user = User.objects.create_user(email, password)
    return user
