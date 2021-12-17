from .user_api_consumer import UserApiConsumer

def test_get_random_movie():
    ''' Test the get_random_iser method of UserApiConsumer class. '''    
    user_api_consumer = UserApiConsumer()
    response = user_api_consumer.get_random_user()

    return print(response)