from src.infra.user_api_consumer import UserApiConsumer
from src.data.usecases.user_list_colector import UserListColector
from src.presenters.controllers.users_list_colector_controller import UsersListColectorController


def get_users_composer():
    ''' Composer '''

    infra = UserApiConsumer()
    use_case = UserListColector(infra)
    controller = UsersListColectorController(use_case)

    return controller
