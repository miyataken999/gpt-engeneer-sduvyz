from repositories.user_repository import UserRepository

class UserService:
    """User service"""
    def __init__(self):
        self.repository = UserRepository()

    def get_all_users(self):
        return self.repository.get_all_users()