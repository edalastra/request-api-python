from typing import Dict, List, Type
from src.domain.usecases import UserListColectorInterface
from src.data.interfaces import UserApiConsumerInterface

class UserListColector(UserListColectorInterface):

    def __init__(self, api_consumer: Type[UserApiConsumerInterface]) -> None:
        self.__api_consumer = api_consumer

    def list(self) -> List[Dict]:
        api_response = self.__api_consumer.get_random_user()
        users_formated_list = self.__format_api_response(api_response.response["results"])
        return users_formated_list

    @classmethod
    def __format_api_response(cls, results: List[Dict]):
        users_formated_list = []

        for user in results:
            users_formated_list.append({
                "id": user["id"]["value"],
                "full_name": f'{user["name"]["title"]} {user["name"]["first"]} {user["name"]["last"]}',
                "country": user['location']["country"],
                "state": user["location"]["state"],
            })
        return users_formated_list
