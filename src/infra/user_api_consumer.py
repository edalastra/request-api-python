from typing import Type
import requests
from requests import Request
from collections import namedtuple

class UserApiConsumer:

    def __init__(self) -> None:
        self.get_random_user_response = namedtuple('get_random_user_response', 'status_code request response')

    def get_random_user(self) -> any:
        req = requests.Request(
            method='GET', 
            url='https://randomuser.me/api/'
        )
        req_prepered = req.prepare()
        response = self.__send_http_request(req_prepered)

        return self.get_random_user_response(
            status_code=response.status_code,
            request=req,
            response=response.json()
        )

    @classmethod
    def __send_http_request(cls, req_prepered: Type[Request]) -> any:
        '''
            Send the request to the API and return the response.
            :param - req_prepered: The request object that has been prepared.
            :response - Http response raw
        '''

        http_session = requests.Session()
        response = http_session.send(req_prepered)
        return response