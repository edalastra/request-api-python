from .user_list_colector import UserListColector
from src.infra import UserApiConsumer

def test_list():
    api_consumer = UserApiConsumer()
    user_list_colector = UserListColector(api_consumer)

    user_list_colector.list()