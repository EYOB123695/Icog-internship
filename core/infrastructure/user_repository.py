 
from core.models import UserModel

from core.domain.user import User

class UserRepository:
    def save(self, user: User) -> User:
        user_obj = UserModel.objects.create(name=user.name, email=user.email, password=user.password)
        return User(id=user_obj.id, name=user_obj.name, email=user_obj.email, password=user_obj.password)

    def get_by_id(self, user_id: int) -> User:
        user_obj = UserModel.objects.get(id=user_id)
        return User(id=user_obj.id, name=user_obj.name, email=user_obj.email, password=user_obj.password)
