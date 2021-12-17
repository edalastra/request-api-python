from .user_api_consumer import UserApiConsumer

def test_get_random_movie():
    ''' Test the get_random_iser method of UserApiConsumer class. '''    
   
    # requests_mock.get('https://randomuser.me/api/', status_code=200, json={'results': [{'name': {'first': 'John', 'last': 'Doe'}}]})
   
    user_api_consumer = UserApiConsumer()
    get_random_user = user_api_consumer.get_random_user()

    assert get_random_user.request.method == 'GET'
    assert get_random_user.request.url == 'https://randomuser.me/api/'
    assert get_random_user.status_code == 200
    assert isinstance(get_random_user.response['results'], list)

