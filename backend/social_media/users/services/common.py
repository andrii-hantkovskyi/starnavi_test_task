from django.contrib.auth import get_user_model

User = get_user_model()


def get_all_users() -> list[User]:
    return User.objects.all()


def get_user_by_id(user_id) -> User:
    return User.objects.get(id=user_id)
