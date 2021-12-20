from fastapi import APIRouter, Request as RequestFastAPI

users_routes = APIRouter()

@users_routes.get("/api/users/list")
def get_users(request: RequestFastAPI):
    ''' Get all users '''
    return { "Olá": "Mundo" }
