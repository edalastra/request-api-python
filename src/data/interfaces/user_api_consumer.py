from typing import Dict, Tuple, Type
from abc import ABC, abstractmethod
from requests import Request

class UserApiConsumerInterface(ABC):
    ''' Api consuemr interface '''
    @abstractmethod
    def get_random_user(self) -> Tuple[int, Request, dict]:
        ''' Must implement '''
        raise Exception('Not implemented')
