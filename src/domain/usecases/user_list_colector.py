from abc import ABC, abstractmethod
from typing import Dict, List

class UserListColectorInterface(ABC):
    '''
        User colector interface.
    '''

    @abstractmethod
    def list(self) -> List[Dict]:
        '''Must implement '''
        raise Exception('Not implemented')