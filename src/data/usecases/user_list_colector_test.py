from src.infra import UserApiConsumer
from .user_list_colector import UserListColector

def test_list():
    ''' Test the list method of UserListColector '''
    api_consumer = UserApiConsumer()
    user_list_colector = UserListColector(api_consumer)

    response = user_list_colector.list()

    assert isinstance(response, list)
    assert "id" in response[0]
    assert "full_name" in response[0]
