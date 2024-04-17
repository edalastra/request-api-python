from typing import Dict, Type
from src.domain.usecases.user_list_colector import UserListColectorInterface

class UsersListColectorController:
    ''' Controller to list users '''
    def __init__(self, user_list_colector: Type[UserListColectorInterface]) -> None:
        self.__use_case = user_list_colector

    def handle(self, http_request: Dict) -> Dict:
        ''' Handle to list colector '''

        page = http_request["query_params"]["page"]

        users_list = self.__use_case.list()

        http_reponse = { "status_code": 200, "data": users_list }

        return http_reponse
