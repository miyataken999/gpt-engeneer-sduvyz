from services.user_service import UserService
from utils.utils import hello_world

def main():
    hello_world()
    user_service = UserService()
    users = user_service.get_all_users()
    for user in users:
        print(user)

if __name__ == '__main__':
    main()