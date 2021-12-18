from collections import namedtuple
from faker import Faker

fake = Faker()

def mock_user():
    '''
        Mock data for user
        :return - dict with user data
    '''
    return {
            "gender": "female",
            "name": {
                "title": "Ms",
                "first": fake.name(),
                "last": fake.name()
            },
            "location": {
                "street": {
                    "number": fake.random_int(min=1, max=9999),
                    "name": fake.name()
                },
                "city": fake.name(),
                "state": fake.name(),
                "country": fake.name(),
                "postcode": fake.random_int(min=1, max=9999),
                "coordinates": {
                    "latitude": fake.random_int(min=-100, max=9999),
                    "longitude": fake.random_int(min=-100, max=9999)
                },
            },
            "id": {
                "name": "CPR",
                "value": "140361-2967"
            }
    }

class UserApiConsumerSpy:
    ''' Spy for UserApiConsumer '''
    def __init__(self) -> None:
        self.get_random_user_response = namedtuple('get_random_user_response', 'status_code request response' )

    def get_random_user(self) -> any:
        ''' mock to ger a random user '''
        return self.get_random_user_response(
            status_code=200,
            request=None,
            response={"results": [mock_user()]}
        )
