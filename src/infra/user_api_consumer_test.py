from src.errors import HttpRequestError
from .user_api_consumer import UserApiConsumer

def test_get_random_user(requests_mock):
    ''' Test the get_random_iser method of UserApiConsumer class. '''

    requests_mock.get('https://randomuser.me/api/', status_code=200, json={'results': [{'name': {'first': 'John', 'last': 'Doe'}}]})

    user_api_consumer = UserApiConsumer()
    get_random_user = user_api_consumer.get_random_user()

    assert get_random_user.request.method == 'GET'
    assert get_random_user.request.url == 'https://randomuser.me/api/'
    assert get_random_user.status_code == 200
    assert isinstance(get_random_user.response['results'], list)

def test_get_user_http_error(requests_mock):
    ''' Test the get_random_iser method of UserApiConsumer class. '''

    requests_mock.get('https://randomuser.me/api/', status_code=200, json={'detail': 'something'})

    user_api_consumer = UserApiConsumer()

    try:
        user_api_consumer.get_random_user()
        assert True is True
    except HttpRequestError as error:
        assert error.message is not None
        assert error.status_code is not None
        print(error.message)
        print(type(error))
