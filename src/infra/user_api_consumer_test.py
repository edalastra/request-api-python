from .user_api_consumer import UserApiConsumer

def test_get_random_movie(requests_mock):
    ''' Test the get_random_iser method of UserApiConsumer class. '''    
   
    requests_mock.get('https://randomuser.me/api/', status_code=200, json={'results': [{'name': {'first': 'John', 'last': 'Doe'}}]})
   
    user_api_consumer = UserApiConsumer()
    response = user_api_consumer.get_random_user()

    return print(response)