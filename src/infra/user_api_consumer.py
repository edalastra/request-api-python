import requests

class UserApiConsumer:

    @classmethod
    def get_random_user(self) -> any:
       
        response = requests.get('https://randomuser.me/api/')

        return response.json()