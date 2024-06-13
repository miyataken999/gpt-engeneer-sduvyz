from models.user import User

class UserRepository:
    """User repository"""
    def get_all_users(self):
        # TO DO: implement database connection and query
        return [User(id=1, name='John Doe', email='john@example.com')]