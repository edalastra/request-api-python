from src.domain.usecases import UserListColectorInterface
from typing import Dict, List, Type
from src.infra import UserApiConsumer

class UserListColector(UserListColectorInterface):

    def __init__(self, api_consumer: Type[UserApiConsumer]) -> None:
        self.__api_consumer = api_consumer

    def list(self) -> List[Dict]:
       response = self.__api_consumer.get_random_user()
       print(response)