from typing import Tuple, Type
from collections import namedtuple
import requests
from requests import Request
from src.data.interfaces import UserApiConsumerInterface
from src.errors import HttpRequestError


class UserApiConsumer(UserApiConsumerInterface):

    '''
        Class to consumer the user api.
    '''

    def __init__(self) -> None:
        self.get_random_user_response = namedtuple('get_random_user_response', 'status_code request response')

    def get_random_user(self) -> Tuple[int, Request, dict]:
        '''
            Get a random user from the user api.
            :return - Tuple with the status code, request and response.
        '''

        req = requests.Request(
            method='GET',
            url='https://randomuser.me/api/'
        )

        req_prepered = req.prepare()
        response = self.__send_http_request(req_prepered)
        status_code = response.status_code

        if status_code >= 200 and status_code < 300:
            return self.get_random_user_response(
                status_code=status_code,
                request=req,
                response=response.json()
            )
        else:
            raise HttpRequestError(
                message=response.json['detail'], status_code=status_code
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