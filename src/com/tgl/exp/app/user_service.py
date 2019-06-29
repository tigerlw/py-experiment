from src.com.tgl.exp.domain.user_entity import UserEntity


def create_user(name,age):
    user = UserEntity(name,age)

    return user
