
from core.domain.user import User
from core.infrastructure.user_repository import UserRepository

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, name: str, email: str, password: str) -> User:
        user = User(id=None, name=name, email=email, password=password)  # ID is set in DB
        return self.user_repo.save(user)

    def get_user(self, user_id: int) -> User:
        return self.user_repo.get_by_id(user_id)
